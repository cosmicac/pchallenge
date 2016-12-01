from __future__ import print_function
from collections import defaultdict
import sys

# find all anagrams of w1 in word_bank 
# by creating character count dictionaries 
# and checking if dictionaries are equal
# should take O(n + m) time, where n is the length of 
# the argument word, m is the total length of our word bank
def find_anagrams(w1, word_bank):

	# create dictionary of character counts
	char_counts_w1 = make_char_counts(w1.lower())

	# loop through and create anagram list based on whether 
	# character count dictionaries are equal
	return [w2 for w2 in word_bank if char_counts_w1 == make_char_counts(w2.lower())]
			
def make_char_counts(w):
	char_counts = defaultdict(int)
	for c in w:
		char_counts[c] += 1
	return char_counts

if __name__ == '__main__':

	# path to the txt file from arguments
	path_to_txt = sys.argv[1]

	# extract lines into a list
	word_bank = open(path_to_txt).read().split('\n')
	while True:
		word_to_match = raw_input() 
		if word_to_match == '':
			break
		anagrams = find_anagrams(word_to_match, word_bank)
		if anagrams:
			for a in anagrams:
				print(a, end=" ")
			print('\n', end = "")
		else:
			print('-')