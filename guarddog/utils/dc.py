from dataclasses import dataclass
from datetime import datetime


@dataclass
class UptimeKumaMonitorStatus:
    up: bool
    at = datetime.now()

    def __repr__(self):
        return f"<UptimeKumaMonitorStatus(up={self.up},at={self.at})>"


@dataclass
class UptimeKumaMonitor:
    name: str
    records: list[UptimeKumaMonitorStatus]

    def __repr__(self):
        return f"<UptimeKumaMonitor(name={self.name},record_count={len(self.records)})>"
