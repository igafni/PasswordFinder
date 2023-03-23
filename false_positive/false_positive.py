from app import MODEL_PIPELINE


def false_positive(passwords):
    results = MODEL_PIPELINE(passwords)
    all_data = []
    for i, res in enumerate(results):
        data = {}
        data['password'] = passwords[i]
        data['score_false_positive'] = res[0]['score']
        data['score_true_positive'] = res[1]['score']
        all_data.append(data)
    return all_data
