from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
  print('How are u')
  return 'hello, new concept'

