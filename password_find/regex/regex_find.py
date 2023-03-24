import re
import numpy as np
from utils.utils import *

# regex for 7-32 character mixed alphanumeric + special char


PATTERNS = ['^(?=.*[0-9])(?=.*[a-zA-Z])(?=.*[~!@#$%^&*_\-+=`|\()\{\}[\]:;"\'<>,.?\/])(?=.*\d).{8,32}$',
            "^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$",
            "^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$",
            "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$",
            "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$",
            "^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[*!@$%^&(){}?]).{8,32}$",
            "^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$",
            "^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?!.*\s).{4,8}$",
            "^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?!.*\s).{4,8}$",
            "(?!^[0-9]*$)(?!^[a-zA-Z]*$)^([a-zA-Z0-9]{6,15})$",
            "(?=^.{6,10}$)(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&amp;*()_+}{&quot;:;'?/&gt;.&lt;,])(?!.*\s).*$",
            "^(?=\S*[a-z])(?=\S*[A-Z])(?=\S*\d)(?=\S*[^\w\s])\S{8,}$",
            "^(?=[^A-Z\n]*[A-Z])(?=[^a-z\n]*[a-z])(?=[^0-9\n]*[0-9])(?=[^#?!@$%^&*\n-]*[#?!@$%^&*-]).{8,}$"
            "(?=^.{6,255}$)((?=.*\d)(?=.*[A-Z])(?=.*[a-z])|(?=.*\d)(?=.*[^A-Za-z0-9])(?=.*[a-z])|(?=.*[^A-Za-z0-9])(?=.*[A-Z])(?=.*[a-z])|(?=.*\d)(?=.*[A-Z])(?=.*[^A-Za-z0-9]))^.*"]


def init_regex():
    return [re.compile(pattern) for pattern in PATTERNS]


ALL_REGEX = init_regex()


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
