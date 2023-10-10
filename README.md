# bio_tool
## Here it is some useful tules for a junior bioinformatician

## Table of contents
  * [What you can do using this tool?](#applications)
  * [The structure of the tool](#structure)
  * [How to install the tool?](#Installation)
  * [Module 1](#) 
  * [Module 2](#)
  * [What can module fastaq_tool.py do?](#Fastaq_module)
  * [Usage example](#examples)
 
 
### Installation

To get the tool clone the git repository:

```bash
git clone https://github.com/AlinaPotyseva/bio_tools.git 
cd bio_tools
```

### Fastaq_module

This module consists of three different functions:

 * The `gc_count` function counts GC-content of the inputed sequence. It returns True if GC-content is in a given interval (gc_bounds), else it returns False. Inputed data consists of some parametrs:
   + the first on is `seq`, which represents two strings: sequence and quality and it's type is tuple
   + the second one is `gc_bounds`, which represents the interval for filtering, type of this parametr can be tuple if both edges of the interval is given or int (float) if only right edge is given, default value is (0, 100)
 * The `length_count` function counts the length of the sequence. It returns True if the length of the sequence is in the given `length_bounds`, else it returns False. Inputed data consists of some parametrs:
   + the first on is `seq`, which represents two strings: sequence and quality and it's type is tuple
   + the second one is `length_bounds`, which represents the interval for filtering, type of this parametr can be tuple if both edges of the interval is given or int if only right edge is given, default value is (0, 2 ** 32)
