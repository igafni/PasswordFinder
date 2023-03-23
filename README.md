# PasswordFiner

API for analyzes text with ML for password candidates.

(based on deeppass-finding-passwords-with-deep-learning article by Will Schroeder)

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

Notes about False Positive:
```
The model accuracy is 99%.

Finding password is a big issue because of the ratio of rare events (like a word in a document being a password).

Let’s say we download 100 documents that average 5000 words each, 
and 10 of those documents have a single password within them. 
That means among the 500,000 candidate words we’re going to process only 10 are passwords. 
Where does a 99% accuracy rate get us?

499,990 non-passwords * 99% accuracy = 494990 true negative non-passwords + 5000 false positive passwords

10 passwords * 99% accuracy = 0 false negative non-passwords, 10 true positive passwords

We likely will flag all of the passwords, but we’ll also have 5000 false positives! 
This is a big issue that’s similar to the false positive problem that plagues detection analysts. 
When a true positive is a relatively rare event in a large dataset, 
like a password in a document or real intrusion on a host in a large network, 
even very accurate models will produce a large number of false positives.
```