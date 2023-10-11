# bio_tool
## Here it is some useful tools for a junior bioinformatician
***
> *Using this repository you can take advantage of several programs for working with nucleic acids, proteins and fastq sequences.*
***
## Table of contents
  * [What you can do using this tool?](#Applications)
  * [The structure of the tool](#Structure)
  * [How to install the tool?](#Installation)
  * [What can module dna_rna_tool.py do?](#DNA_RNA_module) 
  * [Module 2](#Protein module)
  * [What can module fastaq_tool.py do?](#Fastaq_module)
  * [How to use bio_tools.py?](#bio_tools.py)
  * [Usage example](#examples)
 
### Applications

You can use this tool to get:
* **transcribed** DNA to RNA and RNA to DNA
* **reversed** DNA and RNA sequences
* **complement** DNA and RNA sequences
* **reversed** and **complement** DNA and RNA sequences
* 
*
*
* **filtered** suquences, which has passed all checks of your given *gc_bounds*, *length_bounds* and *quality_threshold* 

### Stcucture 

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

### Fastaq module

This module consists of three different functions:

 * The `gc_count` function counts GC-content of the inputed sequence. It returns True if GC-content is in a given interval (gc_bounds), else it returns False. Inputed data consists of some parametrs:
   + the first on is `seq`, which represents two strings: sequence and quality and it's type is tuple
   + the second one is `gc_bounds`, which represents the interval for filtering, type of this parametr can be tuple if both edges of the interval is given or int (float) if only right edge is given, default value is (0, 100)
 * The `length_count` function counts the length of the sequence. It returns True if the length of the sequence is in the given `length_bounds`, else it returns False. Inputed data consists of some parametrs:
   + the first on is `seq`, which represents two strings: sequence and quality and it's type is tuple
   + the second one is `length_bounds`, which represents the interval for filtering, type of this parametr can be tuple if both edges of the interval is given or int if only right edge is given, default value is (0, 2 ** 32)
 * The `quality_check` function returns the quality of the sequence. It returns True if the average quality is less, then *quality_threshold*, else False. Inputed data consists of some parametrs:
   + the first on is `seq`, which consists of two strings: sequence and quality and it's type is tuple
   + the second one is `quality_threshold`, which is a threshold value of average quality for filtering, default value is 0
 
###  bio_tools.py

>The main script consists of three functions, which uses modules, which were described above.

#### 1. dna_rna_tool_running
This program can perform some manipulations with input DNA and RNA sequences. The input should be in the format `dna_rna_tool_running('sequences', 'process')`.

As a process you should input:
* `transcribe` to get a transcribed sequence 
* `reverse` to get reversed sequence
* `complement` to get a complementary sequence
* `reverse_complement` to get reverse and complementary sequence

The desired number of sequences can be fed to the input at once. The program is able to distinguish between DNA and RNA, as well as character case.

#### 2. 

#### 3. fastaq_tool_running
This program can perform some manipulations with input DNA sequences. The input should be in the format
```python
fastaq_tool_running(seqs: dict, 
                    gc_bounds: int or float or tuple = (0, 100),
                    length_bounds: int or tuple = (0, 2 ** 32),
                    quality_threshold: int = 0) -> dict
```

* As a `seqs` you should input a dictionary consisting of fastq-sequences, the structure is:
    + Key - a string, the name of the sequence
    + Value - tuple of two strings: sequence and quality
* As a `gc_bounds` you should input the interval for filtering, type: tuple if both edges of the interval is given or int (or float) if only right edge is given, default value is (0, 100)
* As a `length_bounds` you should input the interval for filtering, type: tuple if both edges of the interval is given or int if only right edge is given, default value is (0, 2 ** 32)
*  As a `quality_threshold` you should input a threshold value of average quality for filtering, default value is 0
