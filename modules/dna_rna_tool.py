TRANSCRIBE_DICT = dict(A='A', T='U', G='G', C='C',
                       a='a', t='u', g='g', c='c')
DNA_COMPLEMENT_DICT = dict(A='T', T='A', G='C', C='G',
                           a='t', t='a', g='c', c='g')
RNA_COMPLEMENT_DICT = dict(A='U', U='A', G='C', C='G',
                           a='u', u='a', g='c', c='g')

def check_input_for_nucleic_acids(nucleic_acid: str) -> bool:
    """
    Function checks if inputed data is a nucleic acid or not. If it is it
    returns True, else False.
    :param nucleic_acid: inputed data, type:str
    :return: True if inputed data is a nucleic acid, else returns False
    """
    dna_rna_alphabet = set('ATUGCatugc')
    if (dna_rna_alphabet.issuperset(nucleic_acid)):
        return True
    else:
        return False

def transcribe(nucleic_acid: str) -> str:
    """
    Fenction returns the transcribed sequence of the inputed data.
    :param nucleic_acid: inputed data, type:str
    :return: string of transcribed sequence
    """
    for i in range(len(nucleic_acid)):
        nucleic_acid[i] = TRANSCRIBE_DICT[nucleic_acid[i]]
    return str("".join(nucleic_acid))

def reverse(nucleic_acid: str) -> str:
    """
    Function returns the reversed sequence of the inputed data.
    :param nucleic_acid: inputed data, type:str
    :return: string of reversed sequence
    """
    return "".join(reversed(nucleic_acid))

def complement(nucleic_acid: str) -> str:
    """
    Function returns the complemented sequence of the inputed data.
    :param nucleic_acid: inputed data, type:str
    :return: string of complemented sequence
    """
    for i in range(len(nucleic_acid)):
        if nucleic_acid[i] in DNA_COMPLEMENT_DICT.keys():
            nucleic_acid[i] = DNA_COMPLEMENT_DICT[nucleic_acid[i]]
        elif nucleic_acid[i] in RNA_COMPLEMENT_DICT.keys():
            nucleic_acid[i] = RNA_COMPLEMENT_DICT[nucleic_acid[i]]
    return "".join(nucleic_acid)

def reverse_complement(nucleic_acid: str) -> str:
    """
    Function returns the reversed and complemented sequence of the inputed data.
    :param nucleic_acid: inputed data, type:str
    :return: string of reversed and complemented sequence
    """
    return "".join(reverse(complement(nucleic_acid)))
