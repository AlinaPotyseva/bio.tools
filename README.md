## Here it is some useful tools for a junior bioinformatician
***
> *Using this repository you can take advantage of several programs for working with nucleic acids, proteins and fastq sequences.*
***
## Table of contents
  * [What you can do using this tool?](#Applications)
  * [The structure of the tool](#Structure)
  * [How to install the tool?](#Installation)
  * [What can module dna_rna_tool.py do?](#DNA_RNA_module) 
  * [What can module protein_tool.py do?](#Protein_module)
  * [What can module fastaq_tool.py do?](#Fastaq_module)
  * [How to use bio_tools.py?](#bio_tools.py)
  * [Usage example](#Examples)
 
### Applications

You can use this tool to get:
* **transcribed** DNA to RNA and RNA to DNA
* **reversed** DNA and RNA sequences
* **complement** DNA and RNA sequences
* **reversed** and **complement** DNA and RNA sequences
* find possible **RNA sequences** for defined protein sequence
* determinate **isoelectric point**
* calculate protein **molecular weight**
* determine possible **DNA sequence** from protein sequence
* **filtered** suquences, which has passed all checks of your given *gc_bounds*, *length_bounds* and *quality_threshold* 

### Structure 

```python
    -/
     |- bio_tools.py
     |- README.md
     |- modules/
           |- dna_rna_tool.py
           |- доп_модуль_2.py
           |- fastaq_tool.py
           |- ...
```
 
To work with the program a user only needs to import the main script and call any of the three functions from it.

### Installation

To get the tool clone the git repository:

```bash
git clone https://github.com/AlinaPotyseva/bio_tools.git 
cd bio_tools
```
### DNA&RNA module

This module consists of five different functions:

* The `check_input_for_nucleic_acids` function checks if inputed data is a nucleic acid or not. If it is it returns True, else False. Inputed data `nucleic_acid` should be string.
* The `transcribe` function returns a string: the transcribed sequence of the inputed data. Inputed data `nucleic_acid` should be string.
* The `reverse` function returns a string: the reversed sequence of the inputed data. Inputed data `nucleic_acid` should be string.
* The `complement` function returns a string: the complement sequence of the inputed data. Inputed data `nucleic_acid` should be string.
* The `reverse_complement` function returns a string: the reversed and complement sequence of the inputed data. Inputed data `nucleic_acid` should be string.

### Protein module

This module consists of five different functions:

* The `convert_aa_coding` translates 1 letter to 3 letter encoding and *vice versa* 
  + needs at least 1 sequence 1- or 3- letter encoded. Can recieve more than 1 sequences
  + returns a dictionary containing translations between 1- and 3-letter codes
* The `from_proteins_seqs_to_rna` find possible RNA sequences for defined protein sequence
  + needs at least 1 protein sequence 3-letter encoded
  + returns a dictionary, where key is your input protein sequences and values are combinations of RNA codones, which encode this protein
* The `isoelectric_point_determination` determinate isoelectric point
  + needs an input containing at least 1 aminoacid. Can recive multiple different protein sequences
  + returns a dictionary, where key is your input protein sequence and value is an isoelectric point of this protein
* The `calc_protein_molecular_weight` calculate protein molecular weight
  + Seqs is an argument of the function. It is a string without whitespace (e.g. 'AlaSer'). You can put as many arguments as you wish.
  + returns a dictionary with protein sequences as keys and their calculated molecular weight as corresponding values
* The `back_transcribe` determine possible DNA sequence from protein sequence
  + needs a string without whitespaces. You can put as many arguments as you wish.
  + returns a dictonary where keys are inputed protein sequences and corresponding values are possible DNA codons

### Fastaq module

This module consists of seven different functions:

 * The `check_file` checks if inputed data is file or not. It returns True if inputed data is a file, else False. Inputed data consists of just one parametr:
   + `input_file` is the name of the inputed file.
 * The `fastaq_reading` function reads an inputed file. It returns a dictionary with fastq sequences. Inputed data consists of some parametrs:
   + the first one is `input_path` is the path, where the inputted file is located.
   + the second one is `input_file` is the name of the inputted file.
 * The `gc_count` function counts GC-content of the inputed sequence. It returns True if GC-content is in a given interval (gc_bounds), else it returns False. Inputed data consists of some parametrs:
   + the first on is `seq`, which represents two strings: sequence and quality and it's type is tuple
   + the second one is `gc_bounds`, which represents the interval for filtering, type of this parametr can be tuple if both edges of the interval is given or int (float) if only right edge is given, default value is (0, 100)
 * The `length_count` function counts the length of the sequence. It returns True if the length of the sequence is in the given `length_bounds`, else it returns False. Inputed data consists of some parametrs:
   + the first on is `seq`, which represents two strings: sequence and quality and it's type is tuple
   + the second one is `length_bounds`, which represents the interval for filtering, type of this parametr can be tuple if both edges of the interval is given or int if only right edge is given, default value is (0, 2 ** 32)
 * The `quality_check` function returns the quality of the sequence. It returns True if the average quality is less, then *quality_threshold*, else False. Inputed data consists of some parametrs:
   + the first on is `seq`, which consists of two strings: sequence and quality and it's type is tuple
   + the second one is `quality_threshold`, which is a threshold value of average quality for filtering, default value is 0
 * The `check_dir` checks if directory fastq_filtrator_resuls exists. If it exists, the function returns True, else it creates the directory in the working directory and returns True.
 * The `fasta_writing` creates a file with results of filtration. Inputed data consists of some parametrs:
   + the first on is `out_data`, which is a dictionary of data after filtration
   + the second one is `input_file`, which is the name of the inputted file.
   + the third one is `output_filename`, which is the name of the outputted file, if `outputed_filename` is None then `outputed_filename = inputed_file`
 
###  bio_tools.py

>The main script consists of three functions, which uses modules, which were described above.

#### 1. dna_rna_tool_running
This program can perform some manipulations with inputed DNA and RNA sequences. The input should be in the format: `dna_rna_tool_running('sequences', 'process')`.

As a process you should input:
* `transcribe` to get a transcribed sequence 
* `reverse` to get reversed sequence
* `complement` to get a complementary sequence
* `reverse_complement` to get reverse and complementary sequence

The desired number of sequences can be fed to the input at once. The program is able to distinguish between DNA and RNA, as well as character case.

#### 2. protein_tool_running

This program can perform some manipulations with inputed polyaminoacid sequences. The input should be in the format:
`protein_tool_running('*args', 'method')`.

Arguments:
- `*args[str]` sequences to work with. You can pass several arguments into all functions
- `method` - a method to use

#### 3. fastaq_tool_running
This program can perform some manipulations with input DNA sequences. The input should be in the format
```python
fastaq_tool_running(input_path: str, input_file: str,
          gc_bounds: int or float or tuple = (0, 100),
          length_bounds: int or tuple = (0, 2 ** 32),
          quality_threshold: int = 0, output_filename: str = None)
```

* As an `input_path` you should input a path, where the file is located
* As an `input_file` you should input the name of the inputted file
* As a `gc_bounds` you should input the interval for filtering, type: tuple if both edges of the interval is given or int (or float) if only right edge is given, default value is (0, 100)
* As a `length_bounds` you should input the interval for filtering, type: tuple if both edges of the interval is given or int if only right edge is given, default value is (0, 2 ** 32)
* As a `quality_threshold` you should input a threshold value of average quality for filtering, default value is 0
* As an `output_filename` you should input the name of the outputted file, if `outputed_filename` is None then `outputed_filename = inputed_file`
As a result of the work of the program you will get a file with filtered sequences in the directory `fastq_filtrator_resuls`

### Examples of usage

#### dna_rna_tool_running
```python
dna_rna_tool_running('ATG', 'transcribe')  #'AUG'
dna_rna_tool_running('ATG', 'reverse') #'GTA'
dna_rna_tool_running('AtG', 'complement') #'TaC'
dna_rna_tool_running('ATg', 'reverse_complement') #'cAT'
dna_rna_tool_running('ATG', 'aT', 'reverse') #['GTA', 'Ta']`
```

#### protein_tool_running
```python
protein_tool_running('ArgArg', method='convert_aa_coding')
# Your sequences are: ['ArgArg'] 
# The method is: convert_aa_coding
# {'ArgArg': 'RR'}
protein_tool_running('ArgArg', method='from_proteins_seqs_to_rna')
#Your sequences are: ['ArgArg']
#The method is: from_proteins_seqs_to_rna
#{'ArgArg': 'AGGAGG'}
protein_tool_running('ArgArg', method='calc_protein_molecular_weight')
#Your sequences are: ['ArgArg']
#The method is: calc_protein_molecular_weight
#{'ArgArg': 348}
protein_tool_running('ArgArg', method='isoelectric_point_determination')
#Your sequences are: ['ArgArg']
#The method is: isoelectric_point_determination
#{'ArgArg': 7.425}
protein_tool_running('ArgArg', method='back_translate')
#Your sequences are: ['ArgArg']
#The method is: back_translate
#{'ArgArg': 'CGTCGT'}
```
#### fastaq_tool_running
![изображение](https://github.com/AlinaPotyseva/bio_tools/assets/145059499/22282069-1fe0-402f-93f9-2c5f9c6c5653)

```python
fastaq_tool_running('/home/alina/PycharmProjects/HW_6_2','data.txt')
```

![изображение](https://github.com/AlinaPotyseva/bio_tools/assets/145059499/ed5ef267-2e59-4d04-bb4a-09162c319a95)
![изображение](https://github.com/AlinaPotyseva/bio_tools/assets/145059499/bca62998-63be-40ee-b012-661d06d325fd)

Author: Potyseva Alina (mailto:alina.potyseva@gmail.com)
