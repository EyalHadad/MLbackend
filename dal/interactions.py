from dal.db_connection import db, cache
from dal.db_connection import Interaction, DataSet
from sqlalchemy import or_, and_
from configurator import Configurator


def get_interactions_query(all_rows, data_sets_ids, seed_families, mirna_ids,
                     mirna_seqs, site_types, gene_ids, regions):
    results = []
    try:
        filters = [Interaction.data_set_id.in_(data_sets_ids) if data_sets_ids else True,
                  Interaction.seed_family.in_(seed_families) if seed_families else True,
                  Interaction.mirna_id.in_(mirna_ids) if mirna_ids else True,
                  Interaction.mirna_sequence.in_(mirna_seqs) if mirna_seqs else True,
                  Interaction.Gene_ID.in_(gene_ids) if gene_ids else True,
                  Interaction.region.in_(regions) if regions else True]
        site_types_filters = None
        if site_types:
            site_types_filters = []
            if 'canonical' in site_types:
                site_types_filters.append(Interaction.Seed_match_canonical == True)
            if 'noncanonical' in site_types:
                site_types_filters.append(Interaction.Seed_match_noncanonical == True)
            if 'other' in site_types:
                site_types_filters.append(and_(
                    Interaction.Seed_match_canonical == False,
                    Interaction.Seed_match_noncanonical == False
                ))
            filters.append(or_(*site_types_filters))
        if all_rows:
            results = Interaction.query.filter(*filters).all()
        else:
            results = Interaction.query.filter(*filters).order_by(Interaction.index).limit(750).all()
        return results
    except Exception as e:
        print(f'dal failed to get interactions. error: {str(e)}')

    
def get_interactions_general_search_query(all_rows, query_string):
    interactions = []
    if query_string is None or query_string == '':
        return interactions
    try:
        if all_rows:
            interactions = db.session.query(Interaction).filter(or_(
                Interaction.mirna_id.like(f'%{query_string}%'),
                Interaction.mirna_sequence.like(f'%{query_string}%'),
                Interaction.seed_family.like(f'%{query_string}%'),
                Interaction.site.like(f'%{query_string}%'),
                Interaction.region.like(f'%{query_string}%'),
                Interaction.mrna_bulge.like(f'%{query_string}%'),
                Interaction.mrna_inter.like(f'%{query_string}%'),
                Interaction.mir_inter.like(f'%{query_string}%'),
                Interaction.mir_bulge.like(f'%{query_string}%'),
                Interaction.Gene_ID.like(f'%{query_string}%')
            )).order_by(Interaction.index).all()
        else:
            interactions = db.session.query(Interaction).filter(or_(
            Interaction.mirna_id.like(f'%{query_string}%'),
            Interaction.mirna_sequence.like(f'%{query_string}%'),
            Interaction.seed_family.like(f'%{query_string}%'),
            Interaction.site.like(f'%{query_string}%'),
            Interaction.region.like(f'%{query_string}%'),
            Interaction.mrna_bulge.like(f'%{query_string}%'),
            Interaction.mrna_inter.like(f'%{query_string}%'),
            Interaction.mir_inter.like(f'%{query_string}%'),
            Interaction.mir_bulge.like(f'%{query_string}%'),
            Interaction.Gene_ID.like(f'%{query_string}%')
        )).order_by(Interaction.index).limit(750).all()
        return interactions
    except Exception as e:
        print(f'dal failed to get general interactions. error: {str(e)}')


@cache.memoize(timeout=12000)
def get_interactions(data_sets_ids, seed_families, mirna_ids,
                     mirna_seqs, site_types, gene_ids, regions):
    interactions = []
    try:
        results = get_interactions_query(False, data_sets_ids, seed_families, mirna_ids,
                     mirna_seqs, site_types, gene_ids, regions)
        interactions = create_interactions_list(results)
    except Exception as e:
        print(f'dal failed to get interactions. error: {str(e)}')
    return interactions


@cache.memoize(timeout=12000)
def get_interactions_general_search(query_string):
    interactions = []
    if query_string is None or query_string == '':
        return interactions
    try:
        results = get_interactions_general_search_query(False, query_string)
        interactions = create_interactions_list(results)
    except Exception as e:
        print(f'dal failed to get general interactions. error: {str(e)}')
    return interactions


