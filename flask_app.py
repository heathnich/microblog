
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home_page():
	return 'work in progress'

@app.route('/hello')
def hello_page():
    return 'Hello jnicho49'

