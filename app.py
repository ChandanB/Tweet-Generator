from stoch_samp import get_sentence
from stoch_samp import random_word
from flask import Flask
import os


app = Flask(__name__)

@app.route('/')
def random_word():
    word = random_word()
    return '''
    <!doctype html>
    <html>
        <head>
            <title>Random Words and Sentences</title>
        </head>
        <body>
            <h1>''' + word + '''</h1>
        </body>
    </html>
    '''

@app.route('/<int:num>')
def generate_sentence(num):
    sentence = get_sentence(num)
    return '''
    <!doctype html>
    <html>
        <head>
            <title>Random Words and Sentences</title>
        </head>
        <body>
            <h1>''' + sentence + '''</h1>
        </body>
    </html>
    '''

if __name__ == '__main__':
    #uncomment the next two lines to run on heroku
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

    # uncomment to the next line run locally
    # app.run()
