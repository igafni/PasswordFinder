from password_find.regex.regex_find import extract_terms_regex, ALL_REGEX
from password_find.model.model_find import extract_passwords_model
from utils.utils import *
from false_positive.false_positive import false_positive
import tensorflow as tf
import numpy as np


def process_document(text, custom_regex=None):
    """
    Processes a file through the NN/regex.

    :param text: text to predict on.
    :return: A dictionary containing the file name, model password candidates, and regex password candidates.
    """

    results = []

    n = 50000

    # chunkify things if needed because of the memory limits for the deep learning model (TODO: double check this)
    chunks = [text[i:i + n] for i in range(0, len(text), n)]
    model_password_candidates = list()

    for chunk in chunks:
        # extract password candidates from the model
        model_password_candidates.extend(extract_passwords_model(chunk))

    print(f"[*] Number of model password candidates: {len(model_password_candidates)}")

    # extract password candidates from the regex
    regex_password_candidates = extract_terms_regex(text, ALL_REGEX)

    print(f"[*] Number of regex password candidates: {len(regex_password_candidates)}")

    # check for any custom regex
    custom_regex_matches = None
    if (custom_regex):
        custom_regex_matches = extract_terms_regex(text, custom_regex)
    model_password = [res['password'] for res in model_password_candidates]
    model_password = model_password if model_password else []
    regex_passwords = [res['password'] for res in regex_password_candidates]
    regex_passwords = regex_passwords if regex_passwords else []
    passwords = list(np.unique(model_password + regex_passwords))
    false_positive_passwords = false_positive(passwords)
    # TODO: Send for Vader password check for false positive (password-model from huggingface with new tokenizer)
    long_result = {
        'candidates_password': passwords,
        'false_positive_passwords': false_positive_passwords,
        'number_of_model_password_candidates': len(model_password_candidates),
        'number_of_regex_password_candidates': len(regex_password_candidates),
        'model_password_candidates': model_password_candidates,
        'regex_password_candidates': regex_password_candidates,
        'custom_regex_matches': custom_regex_matches
    }
    short_result = {
        'candidates_password': passwords,
        'model_password_candidates': model_password,
        'regex_password_candidates': regex_passwords,
        'false_positive_scores': false_positive_passwords
    }

    return short_result
