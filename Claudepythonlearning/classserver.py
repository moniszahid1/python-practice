class Server:
    def __init__(self,name,cpu_usage):
        self.name=name
        self.cpu_usage=cpu_usage

    def get_status(self):
        if self.cpu_usage>90:
            return "critical"
        elif self.cpu_usage>70:
            return "Alarming"
        else:
            return "Normal"
web01 =Server("web01",78)
print(web01.name)
print(web01.cpu_usage)
print(web01.get_status())


    