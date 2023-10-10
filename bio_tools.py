import modules.fastaq_tool as fqt

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