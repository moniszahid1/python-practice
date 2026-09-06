class Device:
    def __init__(self,hostname):
        self.hostname = hostname

    def ping(self):
        return f"{self.hostname} is reachable"
class Server(Device):
    def __init__(self, hostname, cpu_usage):
        super().__init__(hostname)
        self.cpu_usage = cpu_usage

    def get_status(self):
        if self.cpu_usage > 90:
            return "critical"
        elif self.cpu_usage > 70:
            return "warning"
        else:
            return "normal"

srv = Server("web01",55)

print(srv.ping())
print(srv.get_status())


                

        