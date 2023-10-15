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
    is (0, 2 ** 32)
    :return: True if the length of the sequence is in length_bounds, else False
    """
    if type(length_bounds) == int:
        length_bounds = (0, length_bounds)
    result = len(seq[0])
    return length_bounds[0] <= result <= length_bounds[1]

def quality_check(seq: tuple, quality_threshold: int = 0) -> bool:
    """
    Function returns the quality of the sequence.
    :param seq: consists of two strings: sequence and quality, type: tuple
    :param quality_threshold: threshold value of average quality for filtering,
    default is 0
    :return: True if the average quality is less, then quality_threshold, else
    False
    """
    quality_sum = 0
    for letter in seq[1]:
        quality_sum += ord(letter) - 33
    mean = quality_sum / len(seq)
    return mean >= quality_threshold
    
def check_file(input_file: str) -> bool:
    """
    Function checks if inputed data is file or not
    :param input_file: The name of the inputed file.
    :return: True is inputed data is a file, else False.
    """
    if os.path.isfile(input_file):
        return True
    else:
        return False

def fastaq_reading(input_path: str, input_file: str) -> dict:
    """
    Function reads an inputed file.
    :param input_path: path, where the file is located
    :param input_file: the name of the file
    :return: a dictionary with fastq sequences
    """
    if check_file(input_file):
        fastq_dict = {}
        with open(os.path.join(input_path, input_file)) as file:
            for line in file:
                if ' ' in line and '+' not in line:
                    sequence = file.readline().strip()
                    quality = file.readline().strip()
                    fastq_dict[line] = ([sequence, quality])
        return fastq_dict

