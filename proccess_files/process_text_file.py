def extract_text(file_path):
    """
    extract_text Extracts plaintext from a document path using Tika.

    :param file_path: The path of the file to extract text from.
    :return: ASCII-encoded plaintext extracted from the document.
    """
    with open(file_path, 'r') as file:
        return file.read()
