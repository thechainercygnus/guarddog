from guarddog.utils import UptimeKuma

uk_address = "http://192.168.71.252:3001/metrics"
uk_token = "uk2_Oz4b1NVb1zCL1JHp4a-XdgJpLoBzD01Y6kCX5UaQ"
uk_mon = UptimeKuma(uk_address=uk_address, uk_token=uk_token)
uk_mon.get_monitors()
print(uk_mon.monitors["Gate"].records)
print
