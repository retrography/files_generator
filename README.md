# Files Generator
This script generates a set of text files according to the cases described in "testcases.txt". <br /> Further purpose is to analyze and compare the Similarity Algorithms (LSH, TLSH, SDHASH).


### Parameters
```
config.ini file contains the following parameters:
input_location = directory where the input files are located
output_location = directory of the generated files
NR_WORDS_CUT: number of words to be cut from the file
NR_LINES_CUT = number of lines to be cut from the file
NR_WORDS_ADDED = number of word to be added to the file
NR_LINES_ADDED = number of lines to be added to the file
SECTION_SIZE = size (number of words) of the section the files will be divided (these sections will shuffled)
```

### Run
```
python files_generator.py
```
(Python version 3.7.0)

## Performed tests

"input" directory contains 2 text files: metallica.txt and wikipedia.txt <br />
"output" directory contains 21 generated file according to the cases from testcases.txt and the parameters from config.ini

## Notes

Some of the generated files don't contain endl's (e.g. scrambling words). To view the files, please use a text editor which can automatically structure the file with endlines (e.g. Sublime).

