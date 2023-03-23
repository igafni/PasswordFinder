import uuid
import zipfile
import os
import shutil


def process_zip(file_path, custom_regex=None):
    """
    Extracts a zip file of multiple documents and processes each.

    :param file_path: The path of the document to process.
    :return: A list containing the result dictionaries from process_document().
    """

    results = []

    # generate a random folder for extraction
    zip_folder = f"static/{uuid.uuid4().hex}/"

    # extract all the files from the zip
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(zip_folder)

    # process each file extracted
    for root, dirs, files in os.walk("static"):
        for file in files:
            full_path = os.path.join(root, file)
            if not file.endswith(".zip") and not file.startswith("~") and not file.startswith(".") and os.path.getsize(
                    full_path) != 0:
                try:
                    results.append(process_document(full_path, custom_regex))
                except:
                    print(f"[!] Error processing '{full_path}'")

    # cleanup the extracted folder
    shutil.rmtree(zip_folder)

    return results
