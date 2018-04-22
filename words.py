""" retrieve and print items from a plain text document
from a url.
Usage:
    python words.py <url>
"""

import sys


def fetch_words(url):
    """ Fetch a list of words from a plain text document

    Args:
        url: the path of the text document
	
    Returns:
        A list of the words in the text document
    """
    with open(url) as story:
        story_words = []
        for line in story:
            line_words = line.split()
            for word in line_words:
                story_words.append(word)
        story.close()
    return story_words
		
		
def print_words(story_words):
    """ print items one per line

    Args:
        story_words: an iterable series 

    Returns:
        Returns None
    """	
    for word in story_words:
        print(word)
		

def main(url):
    """ print each item from the palin text document

    Args:
        url: the path to a plain text document
	
    Returns:
        Return None
    """
    words = fetch_words(url)
    print_words(words)

	
if __name__ == '__main__':
    main(sys.argv[1])