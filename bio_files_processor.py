import os

def convert_multiline_fasta_to_oneline(input_fasta, output_fasta=''):
    """
    Function, reads the input fasta file, in which the sequence can be split
    into several lines, and then saves it into a new fasta file in which each
    sequence fits into a single line.
    :param input_fasta: the path to the fasta file
    :param output_fasta: the name of output file, if not given adds 'out' at
    the beginning of the input file
    :return: the new fasta file
    """

    if output_fasta == '':
        output_fasta = os.path.basename(input_fasta)
    with open(input_fasta, 'r') as fasta_file:
        fasta_lines = fasta_file.readlines()
    with open('output_' + output_fasta + '.fasta', 'w') as output_fasta:
        line_number = 0
        while line_number < len(fasta_lines)-1:
            if fasta_lines[line_number][0] == '>':
                output_fasta.write(fasta_lines[line_number])
                line_number += 1
            else:
                count = line_number
                string = ''
                while count < len(fasta_lines) and fasta_lines[count][0] != '>':
                    string = string+fasta_lines[count].replace('\n', '')
                    count += 1
                output_fasta.write(string+'\n')
                line_number = count

def change_fasta_start_pos(input_fasta: str, shift: int, output_fasta: str = None):
    """
    Function shifts the starting position in the file
    :param input_fasta: the path to the fasta file
    :param shift: integer (can be negative) - by how much to shift the initial 
    position in the file
    :param output_fasta: the name of output file, if not given adds 'out' at
    the beginning of the input file
    :return:  a fasta file with shifted sequence
    """

    if os.path.isfile(input_fasta) == False:
        print('The path does not exist!')
    with open(input_fasta, 'r') as fasta_file:
        lines = fasta_file.readlines()
    with open(os.path.join(input_fasta)):
        for line in lines:
            if not line.startswith('>'):
                line = line
                if shift > 0:
                    first_part_line = line[:shift]
                    last_part_line = line[shift+1:]
                    shifting_nucleotide = line[shift]
                    result_sequence = shifting_nucleotide + first_part_line + last_part_line
                elif shift == -1:
                    shifting_nucleotide = line[shift]
                    first_part_line = line[:shift]
                    result_sequence = shifting_nucleotide + first_part_line
    output_dir = os.path.dirname(input_fasta)
    if output_fasta == None:
        input_fasta2 = os.path.basename(input_fasta) + '_2'
        output_fasta_2 = os.path.basename(input_fasta2)
    elif output_fasta.find('.fasta') == False:
        output_fasta_2 = output_fasta + '.fasta'
    else:
        output_fasta_2 = output_fasta
    with open(os.path.join(output_dir, output_fasta_2), mode='w') as file:
        file.write(result_sequence)
