server = {
    "name":"web01",
    "status":"active",
    "cpu_usage":45
    }
print(f"complete server details" ,server)
print (f"Status of the server is ", server["status"])
#print("Status:", server["status"])
server["cpu_usage"]=78
print(f"updated cpu usage of the server {server["name"]} is {server["cpu_usage"]} which was earlier 45")
server["region"]="us-east-1"
print(f"complete server details" ,server)
del server["status"]
print(f"complete server details" ,server)
