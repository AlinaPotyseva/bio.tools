from typing import List, Optional, Tuple, Union

AMINOACIDS_DICT = {
    'Ala': {'TO_1': 'A',
            'PROTEIN_TO_RNA_COMBINATION': {'GCU', 'GCC', 'GCA', 'GCG'},
            'PKA_AMINOACIDS': [2.34, 9.69],
            'MOLECULAR_WEIGHTS': 89},
    'Arg': {'TO_1': 'R',
            'PROTEIN_TO_RNA_COMBINATION': {'CGU', 'CGC', 'CGA', 'CGG', 'AGA',
                                           'AGG'},
            'PKA_AMINOACIDS': [2.17, 9.04, 12.68],
            'MOLECULAR_WEIGHTS': 174},
    'Asn': {'TO_1': 'N',
            'PROTEIN_TO_RNA_COMBINATION': {'AAU', 'AAC'},
            'PKA_AMINOACIDS': [1.88, 9.60, 3.65],
            'MOLECULAR_WEIGHTS': 132},
    'Asp': {'TO_1': 'D',
            'PROTEIN_TO_RNA_COMBINATION': {'GAU', 'GAC'},
            'PKA_AMINOACIDS': [1.88, 9.60, 3.65],
            'MOLECULAR_WEIGHTS': 133},
    'Cys': {'TO_1': 'C',
            'PROTEIN_TO_RNA_COMBINATION': {'UGU', 'UGC'},
            'PKA_AMINOACIDS': [1.96, 10.28, 8.18],
            'MOLECULAR_WEIGHTS': 121},
    'Glu': {'TO_1': 'Q',
            'PROTEIN_TO_RNA_COMBINATION': {'GAA', 'GAG'},
            'PKA_AMINOACIDS': [2.19, 9.67, 4.25],
            'MOLECULAR_WEIGHTS': 147},
    'Gln': {'TO_1': 'E',
            'PROTEIN_TO_RNA_COMBINATION': {'CAA', 'CAG'},
            'PKA_AMINOACIDS': [2.17, 9.13],
            'MOLECULAR_WEIGHTS': 146},
    'Gly': {'TO_1': 'G',
            'PROTEIN_TO_RNA_COMBINATION': {'GGU', 'GGC', 'GGA', 'GGG'},
            'PKA_AMINOACIDS': [2.34, 9.60],
            'MOLECULAR_WEIGHTS': 75},
    'His': {'TO_1': 'E',
            'PROTEIN_TO_RNA_COMBINATION': {'CAU', 'CAC'},
            'PKA_AMINOACIDS': [1.82, 9.17],
            'MOLECULAR_WEIGHTS': 155},
    'Ile': {'TO_1': 'I',
            'PROTEIN_TO_RNA_COMBINATION': {'AUU', 'AUC', 'AUA'},
            'PKA_AMINOACIDS': [2.36, 9.68],
            'MOLECULAR_WEIGHTS': 131},
    'Leu': {'TO_1': 'L',
            'PROTEIN_TO_RNA_COMBINATION': {'CUU', 'CUC', 'CUA', 'CUG'},
            'PKA_AMINOACIDS': [2.36, 9.60],
            'MOLECULAR_WEIGHTS': 131},
    'Lys': {'TO_1': 'K',
            'PROTEIN_TO_RNA_COMBINATION': {'AAA', 'AAG'},
            'PKA_AMINOACIDS': [2.18, 8.95, 10.53],
            'MOLECULAR_WEIGHTS': 146},
    'Met': {'TO_1': 'M',
            'PROTEIN_TO_RNA_COMBINATION': {'AUG'},
            'PKA_AMINOACIDS': [2.28, 9.21],
            'MOLECULAR_WEIGHTS': 149},
    'Phe': {'TO_1': 'F',
            'PROTEIN_TO_RNA_COMBINATION': {'UUU', 'UUC'},
            'PKA_AMINOACIDS': [2.20, 9.13],
            'MOLECULAR_WEIGHTS': 165},
    'Pro': {'TO_1': 'P',
            'PROTEIN_TO_RNA_COMBINATION': {'CCU', 'CCC', 'CCA', 'CCG'},
            'PKA_AMINOACIDS': [1.99, 10.96],
            'MOLECULAR_WEIGHTS': 115},
    'Ser': {'TO_1': 'S',
            'PROTEIN_TO_RNA_COMBINATION': {'UCU', 'UCC', 'UCA', 'UCG'},
            'PKA_AMINOACIDS': [2.21, 9.15],
            'MOLECULAR_WEIGHTS': 105},
    'Thr': {'TO_1': 'T',
            'PROTEIN_TO_RNA_COMBINATION': {'ACU', 'ACC', 'ACA', 'ACG'},
            'PKA_AMINOACIDS': [2.11, 9.62],
            'MOLECULAR_WEIGHTS': 119},
    'Tyr': {'TO_1': 'W',
            'PROTEIN_TO_RNA_COMBINATION': {'UAU', 'UAC'},
            'PKA_AMINOACIDS': [2.20, 9.11, 10.07],
            'MOLECULAR_WEIGHTS': 181},
    'Trp': {'TO_1': 'Y',
            'PROTEIN_TO_RNA_COMBINATION': {'UGG'},
            'PKA_AMINOACIDS': [2.38, 9.39],
            'MOLECULAR_WEIGHTS': 204},
    'Val': {'TO_1': 'V',
            'PROTEIN_TO_RNA_COMBINATION': {'GUU', 'GUC', 'GUA', 'GUG'},
            'PKA_AMINOACIDS': [2.32, 9.62],
            'MOLECULAR_WEIGHTS': 117},
}

