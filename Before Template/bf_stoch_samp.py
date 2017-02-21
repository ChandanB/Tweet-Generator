import sys
import string
import re
import random

outcome_for = {}
user_input  = sys.argv[1]
sentence   = []
dict = open('Bible.txt', 'r')
text = dict.read()
dict.close()

def histogram(source_text):
    histogram = {}
    for word in source_text.split():
        word = word.translate(None, string.punctuation)
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1

    print (histogram)
    return histogram

def random_word(histogram):
    probability = 0
    random_index = random.randint(1, sum(histogram.values()))

    for word in histogram:
        probability += histogram[word]
        if probability >= random_index:
            if word in outcome_for:
                outcome_for[word] += 1
            else:
                outcome_for[word] = 1
            return word

def return_random():
    random_word = random_word(hist_dict)

def get_sentence(count):
    count = str(user_input)
    hist_dict = histogram(text)
    for i in range(count):
        random_word(hist_dict)
        new_word = random_word(hist_dict)
        word = new_word.strip()
        sentence.append(word)
    full_sentence = ' '.join(sentence)
    return full_sentence

if __name__ == "__main__":
    count = str(user_input)
    get_sentence(count)
    random_sentence = get_sentence(count)
    hist_dict = histogram(text)
    print("VALUE: " + str(outcome_for[word]))
    print("ERROR: " + str(abs(outcome_for[word] - 50000.0) / 500.0) + "%")
