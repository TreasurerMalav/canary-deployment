import socket
from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello():
#    print request.headers
    return "Hello World from Stable app!" + "\n" + "Pod name is: " + socket.gethostname()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
