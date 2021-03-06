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

    word_to_index = {'<UNK>': 0}
    index_to_word = {0: '<UNK>'}

    for index, word in enumerate(set(cleaned_text)):
        word_to_index[word] = index + 1
        index_to_word[index + 1] = word

    return word_to_index, index_to_word

def convert_text_to_indices(cleaned_text, word_to_index):
    """
       Convert text to integer form.
    """

    numerical_text = [word_to_index[word] for word in cleaned_text]

    return numerical_text
