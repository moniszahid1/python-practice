import json

server = {"name": "web01", "status": "running", "cpu_usage": 78}

with open("server.json", "w") as f:
    json.dump(server, f)

with open("server.json", "r") as f:
    data = json.load(f)

print(data)
print(data["name"])
print(type(data))
with open("server.json", "w") as f:
    json.dump(server, f, indent=4)
with open("server.json", "w") as f:
    json.dump(server, f, indent=4)
