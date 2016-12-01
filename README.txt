1. The offline running time is O(n) where n is the total number of characters in our input dictionary. We just need to load the words into our word bank, so there is nothing else to do in the offline step. The online step consists of two steps. The first step makes a character count dictionary of the input word. This takes O(m) time where m is the number of characters in the input word. The second step loops over all of the words in our word bank, constructs a character count dictionary for each word, and checks if the character count dictionary is the same as the input character count dictionary. .This step takes O(n) time where n is the total number of characters in our input dictionary. This is because essentially make one pass through all the characters to construct our character count dictionaries, and then another pass to compare dictionaries. So it takes roughly ~ 2n = O(n) time. So, overall, the program takes O(n + m) time. 

2. The things we need to store are:

. the word bank 
. the input word
. a character count dictionary for the input word
. at each iteration, a character count dictionary for the current word in our word bank

. Word bank takes O(n) space where n is the total number of characters in our input dictionary.
. The input word takes O(d) space where d is number of characters in the input word.
. The character count dictionary for the input word also takes O(d) space. 
. Since we only need the character count dictionary for the current word in our word bank, the worst case would be the longest word in our word bank. So, if C is the set of word lengths of our word bank, this step takes O(max(C)) space. 

So overall, the program takes O(n + d + max(C)) space. 

3. You could break your word bank into chunks that fit in memory, and then in the online step load each chunk in and check for anagrams against each chunk separately. This would add a lot of expensive memory access runtime from loading large amounts of data in and out of memory. 