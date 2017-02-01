import sys
import string
from operator import itemgetter

words_file = open('/Users/ChandanB/Library/Mobile Documents/com~apple~CloudDocs/Finesse Fulfilled/Tweet-Generator/Bible.txt')
story = str(words_file.read())
dict_as_unique_word = dict()
story_stripped = story.translate(None, string.punctuation)
story_split = story_stripped.split()
user_input = sys.argv[1]
words_tuple = tuple()

def histogram(source_text):
    for word_index in range(1, len(source_text)):
        current_word = story_split[word_index]
        if current_word not in dict_as_unique_word:
            dict_as_unique_word.update({current_word : 1})
        elif current_word in dict_as_unique_word:
            dict_as_unique_word[current_word] += 1
    words_tuple = [(name,number) for (name,number) in dict_as_unique_word.iteritems()]
    tuple_sorted = sorted(words_tuple, key=itemgetter(1), reverse = True)
    print(tuple_sorted)

def word_count(user_input):
    if user_input in dict_as_unique_word:
        if str(dict_as_unique_word[user_input]) is "1":
            print (user_input + " appears a mere " + str(dict_as_unique_word[user_input]) + " time")
        else:
            print(user_input + " appears " + str(dict_as_unique_word[user_input]) + " times")
    else:
        print(user_input + " appears 0 times")

if __name__ == '__main__':
    count = str(user_input)
    histogram(story_split)
    word_count(count)







#words_count = Counter(story_split)
#print(words_count)
