import modules.fastaq_tool as fqt
import modules.dna_rna_tool as drt

def fastaq_tool_running(seqs: dict, gc_bounds: int or float or tuple = (0, 100),
          length_bounds: int or tuple = (0, 2 ** 32),
          quality_threshold: int = 0) -> dict:
    """
    This function is main. The main function returns a dictionary consisting
    of only those sequences that pass all conditions.
    :param seqs: dictionary consisting of fastq-sequences, the structure is:
    Key - a string, the name of the sequence, Value - tuple of two strings:
    sequence and quality
    :param gc_bounds: the interval for filtering, type: tuple if both edges of
    the interval is given or int or float if only right edge is given, default
    is (0, 100)
    :param length_bounds: the interval for filtering, type: tuple if both
    edges of the interval is given or int if only right edge is given, default
    is (0, 2 ** 34)
    :param quality_threshold: threshold value of average quality for filtering,
    default is 0
    :return: returns a dictionary consisting of only those sequences that pass
    all conditions
    """
    result = {}
    for seq in seqs:
        if fqt.gc_count(seqs[seq][0], gc_bounds) and \
            fqt.length_count(seqs[seq][0], length_bounds) and \
                fqt.quality_check(seqs[seq][1], quality_threshold):
            result[seq] = seqs[seq]
    return result
    
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
