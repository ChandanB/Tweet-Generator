import randomWordDictionary

from flask import Flask
app = Flask(__name__)

from randomWordDictionary import full_sentence
print full_sentence

@app.route('/')
def hello_world():
    return full_sentence
