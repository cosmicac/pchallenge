from __future__ import print_function
from collections import defaultdict
import sys

# find all anagrams of w1 in word_bank 
# by creating character count dictionaries 
# and checking if dictionaries are equal
def find_anagrams(w1, word_bank):

	# create dictionary of character counts
	char_counts_w1 = make_char_counts(w1.lower())

	# loop through and create anagram list based on whether 
	# character count dictionaries are equal
	return [w2 for w2 in word_bank if char_counts_w1 == make_char_counts(w2.lower())]
			
# make a character count dictionary out of input word
def make_char_counts(w):
	char_counts = defaultdict(int)
	for c in w:
		char_counts[c] += 1
	return char_counts

if __name__ == '__main__':

	# path to the txt file from arguments
	path_to_txt = sys.argv[1]

	# extract lines into a word bank
	word_bank = open(path_to_txt).read().split('\n')

	# input loop
	while True:

		#get input word to match
		word_to_match = raw_input() 

		# if input is empty string, just exit
		if word_to_match == '':
			break

		# find anagrams of input word in word bank
		anagrams = sorted(find_anagrams(word_to_match, word_bank))

		# output matches if any
		if anagrams:
			for a in anagrams:
				print(a, end=" ")
			print('\n', end = "")
		else:
			print('-')