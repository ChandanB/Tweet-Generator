import sys
import string
import re
import random

outcome_for = {}
user_input  = sys.argv[1]
dict = open('/Users/ChandanB/Library/Mobile Documents/com~apple~CloudDocs/Finesse Fulfilled/Tweet-Generator/fish.txt', 'r')
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

if __name__ == "__main__":
    word = str(user_input)
    hist_dict = histogram(text)
    for number in range(1, 100000):
        random_word(hist_dict)

    print("VALUE: " + str(outcome_for[word]))
    print("ERROR: " + str(abs(outcome_for[word] - 50000.0) / 500.0) + "%")
