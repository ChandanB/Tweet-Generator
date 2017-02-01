import random
import sys


def random_argument():
    random_index = random.randint(1, len(sys.argv) - 1)
    return sys.argv[random_index]

if __name__ == '__main__':
    for i in range(1, len(sys.argv)):
        random_word = random_argument()
        print(random_word + " ")
