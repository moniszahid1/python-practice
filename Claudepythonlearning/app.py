from flask import Flask, request

app=Flask(__name__)

@app.route("/")
def home():
    return("welcome to my first api")
@app.route("/status")
def status():
    return{"Server":"monis01","status":"running"}
@app.route("/status/<name>")
def get_name(name):
    return{"server":name,"status":"running"}
@app.route("/server/<name>/<cpu_usage>/<language>")
def get_server_cpu(name,cpu_usage,language):
    return{"server":name,"status":"running","cpu_usage":cpu_usage,"language":language}

@app.route("/status", methods=["POST"])
def create_server():
    data=request.get_json()
    return {"message":"Server is created","server":data}
if __name__=="__main__":
    app.run(debug=True)

