import datetime
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
 
  title = "Hello World!"
  now = datetime.datetime.now()
  status = now.strftime("%A, %d-%m-%Y : %H:%M")

  return status/

message = index()
print(message)
