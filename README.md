# Files Generator

This script generates a set of text files according to the cases described in "testcases.txt". 

Further purpose is to analyze and compare the Similarity Algorithms (LSH, TLSH, SDHASH).

## Parameters

config.ini file contains the following parameters:

```
input_location = directory where the input files are located
output_location = directory of the generated files
NR_WORDS_CUT: number of words to be cut from the file
NR_LINES_CUT = number of lines to be cut from the file
NR_WORDS_ADDED = number of word to be added to the file
NR_LINES_ADDED = number of lines to be added to the file
SECTION_SIZE = size (number of words) of the section the files will be divided (these sections will shuffled)
```

## Run

```
python files_generator.py
```

(Python version 3.7.0)

## Performed tests

"input" directory contains 2 text files: metallica.txt and wikipedia.txt 

"output" directory contains 21 generated file according to the cases below and the parameters from config.ini:

1. Exactly similar files
2. Few words cut from the beginning
3. Few lines cut from the beginning
4. Few words cut from the end
5. Few lines cut from the end
6. Few words cut from the middle
7. Few lines cut from the middle
8. Few words added to the beginning
9. Few lines added to the beginning
10. Few words added to the end
11. Few lines added to the end
12. Few words added to the middle
13. Few lines added to the middle
14. Swapping the beginning and the end ---- ?
15. Scrambling the paragraphs
16. Scrambling lines
17. Scrambling words
18. Scrambling similarly sized words/sections
19. Interleaving paragraphs with unrelated text (can be scrambling with another original text)
20. Interleaving sentences with unrelated text (can be scrambling with another original text)
21. Interleaving words with unrelated text (can be scrambling with another original text)

## Notes

Some of the generated files don't contain endl's (e.g. scrambling words). To view the files, please use a text editor which can automatically structure the file with endlines (e.g. Sublime).

