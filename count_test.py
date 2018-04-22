import os
import unittest


def word_count(filename, word):
    """Calculate the count of the 'word' in the'filename'. """
    try:
        with open(filename) as fhand:
            list_words = []
            for line in fhand:
                line = line.rstrip()
                list_words.extend(line.split())
            return list_words.count(word)

    except:
        return 0


class TstCase(unittest.TestCase):
    """use a fixture to include our required file"""
    def setUp(self):
        self.filename = 'C:/Users/Ibrahim Sharaby/Desktop/romeo.txt'
        word_count(self.filename, 'is')

    def test_no_deletion(self):
        word_count(self.filename, 'is')
        self.assertTrue(os.path.exists(self.filename))

    def test_count(self):
        self.assertTrue(word_count(self.filename, 'is'), 4)


if __name__ == '__main__':
    unittest.main()