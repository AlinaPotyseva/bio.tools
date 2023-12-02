import os

def convert_multiline_fasta_to_oneline(input_fasta, output_fasta=''):
    """
    Function, reads the input fasta file, in which the sequence can be split
    into several lines, and then saves it into a new fasta file in which each
    sequence fits into a single line.
    :param input_fasta: the path to the fasta file
    :param output_fasta: the name of output file
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
    :param output_fasta: the name of output file
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

def select_genes_from_gbk_to_fasta(input_gbk: str, genes: list, n_before=1, 
                                   n_after=1, output_fasta=''):
    """
    Function pulls flanking genes from gbk annotation.
    :param input_gbk: the path to the fasta file
    :param genes: list of genes
    :param n_before: number of genes before the gene of interest, default=1
    :param n_after: number of genes after the gene of interest, default=1
    :param output_fasta: the name of output file, if not given adds 'out' at
    the beginning of the input file
    :return: the fasta file
    """
    with open(input_gbk, 'r') as gbk_file:
        gbk_lines = gbk_file.readlines()
    all_genes = [line.split('"')[1] for line in gbk_lines if "/gene=" in line]
    result_genes = []
    for gene in genes:
        target_gene = all_genes.index(gene)
        i = 1
        j = 1
        while i <= n_before:
            if target_gene-i >= 0:
                result_genes.append(all_genes[target_gene-i])
            i += 1
        while j <= n_after:
            if target_gene+j <= len(all_genes):
                result_genes.append(all_genes[target_gene+j])
            j += 1
    indexes = []
    for new_gene in result_genes:
        indexes.append([gbk_lines.index(line) for line in gbk_lines if new_gene in line])
    seqs = []
    for ind in indexes:
        start = ind[0]
        while '/translation=' not in gbk_lines[start]:
            start += 1
        end = start+1
        seq = gbk_lines[start].split('"')[1].replace('\n', '')
        while '"' not in gbk_lines[end]:
            seq = seq+gbk_lines[end].replace('\n', '').replace(' ', '')
            end += 1
        seq = seq+gbk_lines[end].split('"')[0].replace(' ', '')
        seqs.append(seq)
    if output_fasta == '':
        output_fasta = input_gbk.split('/')[-1]
    with open('out_'+output_fasta+'.fasta', 'w') as output_fasta:
        for n in range(len(result_genes)):
            output_fasta.write('>'+result_genes[n]+'\n')
            output_fasta.write(seqs[n]+'\n')
