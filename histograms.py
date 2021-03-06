#!python
from __future__ import division, print_function

class Dictogram(dict):

    def __init__(self, iterable=None):
        """Initialize this histogram as a new dict; update with given items"""
        super(Dictogram, self).__init__()
        self.types = 0  # the number of distinct item types in this histogram
        self.tokens = 0  # the total count of all item tokens in this histogram

        if iterable:
            self.update(iterable)

    def update(self, iterable):
        """Update this histogram with the items in the given iterable"""
        index = 0
        pair_dict = {}
        for item in iterable:
            # TODO: increment item count'
            if index < 7:
                next_word = iterable[index + 1]
                pair_dict[item] = next_word
                #print(pair_dict)

            if item not in self:
                self[item] = 1
                self.types += 1
            elif item in self:
                self[item] += 1

            self.tokens += 1
            index += 1
            pass

    def count(self, item):
        """Return the count of the given item in this histogram, or 0"""
        # TODO: retrieve item count

        pass

def test_histogram(text_list):
    print('text list:', text_list)

    hist_dict = Dictogram(text_list)
    print('dictogram:', hist_dict)

    #hist_list = Listogram(text_list)
    #print('listogram:', hist_list)


def read_from_file(filename):
    """Parse the given file into a list of strings, separated by seperator."""
    return file(filename).read().strip().split()


if __name__ == '__main__':
    import sys
    arguments = sys.argv[1:]  # exclude script name in first argument
    if len(arguments) == 0:
        # test hisogram on letters in a word
        word = 'abracadabra'
    #    test_histogram(word)
        print()
        # test hisogram on words in a sentence
        sentence = 'one fish two fish red fish blue fish'
        word_list = sentence.split()
        test_histogram(word_list)
    elif len(arguments) == 1:
        # test hisogram on text from a file
        filename = arguments[0]
        text_list = read_from_file(filename)
        test_histogram(text_list)
    else:
        # test hisogram on given arguments
        test_histogram(arguments)
