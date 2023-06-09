from multiprocessing import Process
import json
import os
import numpy as np

"""
Helpers
"""


def background_remove(path):
    """
    Backgroundable helper to remove the uploaded file.
    """
    task = Process(target=rm(path))
    task.start()


def rm(path):
    os.remove(path)


class NumpyEncoder(json.JSONEncoder):
    """
    Helper to JSONify numpy arrays.
    """

    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


def split_list_by_items_num_per_list(list_to_split, items_num_per_list):
    return [list_to_split[i * items_num_per_list:(i + 1) * items_num_per_list] for i in
            range((len(list_to_split) + items_num_per_list - 1) // items_num_per_list)]


def split_list_by_list_num(list_to_split, split_list_num):
    return [x.tolist() for x in np.array_split(list_to_split, split_list_num)]
