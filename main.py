import pandas as pd
from full_pipline_positive import full_pipline as full_pipline_positive
from full_pipline_negative import full_pipline as full_pipline_negative


def extract_features_from_sequences(input_details):
    if input_details[5] != None:
        res = full_pipline_positive(input_details)
    else:
        res = full_pipline_negative(input_details,"to_delete")
    return res


def get_prediction(seq_features,org_name):
    #TODO add load_model function
    model = load_model(org_name)
    pred = model.predict(seq_features)
    return pred


def predict_sequences(miRNA_seq=None, mRNA_seq=None, site_seq=None,org_name="Human"):
    columns = ['key', 'paper name', 'organism', 'miRNA ID', 'miRNA sequence', 'site', 'region', 'valid_row',
                        'full_mrna', 'Gene_ID', 'region count']
    values = [None] * len(columns)
    values[4] = miRNA_seq
    values[5] = site_seq
    values[8] = mRNA_seq
    input_details = pd.DataFrame([values], columns = columns)
    seq_features = extract_features_from_sequences(input_details)
    prediction = get_prediction(seq_features,org_name)
    return prediction


if __name__ == '__main__':
    predict_sequences('UGAGGUAGUAGGUUGUAUAGUU', 'ACCAACUCCUCUUGACCGAUGUAGAUCACCUGGAAUGCUUGAA', 'UAUUGCACUUGUCCCGGCCUGU')
