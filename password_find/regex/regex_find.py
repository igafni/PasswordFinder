import re
import numpy as np
from utils.utils import *

# regex for 7-32 character mixed alphanumeric + special char
PASSWORD_REGEX = re.compile('^(?=.*[0-9])(?=.*[a-zA-Z])(?=.*[~!@#$%^&*_\-+=`|\()\{\}[\]:;"\'<>,.?\/])(?=.*\d).{8,32}$')

# HINT_REGEX = re.compile('([Ll]ogin.)?([Ll]ogyn.)?([Pp]ass.)?([Pp]assword.)?([Pp] password.)?([A-Za-z0-9@#$%^&+=]{7,})')

ALL_REGEX = [PASSWORD_REGEX]


def extract_terms_regex(document, regexs):
    """
    extract_terms_regex Runs the supplied compiled regex against extracted documents.

    :param document: The string representing the text of a single document.
    :return: A list of terms matching the regex.
    """

    words = np.array([word.strip() for word in document.split()])
    passwords = list()
    for regex in regexs:
        for x, word in enumerate(words):
            if regex.match(word):
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


