import requests

from . import dc


class UptimeKuma:
    monitors = {}

    def __init__(self, uk_address, uk_token):
        self.address = uk_address
        self.token = uk_token

    def __repr__(self):
        return f"<UptimeKuma(address={self.address},monitors={self.monitors})>"

    def get_monitors(self):
        print(f"Updating monitors from {self.address}")
        response = requests.get(self.address, auth=("", self.token))
        lines = response.text.split("\n")
        print(f"Retrieved {len(lines)} lines from UptimeKuma")
        for line in lines:
            if line.startswith("monitor_status"):
                monitor_name, monitor_status = self.parse_monitor_line(line)
                if monitor_name in self.monitors.keys():
                    self.monitors[monitor_name].records.append(monitor_status)
                else:
                    monitor = dc.UptimeKumaMonitor(
                        name=monitor_name, records=[monitor_status]
                    )
                    self.monitors[monitor_name] = monitor

    @staticmethod
    def parse_monitor_line(monitor_line: str) -> (str, dc.UptimeKumaMonitorStatus):
        open_bracket_index = monitor_line.find("{")
        close_bracket_index = monitor_line.find("}")
        monitor_state = monitor_line[close_bracket_index + 1 :].strip()
        up_status = True if monitor_state == 1 else False
        monitor_details = monitor_line[
            open_bracket_index + 1 : close_bracket_index
        ].split(",")
        for monitor_detail in monitor_details:
            if monitor_detail.startswith("monitor_name"):
                monitor_name = monitor_detail.split("=")[1].strip('"')
        monitor_status = dc.UptimeKumaMonitorStatus(up=up_status)
        return (monitor_name, monitor_status)
