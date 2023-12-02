import modules.fastaq_tool as fqt
import modules.dna_rna_tool as drt
import modules.protein_tool as prt
from typing import List, Optional, Tuple, Union

def fastaq_tool_running(input_path: str, input_file: str,
          gc_bounds: int or float or tuple = (0, 100),
          length_bounds: int or tuple = (0, 2 ** 32),
          quality_threshold: int = 0, output_filename: str = None):
    """
    This function is main. The main function returns a file consisting
    of only those sequences that pass all conditions.
    :param input_path: path, where the file is located
    :param input_file: name of the inputted file
    :param gc_bounds: the interval for filtering, type: tuple if both edges of
    the interval is given or int or float if only right edge is given, default
    is (0, 100)
    :param length_bounds: the interval for filtering, type: tuple if both
    edges of the interval is given or int if only right edge is given, default
    is (0, 2 ** 32)
    :param quality_threshold: threshold value of average quality for filtering,
    default is 0
    :param output_filename: name of the output file, if None, then 
    outputed_filename = inputed_file
    :return: a file with results of filtering
    """

    seqs = fqt.fastaq_reading(input_path, input_file)
    out_data = {}
    for seq in seqs:
        if fqt.gc_count(seqs[seq][0], gc_bounds) and \
           fqt.length_count(seqs[seq][0], length_bounds) and \
           fqt.quality_check(seqs[seq][1], quality_threshold):
            out_data[seq] = seqs[seq]
    fqt.fasta_writing(out_data, input_file, output_filename)
    
def dna_rna_tool_running(*input_data: str) -> str or list:
    """
    Function takes as input an arbitrary number of arguments with DNA or RNA
    sequences (*str*) and the name of the procedure to be executed (it is
    always the last argument, *str*, see example of use). After that, the c
    ommand performs the specified action on all submitted sequences.
    If one sequence is submitted, a string with the result is returned.
    If more than one sequence is submitted, a list of strings is returned.
    :param input_data: str of nucleic acids and a procedure
    :return: string or list of data
    """
    results = []
    nucleic_acids = list(input_data)[:-1]
    for nucleic_acid in nucleic_acids:
        if drt.check_input_for_nucleic_acids(nucleic_acid):
            if list(input_data)[-1] == 'transcribe':
                results.append(drt.transcribe(list(nucleic_acid)))
            if list(input_data)[-1] == 'reverse':
                results.append(drt.reverse(list(nucleic_acid)))
            if list(input_data)[-1] == 'complement':
                results.append(drt.complement(list(nucleic_acid)))
            if list(input_data)[-1] == 'reverse_complement':
                results.append(drt.reverse_complement(list(nucleic_acid)))
        else:
            pass
    if len(results) == 1:
        results_str = str(results[0])
        return results_str
    else:
        return results


def protein_tool_running(*args: Tuple[Union[List[str], str]],
         method: Optional[str] = None) -> dict:
    """
    This function provides the access to the following methods:
    1. Translate 1 letter to 3 letter encoding and *vice versa* - the last
    argument: 'convert_aa_coding'
        - needs at least 1 sequence 1- or 3- letter encoded. Can recieve
        more than 1 sequences
        - returns a dictionary containing translations between 1- and 3-
        letter codes
    2. Find possible RNA sequences for defined protein sequence - the
    last argument: 'from_proteins_seqs_to_rna'
        - needs at least 1 protein sequence 3-letter encoded
        - returns a dictionary, where key is your input protein sequences
        and values are combinations of RNA codones, which encode this protein
    3. Determinate isoelectric point - the last argument:
    'isoelectric_point_determination'
        - needs an input containing at least 1 aminoacid. Can recive multiple
        different protein sequences
        - returns a dictionary, where key is your input protein sequence and
        value is an isoelectric point of this protein
    4. Calculate protein molecular weight - the last argument:
    'calc_protein_molecular_weight'
        - Seqs is an argument of the function. It is a string without
    whitespace (e.g. 'AlaSer'). You can put as many arguments as you wish.
        - returns a dictionary with protein sequences as keys and their
        calculated molecular weight as corresponding values
    5. Determine possible DNA sequence from protein sequence - the last
    argument: 'back_transcribe'
        - needs a string without whitespaces. You can put as many arguments as
        you wish.
        - returns a dictonary where keys are inputed protein sequences and
        corresponding values are possible DNA codons
    """
    seqs_list, seq_on = prt.check_input(*args, method=method)
    print(f'Your sequences are: {seqs_list}',
          f'The method is: {method}', sep='\n')
    match method:
        case 'convert_aa_coding':
            recode_dict: dict = {}
            for seq in seqs_list:
                recode_dict[seq] = prt.convert_aa_coding(seq=seq)
            return recode_dict
        case 'from_proteins_seqs_to_rna':
            return prt.from_proteins_seqs_to_rna(*seqs_list)
        case 'calc_protein_molecular_weight':
            return prt.calc_protein_molecular_weight(*seqs_list)
        case 'isoelectric_point_determination':
            return prt.isoelectric_point_determination(*seqs_list)
        case 'back_translate':
            return prt.back_translate(*seqs_list)
