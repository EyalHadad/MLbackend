import pandas as pd
from full_pipline_positive import full_pipline as full_pipline_positive
from full_pipline_negative import full_pipline as full_pipline_negative
import pickle
from consts.global_consts import list_of_features_for_web as features

def load_model(org_name):
    with open(org_name, 'rb') as f:
        model = pickle.load(f)
    return model

def extract_features(miRNA=None, mRNA=None, site=None):
    columns = ['key', 'paper name', 'organism', 'miRNA ID', 'miRNA sequence', 'site', 'region', 'valid_row',
                        'full_mrna', 'Gene_ID', 'region count']
    values = [None] * len(columns)
    values[4] = miRNA
    values[5] = site
    values[8] = mRNA
    dataset = pd.DataFrame([values], columns = columns)

    if site != None:
        result_df = full_pipline_positive(dataset)
    else:
        result_df = full_pipline_negative(dataset)
        result_df.drop('site_x', axis=1,inplace=True)

    return result_df


def extract_features_from_sequences(df):

    if df['site'].iloc[0] != None:

        result_df = full_pipline_positive(df)
    else:
        result_df = full_pipline_negative(df)
        result_df.drop('site_x', axis=1,inplace=True)

    return result_df


def get_prediction(seq_features,org_name):

    # load the model (the names ends with .model)
    model = load_model(org_name)

    # leave only the columns that the model trained on (list in consts.global_consts)
    columns_to_keep = list(set(seq_features.columns) & set(features))

    # get the features (requires using the viennaRNA module)
    seq_features = seq_features[columns_to_keep]

    # predict 1 for True 0 for False
    pred = model.predict(seq_features)
    return pred


# def filter_columns(seq_features):
#
#     features_to_remove = ['miRNA ID', 'miRNA sequence', 'Gene_ID', 'new_key', 'MiRBase ID',
#                           'Node of origin (locus)', 'Node of origin (family)', 'Family Age_Group',
#                           'Family Age', 'Locus Age', 'seed_family', 'site', 'region', 'paper region',
#                           'sequence', 'Gene_name', 'mrna_bulge', 'mrna_inter', 'mir_inter',
#                           'mir_bulge', 'duplex_method'
#                           ]
#
#     # removing features
#     features_to_remove = list(set(seq_features.columns).intersection(features_to_remove))
#     seq_features = seq_features.drop(columns=features_to_remove)
#
#     # Remove datatypes that are not numeric
#     seq_features = seq_features.select_dtypes(include=['float64', 'int64'])
#
#     seq_features.drop(['index', 'key'], axis=1)
#     return seq_features


def predict_sequences(miRNA_seq=None, mRNA_seq=None, site_seq=None,org_name="Human"):

    seq_features = extract_features(miRNA_seq, mRNA_seq, site_seq)
    prediction = get_prediction(seq_features, org_name)
    return prediction


