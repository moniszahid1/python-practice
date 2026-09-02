
def get_server_status(cpu_usage):
    if cpu_usage>=95:
        return "Critical"
    if cpu_usage>=70:
        return "Alarming"
    else:
        return "Normal"

print(get_server_status(98))
print(get_server_status(70))
print(get_server_status(30))