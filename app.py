from randomWordDictionary import get_sentence
from randomWordDictionary import get_word
from flask import Flask


app = Flask(__name__)

@app.route('/')
def generate_word():
    word = get_word()
    return '''
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
    app.run()
