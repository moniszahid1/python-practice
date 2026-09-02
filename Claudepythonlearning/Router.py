class Router:
    def __init__(self, hostname, connected_device):
        self.hostname=hostname
        self.connected_device=connected_device

    def check_capacity(self):
        if self.connected_device>50:
            return "full"
        elif self.connected_device>=20 and self.connected_device<=50:
            return "Normal"
        else:
            return "UnderUtilized"

r1=Router("edge01",65)
r2=Router("branch01",12)
print(f"Router {r1.hostname} capacity is {r1.check_capacity()}")
print(f"Router  {r2.hostname} capacity is {r2.check_capacity()}")