TO_3_DICT = {nested_dict['TO_1']: key for key,
             nested_dict in AMINOACIDS_DICT.items()}

TRANSCRIBE_DICT: dict = {'A': 'A',
                         'U': 'T',
                         'G': 'G',
                         'C': 'C',
                         'a': 'a',
                         'u': 't',
                         'g': 'g',
                         'c': 'c'}

def check_input(*args: Union[List[str], str], method: str) -> \
                                    Tuple[List[str], Optional[str]]:
    """
    Function to check the validity of the input.
    Args:
    - *args - are supposed to be all sequences to process
    - method - the method to process with method
    Returns:
    - seqs_list - list of sequences
    - seq_on (optional) - in case of local_alignment method
    """

    if len(args) == 0:
        raise ValueError('No input defined.')
    else:
        if method not in ['convert_aa_coding',
                          'from_proteins_seqs_to_rna',
                          'isoelectric_point_determination',
                          'calc_protein_molecular_weight',
                          'back_translate']:
            raise ValueError(method, ' is not a valid method.')
        else:
            seqs_list = list(args)
            for i, seq in enumerate(seqs_list):
                if is_one_letter(seq):
                    print(f'Warning! Function {method}() needs '
                          '3-letter encoded sequences. Your sequence '
                          'will be mutated to a 3-letter encoding.')
                    seqs_list[i] = recode(seq)
                    print(seq, ' sequence has been mutated into: ',
                          seqs_list[i])
            seq_on = None
            return seqs_list, seq_on

def is_one_letter(seq: str) -> bool:
    """
    Defines whether the sequence is 1 coded.
    Args:
    - seq - sequence to check
    Returns:
    - bool
    """
    return all(aa.isalpha() and aa.isupper() for aa in seq)


def convert_aa_coding(seq: str) -> dict:
    """
    Translate 1-letter to 3-letter encoding if 1-letter
    encoded sequence is given and *vice versa*.
    Args:
    - seq - sequence or list of sequences to recode
    Returns:
    - function_result - a dictionary containing recoded sequences as values
    for original sequences keys
    """

    if is_one_letter(seq):
        three_letter_sequence = ""
        for aa in seq:
            three_letter_code = TO_3_DICT.get(aa, aa)
            three_letter_sequence += three_letter_code
        return three_letter_sequence
    # Translate 3-letter to 1-letter coded sequence
    one_letter_sequence = ""
    for aa in range(0, len(seq), 3):
        amino_acid = seq[aa:aa+3]
        one_letter_sequence += AMINOACIDS_DICT[amino_acid]['TO_1']
    return one_letter_sequence


