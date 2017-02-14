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
if __name__ == '__main__':
    count = int(user_input)
    for i in range(1, count):
        new_word = get_word()
        word = new_word.strip()
        sentence.append(word)
    print (" ")
    random_sentence =  " ".join(sentence)
    full_sentence = random_sentence + "."
    print full_sentence
    print (" ")
