import tensorflow as tf
from fastapi import FastAPI
import uvicorn
from utils.inference_utils import *
from utils.utils_functions import *
from pipeline.pipeline import *
from utils.utils import *

from utils.thread_runner import ThreadRunner

app = FastAPI(description="Password Finder API")

PASSWORD_MODEL = tf.keras.models.load_model(SAVE_MODEL_PATH)

"""
Routes
"""


# API endpoint
@app.post("/api/passwords")
def passwords(input_data: TextData):
    texts = input_data.texts
    results = ThreadRunner.run_target_with_dask(process_document, texts)
    return json.dumps(results, cls=NumpyEncoder)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8080)