def calc_protein_molecular_weight(*seqs_list: Union[List[str], str]) -> dict:
    """
    :param seqs_list: seqs_list is a list of strings without whitespace
    (e.g. 'AlaSer'). You can put as many sequences as you wish.
    :return: This function returns molecular weight of the protein.
    """
    results = {}
    for seq in seqs_list:
        protein_weight = 0
        aminoacids = [seq[i:i + 3] for i in range(0, len(seq), 3)]
        for i, aminoacid in enumerate(aminoacids):
            if aminoacid in AMINOACIDS_DICT.keys():
                aminoacid_weight = (AMINOACIDS_DICT[aminoacid]
                                    ['MOLECULAR_WEIGHTS'])
                protein_weight += aminoacid_weight
                results[seq] = protein_weight
    return results

def from_proteins_seqs_to_rna(*seqs_list: Union[List[str], str]) -> dict:
    """
    :param seqs_list: a list of strings with type 'ValTyrAla','AsnAspCys'.
    You can pass more than one sequence at the time.
    :return: dictionary, where [key] is your input protein sequences
    and values are combinations of RNA codones, which encode this protein
    """
    results = {}
    for seq in seqs_list:
        rna_combination = ''
        divided_acids = [seq[i:i + 3] for i in range(0, len(seq), 3)]
        for divided_acid in divided_acids:
            if divided_acid in AMINOACIDS_DICT.keys():
                rna_combination += next(iter(AMINOACIDS_DICT[divided_acid]
                                             ['PROTEIN_TO_RNA_COMBINATION']))
            else:
                raise ValueError('Non-protein aminoacids in sequence')
        results[seq] = rna_combination
    return results

def isoelectric_point_determination(*seqs_list: Union[List[str], str]) -> dict:
    """
    :param seqs_list: a list of strings with type 'ValTyrAla','AsnAspCys'.
    You can pass more than one sequence at a time.
    :return: dictionary, where [key] is your input protein sequence and value
    is an isoelectric point of your input proteins
    """
    results = {}
    for aminoacids in seqs_list:
        divided_acids = [aminoacids[i:i + 3] for i in range(0, len(aminoacids),
                                                            3)]
        for divided_acid in divided_acids:
            if divided_acid not in AMINOACIDS_DICT.keys():
                raise ValueError('Non-protein aminoacids in sequence')
        isoelectric_point_mean = 0
        count_groups = 0
        for acid_index, aminoacid in enumerate(divided_acids):
            if acid_index == 0:
                isoelectric_point_mean\
                    += (AMINOACIDS_DICT[aminoacid]['PKA_AMINOACIDS'][0])
                count_groups += 1
            elif acid_index == len(divided_acids) - 1:
                isoelectric_point_mean = (isoelectric_point_mean
                                          + (AMINOACIDS_DICT[aminoacid]
                                             ['PKA_AMINOACIDS'][-1]))
                count_groups += 1
            else:
                if len(AMINOACIDS_DICT[aminoacid]['PKA_AMINOACIDS']) > 2:
                    isoelectric_point_mean = (isoelectric_point_mean
                                              + (AMINOACIDS_DICT[aminoacid]
                                                 ['PKA_AMINOACIDS'][1]))
                    count_groups += 1
        results[aminoacids] = isoelectric_point_mean / count_groups
    return results

def back_translate(*seqs_list: Union[List[str], str]) -> dict:
    """
    :param seqs_list: is a list of strings without whitespace.
    You can put as many sequences as you wish.
    :return: This function returns a dictonary where key is inputed protein
    sequence and values are DNA codons
    """
    results = {}
    for seq in seqs_list:
        rna = list((from_proteins_seqs_to_rna(seq)).get(seq))
        for i in range(len(rna)):
            if rna[i] in TRANSCRIBE_DICT.keys():
                rna[i] = TRANSCRIBE_DICT[rna[i]]
        results[seq] = "".join(rna)
    return results