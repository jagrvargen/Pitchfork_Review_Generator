""" Helper functions for text processing. """

import nltk.tokenize.punkt as punkt
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
    text = re.sub(regex, ' ', text)

    """ Save cleaned parsed text for later use. """
    with open('data/parsed_text.txt', 'w+', encoding='utf-8') as f:
        f.write(text)

    return text

def clean_and_tokenize_text(text):
    """
       Convert all text to lowercase and tokenize at the sentence level.
    """

    tokenizer = punkt.PunktSentenceTokenizer()
    cleaned_text = tokenizer.tokenize(text.lower())

    return cleaned_text
