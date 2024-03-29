from dal.db_connection import DataSet, db, executor, cache
from dal.db_connection import SeedFamilyOption, SiteOption, GeneIdOption, RegionOption, mirnaIdOption
from dal.db_connection import Interaction
from dal.interactions import create_interactions_list
from configurator import Configurator
import os
import json


@cache.memoize()
def get_organisms_details_with_features(with_options=False):
    path = Configurator().get_path_prefix_of_organism_details_location()
    if not any(os.listdir(path)) or not with_options:
        orgs = get_organisms(with_options=with_options)
        features = get_features_details()
        features_types = Configurator().get_features_types()
        res = {"organisms": orgs, "features": features, "featureTypes": features_types}
        if with_options:
            save_response_to_folder(res, path, "org_details.json")
        return res
    else:
        res = read_json_file(path + "\\org_details.json")
        return res


@cache.memoize(timeout=12000)
def get_organisms(with_options=False):
    data_sets_dict = get_data_sets(with_options)
    organisms_dict = {}
    for data_set in data_sets_dict.values():
        if data_set["organism"].id not in organisms_dict:
            organisms_dict[data_set["organism"].id] = {"id": data_set["organism"].id,
                                                    "name": data_set["organism"].name,
                                                    "datasets": []}
        organisms_dict[data_set["organism"].id]["datasets"].append(data_set)
        data_set.pop("organism")
    organisms_list = list(organisms_dict.values())
    return organisms_list

def get_data_sets(with_options=False):
    if with_options:
        search_options_dict = get_search_options()
    data_sets = db.session.query(DataSet)
    data_sets_dict = {}
    for data_set in data_sets:
        data_sets_dict[data_set.id] = { "id": data_set.id,
                                        "name": data_set.name,
                                        "interactionsAmount": data_set.interactions_amount,
                                        "datasetMB": data_set.data_set_mb,
                                        "searchOptions": {"seedFamilies": [], "miRnaIds": [], "siteTypes": ["canonical", "noncanonical", "other"],
                                                          "geneIds": [], "regions": []},
                                        "organism" : data_set.organism}
    if with_options:
        for op_name, options_of_data_sets_dict in search_options_dict.items():
            for data_set_id, options_list in options_of_data_sets_dict.items():
                if data_set_id in data_sets_dict:
                    data_sets_dict[data_set_id]["searchOptions"][op_name] = options_list
    return data_sets_dict

def get_search_options():
    """ This function create workers and get all search option for all datasets in parallel working.
    each worker get_search_option use function.
    Returns:
        list of tuples that returnd from each worker.
    """
    options_details_dict = {"seedFamilies":[SeedFamilyOption, "seed_family"], "miRnaIds": [mirnaIdOption, "mirna_id"],
                             "geneIds":[GeneIdOption, "Gene_ID"],  "regions": [RegionOption, "region"]}
    workers = []
    for op_name, op_details in options_details_dict.items():
        workers.append(executor.submit(get_search_option, op_name, op_details[0], op_details[1]))
    return dict([w.result() for w in workers])


def get_search_option(op_name: str, option, column_name: str):
    """This function takes three arguments: op_name, option and column_name. It extract the
    distincted values of column_name in mirna_mrna_interaction table (all values of the options ORM object).
    
    Args:
        op_name (str): The option name as need to return in the response.
                       E.g. -> "seedFamilies"
        option (db.Model): The appropriate class of the search option.
                           E.g. -> SeedFamilyOption
        column_name (str): The column name of the appropriate option as called in db.
                           E.g. -> "seed_family" 
        
    Returns:
        tuple of (op_name, dictionary).
        The dictionary is pairs of dataset id and distincted values  list of the appropriate search option.
        E.g. -> ("regions", {2 : ["3utr", "5utr", "coding", "lncRNA"]})
    """
    res = {}
    print(f'---start extraction of {op_name}')
    try:
        data = db.session.query(option).all()
        for d in data:
            op_value = getattr(d, column_name)
            if op_value is None or op_value == "" or op_value == "None":
                continue
            if d.data_set_id not in res:
                res[d.data_set_id] = []
            res[d.data_set_id].append(op_value)
        print(f'---end extraction of {op_name}')
    except Exception as e:
        print(f'---extraction failed- {op_name}. error: {str(e)}')
    return (op_name, res)

@cache.memoize(timeout=12000)
def get_data_set_interactions(data_set_id):
    interactions = []
    try:
        results = Interaction.query.filter_by(data_set_id=data_set_id).order_by(Interaction.index).limit(750).all()
        interactions = create_interactions_list(results)
    except Exception as e:
        print(f'dal failed to get interactions of data set id- {data_set_id}. error: {str(e)}')
    return interactions


def get_features_details():
    features_details = Configurator().get_statistic_features_details()
    return features_details


def save_response_to_folder(response, folder_path, file_name):
    # Serialize the response to a JSON string
    json_string = json.dumps(response, indent=4)

    # Check if the folder exists, if not, create it
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Combine folder path with file name
    file_path = os.path.join(folder_path, file_name)

    # Write the JSON string to the file
    with open(file_path, 'w') as file:
        file.write(json_string)


def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"File not found at path: {file_path}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in file: {file_path}")
        print(f"Error message: {str(e)}")
        return None

