# PasswordFiner

API for analyzes text for password candidates.

Running the project:

```
pip install -r requirements.txt
python run app.py
```

The API can manually be used at `http://localhost:8080/api/passwords` 

The neural network is Bidirectional LSTM:

```
embedding_dimension = 20
dropout = 0.5
cells = 200

model = Sequential()
model.add(Embedding(total_chars, embedding_dimension, input_length=32, mask_zero=True))
model.add(Bidirectional(LSTM(cells)))
model.add(Dropout(dropout))
model.add(Dense(1, activation='sigmoid'))
```

It was trained on 2,000,000 passwords randomly selected from leaked password list and 2,000,000 extracted terms from
various Google dorked documents. The stats for the .1 test set are:

```
------------------
loss       :  0.04804224148392677
tn         :  199446.0
fp         :  731.0
fn         :  3281.0
tp         :  196542.0
------------------
accuracy   :  0.9899700284004211
precision  :  0.9962944984436035
recall     :  0.983580470085144
------------------
F1 score.     :  0.9898966618590025
------------------
```

The training notebook for the model is in  `./notebooks/password_model_bilstm.ipynb`

The False Positive model:

```
password-model from huggingface with new tokenizer (tokenizer i fixed)
```