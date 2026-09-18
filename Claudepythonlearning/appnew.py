from flask import Flask, request
appnew=Flask(__name__)
@appnew.route("/")
def home():
    return"Welcome to my first API"
@appnew.route("/status")
def status():
    return{"Server":"web","status":"running"}
@appnew.route("/server/<name>/<status>/<cpu_usage>")
def get_status(name,status,cpu_usage):
    return{"Server":name,"status":status,"cpu_usage":cpu_usage}
@appnew.route("/server",methods=["POST"])
def create_server():
    data=request.get_json()
    return{"message":"server created","data":data}
if __name__=="__main__":
    appnew.run(debug=True)
