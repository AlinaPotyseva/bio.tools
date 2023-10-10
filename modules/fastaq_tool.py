def gc_count(seq: tuple, gc_bounds: int or float or tuple = (0, 100)) -> bool:
    """
    Function gc_count counts GC-content of the inputed sequence. It returns
    True if GC-content is in a given interval (gc_bounds), else it returns
    False.
    :param seq: consists of two strings: sequence and quality, type: tuple
    :param gc_bounds: the interval for filtering, type: tuple if both edges of
    the interval is given or int or float if only right edge is given, default
    is (0, 100)
    :return: True if gc-content of the sequence is in gc_bounds, else False
    """
    if type(gc_bounds) == int or type(gc_bounds) == float:
        gc_bounds = (0, gc_bounds)
    gc = 0
    for nt in seq[0]:
        if nt == 'G' or nt == 'C':
            gc += 1
    result = 100 * gc / len(seq[0])
    return gc_bounds[0] <= result <= gc_bounds[1]

def length_count(seq: tuple, length_bounds: int or tuple = (0, 2 ** 32)) \
        -> bool:
    """
    Function counts the length of the sequence. It returns True if the length
    of the sequence is in the given length_bounds, else it returns False.
    :param seq: consists of two strings: sequence and quality, type: tuple
    :param length_bounds: the interval for filtering, type: tuple if both
    edges of the interval is given or int if only right edge is given, default
    is (0, 2 ** 34)
    :return: True if the length of the sequence is in length_bounds, else False
    """
    if type(length_bounds) == int:
        length_bounds = (0, length_bounds)
    result = len(seq[0])
    return length_bounds[0] <= result <= length_bounds[1]