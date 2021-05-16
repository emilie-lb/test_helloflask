from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
  return "Hello"

@app.route('/hello_world')
def hello_world():
  return 'Hello World'