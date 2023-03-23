import numpy as np
from password_find.model.tokenize import *
from utils.utils import *
from app import PASSWORD_MODEL

MINIMUM_PRED = 0.5


def extract_passwords_model(document):
    """
    Tokenizes the input text, submits it to the served model, and returns words that might be passwords.

    :param document: The string representing the text of a single document.
    :return: A list of any possible passwords.
    """

    # extract whitespace stripped words
    words = np.array([word.strip() for word in document.split()])

    # turn the input words into sequences and pad them to 32
    tokenized_words = [tokenize(word) for word in words]

    # post the tokenized words to the served model
    pred = PASSWORD_MODEL.predict(tokenized_words)

    # properly cast the predictions for each word
    pred = (pred > MINIMUM_PRED).astype("int32")

    # use the predictions as indicies for the words to return
    positive_indicies = np.where(pred == 1)
    passwords = list()

    for x in positive_indicies[0]:
        left_context = words[:x][-CONTEXT_WORDS:]
        password = words[x]
        right_context = words[x + 1:CONTEXT_WORDS + x + 1]

        result = {
            "left_context": left_context,
            "password": password,
            "right_context": right_context
        }

        passwords.append(result)

    return passwords