if __name__ == '__main__':
    print(predict_sequences('UGGAGUGUGACAAUGGUGUUUG',
                            'CAAUAGAUGUGAGUUAAACUUUAGGAAAAAGGAUUCCCUUUUUUUAAAAAAAAUCAAUACCUCAAAAGCAGGCUUUGGGACAAGAAAACCCCAAAGUGGCCUGCUUUUCCCAUCCCAGGAGCUCAUUAUCCAGUCUGUGCCAACUGAAGUAGGAGACUGACUGUGAGUGCUGGCUAAAAGCCCUGGGUGGUGAGGCUCACAGUACUGGUUUCCAGGAGGAAGAGCCUUUGUGCAUUUGACUGAGGCCAGUUUCUAUGAAGAGCAAGUAGCUGAGGAGAGGUCGAAUUUACUGCUUUUUCCAGGACAAUUCUGGAAGUAAAGAAAAUGUAAUUCAAGCUGGUUAGCUUAAUUUUGUGCCAUUCUUUAACAUAAGAGUAAGCUCUAUUAUGAAAUACAACUUUAAAAAAUUUUAGCUAUAAAUUAUAUAAAUGAUUUUAAAUUGCUGAGGUUUCCUUAGGCAGCUUAUUUAUUUGUUUACAGUUAGACUAUCUGAGUAAAUGGUUCUUUGUGGACCUAGGCAGUUCCUGACUGUUCCACAUGUAGUACAUUGUACCAAAGUUCUUAAUAAGAAUAUUCCCCACAAUCCUGUUCUCUAAAUGUCAAAUAAAGAUUAUUUUCACUAGAUUCAACUUUACAAAAUUUGUUUUAUAUCUGUUAGAAAAUGUACAGACAUAAGUAUUUUCAGUUGACAAAGCAUCAAACCCAGUUCUGCCUAGUGAUAAGUUUCACCCUAGAGUAUGUAUGUAACGUUUUAGCUUAUCCAUCCUUUCUUGGAGCGCCUCCAUUUCCAUUGAAAGCCAGGCUGGAGCAGGACCCUUUUGGAGUAGUGACUCAGUUGCUUCCAAAGCCCCUGCUAUUGUAUGCAGCGCUGACCUGUACUCUUCUUCCCAGGGGAACUCCUGACGAGCUCUUUUUGCAUAAGGCUGGAAAAAAAACAUAAGUAAUAUCACAAUAUCCAUUCUAAAUAUAAAGAACCUUCCUUUUGGACUGGAGUAAAGCUUACAUGCAAAUUUUAUUCUAGUCAUUGGAUCACAAGGGUAGGAGGAUGCACCCCAAAACCCCUACACAGUCAUCUAGAAAAAUAUGUAAAGGCAUUUUGGUUUAUCAUAGCAAUUCAGAGUGCUACUACCAGUGUCUUAGUUUGUAUGUGGUAUACAACAAGUAUCCUGUCCCAAAGGGCUCCCAAUGAGAAGUGCUGCAUAGUCCAAGCUUACAUGUCUUAUAAACAAGUUCAUAAAUGUAUUUUCUUUUUAUGAGAGUUUGACUAAAACUUAUCAGAAUGUUGUUCUUCAUGAAUUACUACUAUACUAAUUACUAUACUAAUAGUGCUCAAAACAAUAUUUUGAAUAUCCUUAUUGGUGUCAAAUUCUGCCUUUUAAUAAGUAGAUGUGAUCUUCAGUUACUGCCAAAAAUUAUUAGGAGACUCAUUUGAUUAAUAAGGCAAGGAAUCAAACUAAACAUUUAGGAGUAAGUUUCUUUCAUUUUCUUCUGUGGUUCAGUAAAGACUGCAUUUAUAGCAUCACUGGUACAAUAUGUAACUUCCCUUAAAGGUUACUACCAAUAAUUCAAACAUACUGAAAGAAUAUAUUUGAUAUGGUGUAGUCCCACUUCUUAAUUUUAAAAGCAACUACCAUAAAACAGAAUUUUACAUGUCUAGAUCUAUUUGAUUUGAAAUUCAGCAUAAGGCUGGAAACCACACUGGUUUGUUUCGUCAGUAAGUAAAAAGGGCAGAAUUUGCCUUGUUAAAGUUUGGCCCCUAUUGAAAUCAGCCCAUACCUGUAAAGAUGACCUCUUUGCUUCUUCUACAGUCACAUUAGCAAAGGGUUCCCAGAAAAUACCUUUUUCCUGUUUCACACGUUCCACUUUGGCAGCUUCAGUUUCAUCUACAAACCCAGUCUGCCAGGGACCAUGAAAAACCAAGCAAAUAGCAACAUGUUAGCACUCUACUAGAUAUGAAAUGGCCACAUAAUUUAAGUGCUGAGUGUUCAACCAUACUAGGCAAAUUCUGGAAGUCACAUGGACUGAUCUAUAAAUACUCUUAGUAUAAUCUGGAUUAAAUCACUCUACUGUGUUCUUCCUUACAAAAUAGUUAGUUAUAGAGUUGUCUUUGCAGGAAAAAAUGAUAGUCUGCUAACCUUUACUGUAUAAGCUAAGAAACUGGCAACAGCAGUGUAUACACAUGUACUUAAAAUCCAGCUUAGAUGUAAUAUAAGUAGGCCAAGUGUGGUGGCUCAUGCCUCUAAUCCCAGGACUUUGGUGGGAGGAAUGCUUGAGCCCAGGAGUUUGAGGUUAUAGCGAGCUAUGAUCACACCACCACACUCCAAUCUGGGCGACAGAGCGAGACUCUGUCUAAAAAAUAAAGUUCAGUGAGUCAAGUGGGCCCAUUUCACCUAAAAAAAUAUAUAUGUAAUAUAUGUAAAAUAUAUAACGUGCAUCAUUACAUGUAAUAUAUCAAAUAAUUCAGUUUCUCCUGGUAGUCUAAAUUUGUGGUUUAACAGUUCCACUAGUAUUUCAAUUAACUAUUAUUUCCUCACACUAAGUUCCCAAGUAUGCAUAGACAUAGGAACCUUGUGAUUCAAAAUUUUGGUUUUAAUUGUAAAAACAGGUCUUGGCUGCAAAGAGAAUAAAAAAGCCAUGCCAAAAAAAAAAAAAAAAAAAAAAAAAAAAGGGCCCUGAGCUUACCCUGGCUUGGGAGGCUGCCCAAAUAAAAAAAAAAAAAAAAAAAAAAAAAAGCCAUGCCUAAAUUAUACCCAAAAUAUGGUAGUAAACAUCCUCUCAGGCCUACCUAAUUAUGUGAUCAAGUGUAUUUAAUUAUGAUUAUUAAUAGCUUAGGGAUCCUCAUUAGUCAUCUCACUGCCUGGAUAAUCAGUGCUAUUACACCCCAAACUACAGGCAGAGGAACUACAAGUGUCCUUUUUUGAGACAGUCUCACUCUGUCGCUCAGGCUGGAGUGCAGUGGCAUGAUCUUGGCUUACUGCAAUCUCUACCUCCCCAGUUCAAGCAAUUCUCCUGCCUCAGCCUCCCGAGUAGCUGGGACUGCAGGCGCGUACCACCAUGCCCGGCUAAUUUUUGUAUUUUUAGUAGAAACAGGGUUUCCCCAUGUUGGCCAGGCUGGUCUUGAACUCCUGACCUCAUGAUCCACCCACCUUGGCCUCCCAAAGUGCUGGGAUUACAGGCAUGAGCCGCCGCGCCUGGCCCCAAGUGUUUUACUUCUGUGGCCUCAAUUGCUUAGUAAAAGUCGUCAGCACUGUGCUCAGCACUGUGAAAAGUUUAAGCUAAGAAGACACUCAGGUUGGUUACAGUUACAUAAUUUCGGAAAAAAAAAAAUAGGACAAAGAAUAAAACAUGAGCCAUGUAAAGAAAGUACCUUCUCCAGAAAGGAUACAACUUUGUUCUUAGUUUCUUCAGAACUGAGACACUGUGGAACUAUCUCUUCAUGAUUUGUUCCCUAUUAAAAAAUUGAUGAACAAGACCAAUUUUAACAUUUCAACAACUUGCAAAGACAAAUAGAUGAGUUUUAUGAGCUACCUUAACCAAAAAUUCAUUUUAAGUAAGAGUCCCAGAGGAUCCUCAAAGGUGAUAAACUCAUGAUUCCUUCAGGGUCCCUAAGGAUAAUACAAAAUUAACUUCUGUACAAGUGUUGUAAGCUUUAAUUACUUCUGCUGGGUCAUACUAAUGCUUCUGGACUCCCUUAUGAUCAUAGGCAUGACUAUACAGCAAAUGCAGUAAGAGUAAAGGAGCAACCCAUCUUACAGGUUUAGGUUCAUCAGCCUAACCCUUAUGACUGAUAGCACAAAAUGAAAUGUAUUAUCAUUUGACCCAAAAAUACUAUCUGCUGGAAGACUGUGUCUGUGUCUGUCUGUAUCAGUAGGCCUGCUGUGUAUGCCUGUUCUGGUCCUUGUUUAUUCAGAGGACCUUACGAAAUUCACUUCAUUUAUCUAAGCCUCAUUUUGAGAAGCUGUAAAAGAGAUAACGAGUAAUGUACCCUUCAGACAAUUUUCCGAUUGCAAUACAGAAGCAGUUCAAUAAAUGUUUUGGGAUUGUUCUGGAAUAUUUGAAAUAUUAAAAUGGUUUGAAAGUCA',
                            'CAAAUAGCAACAUGUUAGCACUCUA',
                            org_name='Human.model'))

