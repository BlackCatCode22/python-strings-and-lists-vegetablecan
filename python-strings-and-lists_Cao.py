'''
Written By Donald Cao
Date: 09/02/2023
CIT-95
Python Program Two: Strings and Lists
'''

###String and String Manipulations

text = "Python is an amazing programming language. It is versatile, easy to learn, and powerful."
#Length Calculation: Write a function calculate_length(text) that takes the given text as input and returns the length of the text (including spaces and punctuation).

def calculate_length(text):
	print(text,"\n")

calculate_length(text)

#Uppercase and Lowercase Conversion: Write Python code that takes the given text as input and returns the text in uppercase letters followed by the text in lowercase letters.

print("Uppercase Only:",text.upper(),"\n")
print("Lowercase Only:",text.lower(),"\n")

#Word Count: Write Python code that takes the given text as input and returns the total number of words in the text.
print(len(text.split()),"words totaled.\n")

#Substring Extraction: Write Python code that takes the given text, and returns the substring of text starting from the start index (inclusive) and ending at the end index (exclusive) supplied by a user.
user_input=eval(input("Enter a number between 0 to 88: "))
print(text[0:user_input])

#Word Replacement: Write Python code that takes the given text, a target word (input by the user), and replacement word (input by the user) as input, and returns the text with all occurrences of the target word replaced by the replacement word.
print("\nPrompt Below:\n",text)
select_input=input("Enter a word to replace from the prompt: ")
replace_input=input("Enter a replacement word: ")
print("Result Below:\n",text.replace(select_input,replace_input),"\n")

#Whitespace Removal: Write Python code that takes the given text as input and returns the text with all leading and trailing whitespaces removed.
print(text.replace(" ",''),'\n')

#Splitting into Sentences: Write a function split_sentences(text) that takes the given text as input and returns a list of sentences present in the text.
def split_sentences(text):
	splitting=eval(input("Enter a number, 0 to 14: "))
	print(' '.join(text.split()[0:splitting]),'\n')

split_sentences(text)

#Word Reversal: Write Python code that takes the given text as input and returns the text with each word reversed.
def reversed_sentences(text):
	words=text.split()
	reverseSentence=''.join(reversed(words))
	print(reverseSentence,'\n')

reversed_sentences(text)

#Character Count: Write Python code that takes the given text and a character as input, and returns the number of occurrences of the specified character in the text.
print(len(text),'\n',)

#Substring Count: Write Python code that takes the given text and a substring as input, and returns the number of occurrences of the specified substring in the text.
print("There are 88 characters in the given text.")
substring_selection=eval(input("Enter a number between 0 to 88: "))
print(''.join(text[0:substring_selection]),'\n')

###List and List Manipulations

#List Creation: Create a list called word_list by splitting the given text into words.
word_list=text.split()
print(word_list,'\n')

#Appending: Append the word "Pythonic" to the word_list.
word_list.append('Pythonic')
print(word_list,'\n')

#Insertion: Insert the word "awesome" at the beginning of the word_list.
word_list.insert(0, 'awesome')
print(word_list,'\n')

#Indexing and Slicing: Print the third word in the word_list and then print a sublist containing the words from the 6th to 9th position.
print(word_list[3])
print(word_list[6:9],'\n')

#Removal: Remove the word "amazing" from the word_list.
word_list.remove('awesome')
print(word_list,'\n')

#Sorting: Sort the word_list in alphabetical order.
word_list.sort()
print(word_list,'\n')

#Counting: Count the occurrences of the word "is" in the word_list.
count=len([i for i in word_list if i=="is"])
print(count,'\n')

#Joining: Create a string sentence by joining the words in the word_list with spaces.
print(' '.join(word_list),'\n')

#Reversal: Reverse the order of elements in the word_list.
word_list.reverse()
print(word_list,'\n')

#Copying: Create a new list copied_list by copying the contents of the word_list.
copied_list = word_list.copy()
print(copied_list)