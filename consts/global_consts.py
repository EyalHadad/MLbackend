from pathlib import Path
from duplex.ViennaDuplex import ViennaDuplex


ROOT_PATH = Path("/sise/home/efrco/efrco-master/")
log_file = ROOT_PATH / "pipeline_log.log"
BIOMART_PATH = Path("/sise/vaksler-group/IsanaRNA/miRNA_target_rules/benorgi/pipeline/data/biomart/")
DATA_PATH = Path("/sise/vaksler-group/IsanaRNA/miRNA_target_rules/benorgi/pipeline/")
POSITIVE_PATH_DATA = Path("/sise/vaksler-group/IsanaRNA/miRNA_target_rules/benorgi/pipeline/data/pipeline_steps/features/")
MERGE_DATA = ROOT_PATH / "data/positive_interactions/"
NEGATIVE_DATA_PATH = Path("/sise/home/efrco/efrco-master/data/negative_interactions/")
DATA_PATH_INTERACTIONS = Path("/sise/home/efrco/efrco-master/data/")
GENERATE_DATA_PATH= ROOT_PATH / "generate_interactions/"
CLIP_PATH_DATA = Path("/sise/vaksler-group/IsanaRNA/miRNA_target_rules/Isana/")
POSITIVE_PATH_FEATUERS = ROOT_PATH / "data/positive_interactions/positive_interactions_new/featuers_step/"


SITE_EXTRA_CHARS: int = 3
HUMAN_SITE_EXTENDED_LEN: int = 25
MINIMAL_BLAST_COVERAGE = 95
MINIMAL_BLAST_IDENTITY = 95
MINIMAL_LENGTH_TO_BLAST = 10
DUPLEX_DICT = {"ViennaDuplex": ViennaDuplex}

CONFIG = {
    'minimum_pairs_for_interaction': 11,
    'duplex_method' :  ["vienna"],
    'max_process' : 1
 #   'duplex_method': ["vienna", "miranda", "vienna_with_constraint"]

    #'duplex_method' :  ["miranda"]
}

