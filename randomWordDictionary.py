import application

from flask import Flask
app = Flask(__name__)

from application import full_sentence
print full_sentence

@app.route('/')
def hello_world():
    return full_sentence
