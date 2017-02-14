from randomWordDictionary import get_sentence
from randomWordDictionary import get_word
from flask import Flask
import os


app = Flask(__name__)

@app.route('/')
def generate_word():
    word = get_word()
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
    #uncomment to run on heroku
    # port = int(os.environ.get('PORT', 5000))
    # app.run(host='0.0.0.0', port=port)
    app.run(debug=True, port=33507)

    # uncomment to run locally
    # app.run()