list_of_features_for_web = ['Acc_P11_7th',
'Acc_P30_2th',
'MRNA_Target_GG_comp',
'HotPairingMRNA_he_P5_L3',
'Acc_P9_9th',
'Acc_P5_10th',
'Acc_P12_4th',
'Acc_P21_5th',
'Acc_P26_4th',
'MRNA_Down_CU_comp',
'HotPairingMirna_he_P8_L4',
'Acc_P31_3th',
'MRNA_Up_C_comp',
'Acc_P13_2th',
'MRNA_Target_UG_comp',
'Acc_P21_6th',
'Acc_P14_8th',
'MRNA_Down_GC_comp',
'Acc_P10_5th',
'MRNA_Target_GC_comp',
'HotPairingMRNA_he_P9_L3',
'Acc_P20_2th',
'Acc_P27_7th',
'HotPairingMirna_he_P5_L5',
'Acc_P25_4th',
'HotPairingMirna_he_P8_L1',
'HotPairingMRNA_he_P9_L5',
'Acc_P4_1th',
'Acc_P31_5th',
'Acc_P37_9th',
'HotPairingMirna_he_P1_L5',
'Acc_P16_3th',
'HotPairingMirna_he_P1_L4',
'Acc_P19_2th',
'Acc_P30_3th',
'Acc_P35_7th',
'Acc_P11_2th',
'Acc_P10_2th',
'Acc_P14_2th',
'Acc_P18_10th',
'Acc_P31_7th',
'HotPairingMirna_he_P1_L3',
'miRNAPairingCount_Seed_GC',
'Seed_match_A',
'Acc_P26_1th',
'Seed_match_GU_2_7',
'Acc_P9_5th',
'Acc_P24_7th',
'Acc_P35_6th',
'Acc_P3_3th',
'miRNAPairingCount_Total_mir_bulge',
'miRNAPairingCount_X3p_GU',
'Acc_P2_6th',
'Acc_P8_8th',
'HotPairingMRNA_he_P4_L5',
'Acc_P26_10th',
'Acc_P3_2th',
'MRNA_Up_UA_comp',
'Seed_match_GU_all',
'HotPairingMirna_he_P3_L4',
'Acc_P7_4th',
'Acc_P12_8th',
'Acc_P20_9th',
'Acc_P19_3th',
'Acc_P10_8th',
'Acc_P23_9th',
'Acc_P9_2th',
'HotPairingMirna_he_P6_L3',
'MRNA_Up_AA_comp',
'HotPairingMRNA_he_P4_L4',
'Acc_P17_5th',
'Acc_P17_2th',
'Acc_P3_6th',
'HotPairingMirna_he_P2_L4',
'Acc_P24_8th',
'Acc_P37_1th',
'miRNAPairingCount_Seed_AU',
'HotPairingMRNA_he_P3_L3',
'Acc_P1_7th',
'Acc_P5_2th',
'Acc_P2_8th',
'Acc_P12_7th',
'Acc_P29_10th',
'Acc_P8_5th',
'HotPairingMRNA_he_P7_L5',
'Acc_P34_5th',
'Acc_P25_3th',
'Acc_P25_10th',
'Acc_P5_8th',
'Acc_P33_4th',
'Acc_P26_3th',
'Acc_P24_1th',
'Acc_P31_2th',
'Acc_P17_3th',
'Acc_P15_4th',
'Acc_P24_6th',
'Acc_P27_3th',
'HotPairingMirna_he_P4_L5',
'Acc_P13_10th',
'Acc_P17_4th',
'Acc_P36_1th',
'Acc_P32_4th',
'Acc_P33_3th',
'Acc_P15_6th',
'Acc_P6_10th',
'Acc_P35_8th',
'Acc_P17_7th',
'Energy_MEF_cons_local_target_normalized',
'Acc_P6_7th',
'Acc_P36_5th',
'miRNAPairingCount_Total_bulge_mir_nt',
'HotPairingMirna_he_P9_L1',
'Acc_P22_5th',
'Acc_P35_1th',
'Acc_P27_6th',
'Acc_P7_8th',
'Acc_P15_9th',
'Acc_P28_6th',
'miRNAPairingCount_Seed_target_bulge',
'MRNA_Up_CG_comp',
'MRNA_Down_UU_comp',
'Acc_P5_3th',
'Acc_P31_1th',
'Acc_P1_3th',
'Acc_P9_4th',
'Acc_P21_10th',
'Acc_P18_1th',
'HotPairingMirna_he_P9_L5',
'miRNAPairingCount_Seed_mir_bulge',
'MRNA_Target_C_comp',
'Acc_P15_8th',
'HotPairingMirna_he_P6_L4',
'Acc_P14_10th',
'Acc_P15_2th',
'Acc_P18_2th',
'Acc_P8_6th',
'MRNA_Target_AG_comp',
'Acc_P23_2th',
'Acc_P37_8th',
'Acc_P28_9th',
'Acc_P3_1th',
'Acc_P32_3th',
'HotPairingMirna_he_P5_L3',
'HotPairingMirna_he_P7_L5',
'Acc_P9_10th',
'Acc_P32_5th',
'Acc_P3_4th',
'Acc_P21_4th',
'HotPairingMirna_he_P7_L2',
'HotPairingMRNA_he_P8_L4',
'HotPairingMRNA_he_P4_L3',
'miRNAPairingCount_X3p_bulge_target_nt',
'MRNA_Target_AC_comp',
'Acc_P21_2th',
'miRNAPairingCount_X3p_target_bulge',
'HotPairingMirna_he_P3_L1',
'Acc_P3_7th',
'Acc_P19_7th',
'Acc_P32_9th',
'MRNA_Target_CA_comp',
'Acc_P2_7th',
'Acc_P3_10th',
'Acc_P32_10th',
'Acc_P1_4th',
'Acc_P3_8th',
'MRNA_Target_U_comp',
'miRNAPairingCount_Seed_bulge_nt',
'Acc_P1_9th',
'MRNA_Target_AU_comp',
'Seed_match_GU_3_8',
'HotPairingMirna_he_P7_L4',
'Acc_P10_3th',
'Acc_P12_3th',
'Seed_match_interactions_2_7',
'Energy_MEF_3p',
'Acc_P37_7th',
'Acc_P23_8th',
'HotPairingMirna_he_P2_L5',
'Acc_P34_1th',
'HotPairingMirna_he_P3_L5',
'Acc_P3_5th',
'HotPairingMRNA_he_P1_L3',
'Acc_P19_9th',
'Acc_P25_6th',
'Acc_P32_2th',
'MRNA_Target_UU_comp',
'HotPairingMirna_he_P9_L4',
'Acc_P5_5th',
'Seed_match_start',
'Acc_P18_6th',
'Acc_P4_8th',
'Acc_P20_8th',
'HotPairingMRNA_he_P8_L3',
'Acc_P29_6th',
'miRNAPairingCount_Total_GU',
'MRNA_Up_GG_comp',
'Acc_P29_3th',
'Acc_P37_6th',
'Acc_P1_10th',
'Acc_P29_7th',
'Seed_match_bulge_mirna',
'Acc_P23_6th',
'MRNA_Down_AA_comp',
'Acc_P28_7th',
'Acc_P30_1th',
'Acc_P19_1th',
'miRNAPairingCount_Total_GC',
'HotPairingMirna_he_P5_L2',
'MRNA_Down_UG_comp',
'Acc_P12_10th',
'miRNAPairingCount_Total_target_bulge',
'Acc_P17_9th',
'Acc_P2_1th',
'MRNA_Up_GU_comp',
'MRNA_Target_GU_comp',
'Acc_P16_10th',
'MRNA_Up_CC_comp',
'Acc_P37_5th',
'Acc_P32_6th',
'Acc_P4_3th',
'Acc_P7_6th',
'Acc_P13_1th',
'Acc_P23_1th',
'Acc_P15_3th',
'HotPairingMRNA_he_P7_L2',
'Acc_P6_1th',
'MRNA_Dist_to_end',
'Acc_P34_10th',
'MRNA_Up_G_comp',
'HotPairingMirna_he_P5_L1',
'MRNA_Down_A_comp',
'Acc_P27_8th',
'MRNA_Up_CU_comp',
'Acc_P11_4th',
'Acc_P29_1th',
'Acc_P9_7th',
'Acc_P22_2th',
'Acc_P20_7th',
'MRNA_Down_G_comp',
'HotPairingMirna_he_P2_L1',
'Energy_MEF_local_target',
'miRNAPairingCount_X3p_bulge_mir_nt',
'Acc_P7_7th',
'HotPairingMRNA_he_P5_L1',
'Acc_P13_5th',
'Acc_P17_10th',
'HotPairingMirna_he_P1_L2',
'MRNA_Down_GU_comp',
'Acc_P4_9th',
'Seed_match_mismatch_left',
'HotPairingMRNA_he_P1_L1',
'Acc_P33_5th',
'Acc_P4_7th',
'Acc_P33_10th',
'Acc_P24_9th',
'Acc_P7_5th',
'Acc_P28_2th',
'HotPairingMirna_he_P1_L1',
'Acc_P35_9th',
'Acc_P27_5th',
'Acc_P37_2th',
'HotPairingMirna_he_P3_L3',
'Acc_P21_9th',
'Acc_P8_2th',
'Acc_P20_4th',
'MRNA_Down_AG_comp',
'Acc_P36_10th',
'Acc_P15_7th',
'Acc_P35_4th',
'Acc_P22_6th',
'MRNA_Up_AU_comp',
'HotPairingMRNA_he_P7_L4',
'Acc_P36_9th',
'Acc_P21_8th',
'Acc_P16_8th',
'Acc_P13_3th',
'Acc_P2_4th',
'Acc_P13_6th',
'Acc_P35_5th',
'Acc_P5_9th',
'Acc_P25_5th',
'Acc_P33_6th',
'Acc_P11_1th',
'Acc_P33_8th',
'Acc_P24_2th',
'Acc_P28_1th',
'Acc_P33_2th',
'Acc_P16_9th',
'Acc_P26_5th',
'Acc_P33_1th',
'Acc_P28_8th',
'MRNA_Up_CA_comp',
'Acc_P11_9th',
'Acc_P23_3th',
'Acc_P7_10th',
'Acc_P18_4th',
'Acc_P18_3th',
'Acc_P16_4th',
'MRNA_Up_UU_comp',
'Acc_P36_3th',
'Acc_P19_8th',
'Acc_P31_8th',
'Acc_P11_6th',
'Acc_P9_6th',
'Acc_P16_6th',
'Acc_P35_10th',
'Acc_P31_4th',
'Acc_P12_6th',
'MRNA_Target_CC_comp',
'Acc_P18_5th',
'Acc_P26_8th',
'Acc_P36_2th',
'MRNA_Down_U_comp',
'HotPairingMRNA_he_P5_L5',
'MRNA_Down_CA_comp',
'Acc_P19_10th',
'HotPairingMRNA_he_P1_L5',
'MRNA_Target_UA_comp',
'Acc_P31_9th',
'HotPairingMRNA_he_P9_L2',
'MRNA_Up_GA_comp',
'HotPairingMirna_he_P8_L3',
'HotPairingMRNA_he_P2_L4',
'Acc_P14_9th',
'Acc_P7_9th',
'Acc_P13_7th',
'Acc_P30_4th',
'Seed_match_mismatch_right',
'MRNA_Up_GC_comp',
'Acc_P4_5th',
'Seed_match_interactions_all',
'HotPairingMRNA_he_P6_L4',
'Acc_P33_9th',
'MRNA_Down_GA_comp',
'miRNAPairingCount_Total_AU',
'Acc_P1_6th',
'Acc_P22_9th',
'MRNA_Target_CG_comp',
'HotPairingMRNA_he_P4_L2',
'Acc_P10_1th',
'miRNAPairingCount_Total_bulge_target_nt',
'Acc_P26_7th',
'Seed_match_bulge_target',
'HotPairingMRNA_he_P9_L4',
'end',
'Acc_P5_7th',
'miRNAPairingCount_X3p_bulge_nt',
'MRNA_Target_CU_comp',
'Acc_P34_4th',
'Acc_P11_8th',
'Acc_P24_10th',
'Acc_P20_6th',
'Acc_P8_4th',
'Acc_P14_4th',
'Acc_P10_6th',
'Acc_P34_7th',
'Acc_P8_3th',
'Acc_P11_3th',
'Acc_P26_6th',
'HotPairingMirna_he_P3_L2',
'Acc_P5_6th',
'miRNAPairingCount_X3p_mismatch',
'HotPairingMirna_he_P9_L3',
'Acc_P7_2th',
'MRNA_Up_UG_comp',
'HotPairingMirna_he_P2_L2',
'miRNAPairingCount_Seed_GU',
'Acc_P30_6th',
'Acc_P29_4th',
'HotPairingMirna_he_P5_L4',
'Acc_P29_2th',
'MRNA_Target_G_comp',
'Acc_P25_8th',
'miRNAPairingCount_X3p_AU',
'Acc_P27_2th',
'Acc_P2_5th',
'HotPairingMRNA_he_P9_L1',
'Acc_P20_3th',
'HotPairingMRNA_he_P3_L4',
'HotPairingMRNA_he_P3_L5',
'HotPairingMRNA_he_P2_L5',
'HotPairingMirna_he_P6_L1',
'Acc_P26_9th',
'Acc_P21_1th',
'Acc_P25_7th',
'MRNA_Target_A_comp',
'Acc_P19_4th',
'Acc_P29_5th',
'Acc_P9_8th',
'Acc_P14_7th',
'Energy_MEF_local_target_normalized',
'MRNA_Up_U_comp',
'MRNA_Target_AA_comp',
'Acc_P20_1th',
'HotPairingMRNA_he_P8_L1',
'Acc_P14_1th',
'Acc_P22_8th',
'Acc_P4_10th',
'Acc_P27_9th',
'Acc_P31_10th',
'HotPairingMRNA_he_P5_L2',
'Acc_P17_1th',
'Acc_P9_3th',
'Acc_P36_6th',
'Acc_P34_8th',
'MRNA_Up_A_comp',
'MRNA_Down_C_comp',
'Acc_P22_4th',
'MRNA_Down_CG_comp',
'Acc_P30_10th',
'HotPairingMRNA_he_P1_L2',
'Acc_P18_8th',
'miRNAPairingCount_Seed_mismatch',
'Acc_P6_6th',
'Acc_P17_6th',
'Acc_P6_8th',
'Acc_P9_1th',
'HotPairingMirna_he_P8_L5',
'miRNAPairingCount_Total_mismatch',
'Acc_P27_4th',
'Acc_P20_10th',
'Acc_P23_7th',
'Acc_P34_6th',
'Acc_P8_10th',
'Acc_P3_9th',
'Acc_P1_1th',
'Acc_P8_9th',
'Energy_MEF_cons_local_target',
'Acc_P30_5th',
'HotPairingMRNA_he_P5_L4',
'Acc_P25_1th',
'HotPairingMRNA_he_P4_L1',
'miRNAPairingCount_Total_bulge_nt',
'Acc_P1_2th',
'Acc_P6_2th',
'HotPairingMirna_he_P9_L2',
'Acc_P35_3th',
'Acc_P2_3th',
'Acc_P18_7th',
'Acc_P30_8th',
'Acc_P37_10th',
'Acc_P26_2th',
'Acc_P15_1th',
'start',
'Acc_P34_9th',
'HotPairingMRNA_he_P3_L2',
'Acc_P20_5th',
'Acc_P28_10th',
'Acc_P24_3th',
'HotPairingMRNA_he_P6_L5',
'Acc_P35_2th',
'Acc_P30_9th',
'Acc_P32_7th',
'Acc_P13_8th',
'miRNAPairingCount_Seed_bulge_target_nt',
'miRNAPairingCount_X3p_GC',
'Acc_P37_4th',
'Acc_P31_6th',
'Acc_P4_4th',
'Acc_P34_3th',
'HotPairingMRNA_he_P6_L2',
'Acc_P23_10th',
'Acc_P32_8th',
'HotPairingMirna_he_P4_L1',
'Acc_P22_1th',
'HotPairingMirna_he_P2_L3',
'MRNA_Down_AC_comp',
'Acc_P27_10th',
'Acc_P21_7th',
'Acc_P23_5th',
'Acc_P22_7th',
'Acc_P10_10th',
'Acc_P7_1th',
'Energy_MEF_Duplex',
'HotPairingMRNA_he_P3_L1',
'Acc_P1_8th',
'Acc_P12_5th',
'Acc_P22_3th',
'MRNA_Down_AU_comp',
'MRNA_Up_UC_comp',
'Acc_P25_2th',
'Acc_P28_4th',
'MRNA_Dist_to_start',
'Acc_P6_9th',
'Acc_P12_2th',
'Acc_P10_4th',
'Acc_P25_9th',
'Acc_P7_3th',
'Acc_P33_7th',
'HotPairingMRNA_he_P1_L4',
'HotPairingMRNA_he_P7_L1',
'Acc_P4_6th',
'Acc_P34_2th',
'HotPairingMRNA_he_P7_L3',
'Seed_match_mismatch_inner',
'MRNA_Down_CC_comp',
'MRNA_Target_GA_comp',
'Acc_P12_1th',
'Acc_P19_5th',
'Acc_P22_10th',
'Acc_P29_9th',
'Acc_P2_9th',
'HotPairingMRNA_he_P6_L3',
'HotPairingMRNA_he_P2_L2',
'Acc_P10_9th',
'Acc_P32_1th',
'Acc_P27_1th',
'HotPairingMirna_he_P4_L4',
'Acc_P30_7th',
'Acc_P6_5th',
'HotPairingMRNA_he_P2_L3',
'Acc_P6_3th',
'Acc_P15_10th',
'MRNA_Up_AG_comp',
'Acc_P24_5th',
'Acc_P14_6th',
'Acc_P21_3th',
'MRNA_Target_UC_comp',
'HotPairingMirna_he_P8_L2',
'Acc_P16_5th',
'Acc_P12_9th',
'Acc_P17_8th',
'Acc_P5_4th',
'MRNA_Down_UC_comp',
'Acc_P16_2th',
'HotPairingMirna_he_P6_L2',
'HotPairingMirna_he_P7_L1',
'Acc_P13_4th',
'HotPairingMirna_he_P4_L3',
'miRNAPairingCount_Total_basepair',
'Acc_P14_3th',
'Acc_P14_5th',
'HotPairingMirna_he_P4_L2',
'Acc_P16_1th',
'Acc_P16_7th',
'Acc_P15_5th',
'HotPairingMirna_he_P6_L5',
'miRNAPairingCount_Seed_bulge_mir_nt',
'Acc_P2_2th',
'Seed_match_interactions_3_8',
'HotPairingMirna_he_P7_L3',
'Acc_P19_6th',
'Acc_P29_8th',
'MRNA_Up_AC_comp',
'Energy_MEF_Seed',
'Acc_P11_5th',
'HotPairingMRNA_he_P2_L1',
'Acc_P18_9th',
'Acc_P13_9th',
'Acc_P11_10th',
'Acc_P8_1th',
'Acc_P36_4th',
'Acc_P36_8th',
'Acc_P4_2th',
'Acc_P28_5th',
'Acc_P36_7th',
'HotPairingMRNA_he_P6_L1',
'Acc_P5_1th',
'Acc_P6_4th',
'Acc_P2_10th',
'MRNA_Down_UA_comp',
'Acc_P1_5th',
'Acc_P10_7th',
'HotPairingMRNA_he_P8_L5',
'Acc_P24_4th',
'Acc_P37_3th',
'HotPairingMRNA_he_P8_L2',
'Acc_P28_3th',
'Acc_P23_4th',
'miRNAPairingCount_X3p_mir_bulge',
'MRNA_Down_GG_comp',
'Acc_P8_7th',]