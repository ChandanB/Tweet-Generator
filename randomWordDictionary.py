import random
import sys

from flask import Flask
app = Flask(__name__)

words_file = open('/usr/share/dict/words')
words_list = words_file.readlines()
user_input = sys.argv[1]
sentence   = []

#4
def get_word():
        random_index = random.randint(1, len(words_list))
        random_word = words_list[random_index]
        return random_word

#10
def get_sentence(count):
    for i in range(count):
        new_word = get_word()
        word = new_word.strip()
        sentence.append(word)
    full_sentence = ' '.join(sentence)
    return full_sentence

if __name__ == '__main__':
    count = int(user_input)
    random_sentence = get_sentence(count)
    print random_sentence
    print (" ")
