import os
import random
import re
import configparser

# Parameters:
Config = configparser.ConfigParser()
Config.read("config.ini")
INPUT = Config.get('io','input_location')
OUTPUT = Config.get('io','output_location')
NR_WORDS_CUT = int(Config.get('parameters','NR_WORDS_CUT'))
NR_LINES_CUT = int(Config.get('parameters','NR_LINES_CUT'))
NR_WORDS_ADDED = int(Config.get('parameters','NR_WORDS_ADDED'))
NR_LINES_ADDED = int(Config.get('parameters','NR_LINES_ADDED'))
SECTION_SIZE = int(Config.get('parameters','SECTION_SIZE'))  # file will be scrambled by setions of 5 words

class FilesGenerator:
	content = {}
	def __init__(self):
		files_list = os.listdir(INPUT)
		# print ("files_list: " + str(files_list))
		self.file1 = os.path.join(INPUT,files_list[0])
		self.filename1 = os.path.basename(self.file1.split(".")[0])

		self.file2 = os.path.join(INPUT,files_list[1])

		self.content[self.file1] = self.read_file(self.file1)
		self.content[self.file2] = self.read_file(self.file2)

		# create output directory:
		try:
			os.mkdir(OUTPUT)
		except FileExistsError:
			pass

	def read_file(self, file_path):
		with open(file_path, 'r') as f:
			# print(f.read())
			return f.read()

	def write_file(self, file_out_name, content):
		with open(file_out_name, 'w') as f:
			f.write(content)

	def duplicate(self):
		output_file_path = os.path.join(OUTPUT,self.filename1)
		self.write_file( output_file_path + "_duplicate.txt", self.content[self.file1])
	
	def cutting(self):
		output_file_path = os.path.join(OUTPUT,self.filename1)

		# cutting words:
		words = self.content[self.file1].split(" ")
		cutted_start_words = " ".join(words[NR_WORDS_CUT : -1])
		cutted_end_words = " ".join(words[0 : NR_WORDS_CUT*(-1)])
		cutted_mid_words_1 = " ".join(words[0 : (len(words) // 2 - NR_WORDS_CUT // 2)])
		cutted_mid_words_2 = " ".join(words[(len(words) // 2 + NR_WORDS_CUT // 2)*(-1):])

		self.write_file(output_file_path + "_cut_beginning_words.txt", cutted_start_words)
		self.write_file(output_file_path + "_cut_end_words.txt", cutted_end_words)
		self.write_file(output_file_path + "_cut_mid_words.txt", cutted_mid_words_1 + cutted_mid_words_2)

		# cutting lines:
		lines = self.content[self.file1].split("\n")
		cutted_start_lines = "\n".join(lines[NR_LINES_CUT:])
		cutted_end_lines = "\n".join(lines[0 : NR_LINES_CUT*(-1)])
		cutted_mid_lines_1 = "\n".join(lines[0 : (len(lines) // 2 - NR_LINES_CUT // 2)])
		cutted_mid_lines_2 = "\n".join(lines[(len(lines) // 2 + NR_LINES_CUT // 2)*(-1):])

		self.write_file(output_file_path + "_cut_beginning_lines.txt", cutted_start_lines)
		self.write_file(output_file_path + "_cut_end_lines.txt", cutted_end_lines)
		self.write_file(output_file_path + "_cut_mid_lines.txt", cutted_mid_lines_1 + cutted_mid_lines_2)

		# scrumbling lines (1doc):
		scrambled_lines = [l.strip() for l in lines]
		random.shuffle(scrambled_lines)
		scrambled_lines_content = "\n".join(scrambled_lines)
		self.write_file(output_file_path + "_scrambled_lines.txt", scrambled_lines_content)

	def adding(self):
		output_file_path = os.path.join(OUTPUT,self.filename1)

		# adding words:
		words = self.content[self.file1].split(" ")
		added_words_raw = self.content[self.file2].split(" ")[0:NR_WORDS_ADDED]
		added_words = [w.strip() for w in added_words_raw]
		added_start_words = " ".join(added_words + [(words[0].strip())] + words[1:])
		added_end_words = " ".join(words + added_words)
		added_mid_words = " ".join(words[0 : (len(words) // 2)] + added_words + words[((len(words) // 2) * (-1)):])

		self.write_file(output_file_path + "_add_beginning_words.txt", added_start_words)
		self.write_file(output_file_path + "_add_end_words.txt", added_end_words)
		self.write_file(output_file_path + "_add_mid_words.txt", added_mid_words)

		# adding lines:
		lines = self.content[self.file1].split("\n")
		added_lines = self.content[self.file2].split("\n")[0:NR_LINES_ADDED]
		added_start_lines = "\n".join(added_lines + lines)
		added_end_lines = "\n".join(lines + added_lines)
		added_mid_lines = "\n".join(lines[0 : (len(lines) // 2)] + added_lines + lines[((len(lines) // 2) * (-1)):])

		self.write_file(output_file_path + "_add_beginning_lines.txt", added_start_lines)
		self.write_file(output_file_path + "_add_end_lines.txt", added_end_lines)
		self.write_file(output_file_path + "_add_mid_lines.txt", added_mid_lines)

	def scrambling(self):
		output_file_path = os.path.join(OUTPUT,self.filename1)

		# scrambling words (2 docs):
		words1 = [re.sub('\W+', "", w) for w in self.content[self.file1].split(" ")]
		words2 = [re.sub('\W+', "", w) for w in self.content[self.file2].split(" ")]
		scrambled_words = words1 + words2
		random.shuffle(scrambled_words)
		scrambled_words_merged =  " ".join(scrambled_words)
		self.write_file(output_file_path + "_scrambled_words_2docs.txt", scrambled_words_merged)

		#scrambling words (1doc):
		scrambled_words_one_doc = [re.sub('\W+', "", w) for w in words1]
		random.shuffle(scrambled_words_one_doc)
		scrambled_words_doc =  " ".join(scrambled_words_one_doc)
		self.write_file(output_file_path + "_scrambled_words.txt", scrambled_words_doc)

		# scrambling sections of words:
		block_list = []
		for i in range(0, len(words1), SECTION_SIZE):
			block = " ".join(words1[i : (i+SECTION_SIZE)])
			block_list.append(block)
			# print("block: " + str(i))
			# print(block)
		random.shuffle(block_list)
		block_list_content = " ".join(block_list)
		self.write_file(output_file_path + "_shuffled_sections.txt", block_list_content)

		# scrambling sentences (2 docs):
		sentences1 = [w.replace('\n'," ").strip() + "." for w in self.content[self.file1].split(".")]
		sentences2 = [w.replace('\n'," ").strip() + "." for w in self.content[self.file2].split(".")]
		scrambled_sentences = sentences1 + sentences2
		random.shuffle(scrambled_sentences)
		scrambled_sentences_merged = " ".join(scrambled_sentences)
		self.write_file(output_file_path + "_scrambled_sentences_2docs.txt", scrambled_sentences_merged)
		
		# swapping begining of the file with the end of the file
		first_half = sentences1[0 : (len(sentences1)//2)]
		second_half = sentences1[((-1)*len(sentences1)//2) : -1]
		swapped_halves = " ".join(second_half + ["\n"] + first_half)
		self.write_file(output_file_path + "_swapped_halves.txt", swapped_halves)

		# scrambling paragraphs (2 docs):
		paraghraphs1 = [w.replace('\n'," ").strip() for w in self.content[self.file1].split("\t")[1:]]
		paraghraphs2 = [w.replace('\n'," ").strip() for w in self.content[self.file2].split("\t")[1:]]
		scrambled_pars = paraghraphs1 + paraghraphs2
		random.shuffle(scrambled_pars)
		scrambled_pars_merged = "\t" + "\n\t".join(scrambled_pars)
		self.write_file(output_file_path + "_scrambled_paragraphs_2docs.txt", scrambled_pars_merged)

		# scrambling paraghraphs (1doc):
		scrambled_paragraphs = paraghraphs1
		random.shuffle(scrambled_paragraphs)
		scrambled_paragraphs_merged = "\t" + "\n\t".join(scrambled_paragraphs)
		self.write_file(output_file_path + "_scrambled_paragraphs.txt", scrambled_paragraphs_merged)

FilesGeneratorObj = FilesGenerator()
FilesGeneratorObj.duplicate()
FilesGeneratorObj.cutting()
FilesGeneratorObj.adding()
FilesGeneratorObj.scrambling()