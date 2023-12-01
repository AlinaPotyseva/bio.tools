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
        output_fasta = input_fasta.split('/')[-1]
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