def create_interactions_list(results):
    interactions = []
    for interaction in results:
            interactions.append({"interactionId": interaction.id,
                                "index": interaction.index,
                                "datasetId": interaction.data_set_id,
                                "miRnaId": interaction.mirna_id,
                                "miRnaSeq": interaction.mirna_sequence,
                                "seedFamily": interaction.seed_family,
                                "site": interaction.site,
                                "region": interaction.region,
                                "start": interaction.start,
                                "end": interaction.end,
                                "mrnaBulge": interaction.mrna_bulge,
                                "mrnaInter": interaction.mrna_inter,
                                "mirInter": interaction.mir_inter,
                                "mirBulge": interaction.mir_bulge,
                                "energyMefDuplex": interaction.Energy_MEF_Duplex,
                                "geneId": interaction.Gene_ID
                            })
    return interactions


@cache.memoize(timeout=12000)
def get_interaction_id_data(interaction_id):
    interaction_id_data = {}
    try:
        results = Interaction.query.filter_by(id=interaction_id)
        interaction_id_data = create_interaction_outer_data_object(results[0])
    except Exception as e:
        print(f'dal failed to get general interactions. error: {str(e)}')
    return interaction_id_data


def create_interaction_outer_data_object(interaction_id_data):
    mi_rna_data_dict = {
            "miRnaId": interaction_id_data.mirna_id,
            "miRnaSequence": interaction_id_data.mirna_sequence,
            "seedFamily": interaction_id_data.seed_family
        }
    sequence_url = create_sequence_url(interaction_id_data.Gene_ID, interaction_id_data.organism)
    m_rna_data_dict = {
            "region": interaction_id_data.region,
            "geneId": interaction_id_data.Gene_ID,
            "geneName": interaction_id_data.Gene_name,
            "sequenceUrl": sequence_url,
            "interStart": interaction_id_data.start,
            "interEnd": interaction_id_data.end,
            "site": interaction_id_data.site
        }
    
    duplex_structure = create_duplex_structure(interaction_id_data.mrna_bulge,
                                               interaction_id_data.mrna_inter,
                                               interaction_id_data.mir_inter,
                                               interaction_id_data.mir_bulge)
    site_type = "other"
    if interaction_id_data.Seed_match_noncanonical:
        site_type = "noncanonical"
    elif interaction_id_data.Seed_match_canonical:
        site_type = "canonical"
    data_set_id = interaction_id_data.data_set_id
    dataset = DataSet.query.filter_by(id=data_set_id)
    dataset_name = dataset[0].name
    interaction_inner_data_dict = {
            "interactionId": interaction_id_data.id,
            "organismName": interaction_id_data.organism,
            "dataSetName": dataset_name,
            "duplexStructure": duplex_structure,
            "energyMefDuplex": interaction_id_data.Energy_MEF_Duplex,
            "mRnaDistToEnd": interaction_id_data.MRNA_Dist_to_end,
            "mRnaDistToStart": interaction_id_data.MRNA_Dist_to_start,
            "seedMatchStart": interaction_id_data.Seed_match_start,
            "siteType": site_type
        }
    
    interaction_outer_data_object = {
        "miRnaData": mi_rna_data_dict,
        "mRnaData": m_rna_data_dict,
        "interactionInnerData": interaction_inner_data_dict
        }
    return interaction_outer_data_object


def create_duplex_structure(mrna_bulge, mrna_inter, mir_inter, mir_bulge):
    mrna_bulge_prefix = "mRNA  3’ "
    mrna_bulge_sufix = " 5’"
    mrna_inter_prefix = "         "
    mrna_inter_sufix = "   "
    mir_inter_prefix = "         "
    mir_inter_sufix = "   "
    mir_bulge_prefix = "miRNA 5’ "
    mir_bulge_sufix = " 3’"
    return f'{mrna_bulge_prefix}{mrna_bulge}{mrna_bulge_sufix}\n{mrna_inter_prefix}{mrna_inter}{mrna_inter_sufix}\n{mir_inter_prefix}{mir_inter}{mir_inter_sufix}\n{mir_bulge_prefix}{mir_bulge}{mir_bulge_sufix}'


def create_sequence_url(gene_id, organism):
    confg = Configurator()
    relevant_gene_id = gene_id.split('|')[0]
    ensamble_org_name = confg.get_ensamble_organisms_names_dict()[organism]
    url_string = confg.get_ensambl_url().format(organism_name=ensamble_org_name, gene_id=relevant_gene_id)
    return url_string

