'''
Have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string. If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty.
Sample Test Cases

Input:"fun&!! time"

Output:"time"

Input:"I love dogs"

Output:"love"


'''
import re
def longestWord(sentence):
	x = re.findall("[a-zA-Z]+", sentence) 
	longestWord = ""
	for word in x:
		if len(word) > len(longestWord):
			longestWord = word
			print(longestWord)
	return longestWord
	
	