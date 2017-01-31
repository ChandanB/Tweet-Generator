import random
import sys

user_input = sys.argv[1:]
words_file = open('/usr/share/dict/words')

def random_argument():
    random_index = random.randint(1, words_file - 1)
    return sys.argv[random_index]

if __name__ == '__main__':
    for i in range(1, len(words_file):
        random_word = random_argument()
        print(random_word + " ")
