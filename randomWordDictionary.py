import random
import sys

words_file = open('/usr/share/dict/words')
words_list = words_file.readlines()
user_input = sys.argv[1]
sentence   = []

def get_word():
        random_index = random.randint(1, len(words_list))
        random_word = words_list[random_index]
        return random_word

if __name__ == '__main__':
    count = int(user_input)
    for i in range(1, count):
        new_word = get_word()
        word = new_word.strip()
        sentence.append(word)
    print (" ")
    random_sentence =  " ".join(sentence)
    print random_sentence + "."
    print (" ")
