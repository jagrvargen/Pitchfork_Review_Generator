""" Helper functions for text processing. """

from nltk.tokenize import word_tokenize

import re
import string


def get_raw_text():
    """ 
       Retrieve text data and remove most punctuation and irrelevant
       SQL syntax.
    """

    with open('data/reviews_corpus.txt', 'r', encoding='utf-8') as f:
        text = f.read()

    regex = re.compile(u"INSERT INTO content VALUES\(\d+,\'|\'\);|[^a-zA-Z_.0-9]")
    text = re.sub(regex, ' ', text).strip()

    """ Save cleaned parsed text for later use. """
    with open('data/parsed_text.txt', 'w+', encoding='utf-8') as f:
        f.write(text)

    return text

def clean_and_tokenize_text(text):
    """
       Convert text to lowercase and tokenize at the word level.
    """

    cleaned_text = word_tokenize(text.lower())

    return cleaned_text

def create_dictionaries(cleaned_text):
    """
       Create dictionaries to map words to indices and vice versa.
    """

    word_to_index = dict()
    index_to_word = dict()

    for index, word in enumerate(set(cleaned_text)):
        word_to_index[word] = index
        index_to_word[index] = word

    return word_to_index, index_to_word
