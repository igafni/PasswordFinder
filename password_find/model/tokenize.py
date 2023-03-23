

CHAR_DICT = {'<UNK>': 1, 'e': 2, 'i': 3, 'a': 4, 'n': 5, 't': 6, 'r': 7, 'o': 8, 's': 9, 'c': 10, 'l': 11, 'A': 12,
             'E': 13, 'd': 14, 'u': 15, 'm': 16, 'p': 17, 'I': 18, 'S': 19, 'R': 20, 'O': 21, 'N': 22, 'g': 23, 'T': 24,
             '-': 25, 'L': 26, 'h': 27, 'y': 28, 'C': 29, 'b': 30, 'f': 31, 'M': 32, 'v': 33, 'D': 34, '1': 35, 'U': 36,
             'H': 37, 'P': 38, 'k': 39, '2': 40, '0': 41, 'B': 42, 'G': 43, 'w': 44, 'Y': 45, 'K': 46, '3': 47, '9': 48,
             'F': 49, '.': 50, ',': 51, '4': 52, '8': 53, 'V': 54, '5': 55, '7': 56, '6': 57, 'W': 58, 'j': 59, 'x': 60,
             'z': 61, 'J': 62, 'q': 63, 'Z': 64, '_': 65, "'": 66, ':': 67, 'X': 68, 'Q': 69, '/': 70, ')': 71, '(': 72,
             '"': 73, '!': 74, ';': 75, '*': 76, '@': 77, '\\': 78, ']': 79, '?': 80, '[': 81, '<': 82, '>': 83,
             '=': 84, '#': 85, '&': 86, '$': 87, '+': 88, '%': 89, '`': 90, '~': 91, '^': 92, '{': 93, '}': 94, '|': 95}


def tokenize(word):
    """
    Tokenizes and pads the supplied word to the proper length.

    :param word: The word to tokenize.
    :return: A 32 val numpy array of representing the character tokenization of the word.
    """

    global CHAR_DICT

    if len(word) < 7 or len(word) > 32:
        return [0] * 32
    else:
        seq = [CHAR_DICT[char] if char in CHAR_DICT else 1 for char in word]
        seq.extend([0] * (32 - len(seq)))
        return seq
