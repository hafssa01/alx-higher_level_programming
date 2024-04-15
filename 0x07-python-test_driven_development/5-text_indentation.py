#!/usr/bin/python3
"""Module for text_indentation methode."""

def text_indentation(text):
	"""Method for adding 2 new lines after '.?:' chars.

	Args:
	    text: The str text.

	Raises:
	    TypeError: If text is not a str.
	"""
	if not isinstance(text, str):
		raise TypeError("text should be a string")
	result = ''
	for c in text:
		if c in ["?",".",":"]:
			result += c + '\n\n'
		else:
			result += c
	print(result, end='') 
	
if __name__ == "__main__":
	import doctest
	doctest.testfile("tests/5-text_indentation.txt")
