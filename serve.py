from flask import Flask, request
import socket
import subprocess

app = Flask(__name__)

data = {'num':0}

@app.route('/', methods = ['POST', 'GET'])
def hello_world():
   global data
   if (request.method == 'GET'):
      return socket.gethostname()
   if (request.method == 'POST'):
      args = ['python3', 'stress_cpu.py']
      proc = subprocess.Popen(args)
      return 'Success'


if __name__ == "__main__":
 app.run(host = "0.0.0.0")
