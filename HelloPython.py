import datetime
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
 
  title = print("Hello World!")
  now = datetime.datetime.now()
  heading = print("Current date and time is ")
  print(now.strftime("%A, %d-%m-%Y : %H:%M"))

  return (title , heading, now.strftime("%A, %d-%m-%Y : %H:%M"))
index()
