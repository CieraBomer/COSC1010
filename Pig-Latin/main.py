#
# Ciera Bomer
# 4-13-2025
# Pig Latin Programming Project
# COSC 1010
#
# Varibles
pla_convert = 0
first_letter = 0
whole_word = 0
pla_word = 0
input_sentence = 0
words = 0
platin_words = 0
converted_word = 0
pla_sentence = 0
# Define a function to convert a word to Pig Latin
def pla_convert(word):
    # Check if the word has at least one character
    if len(word) > 0:
        # Get the first letter
        first_letter = word[0]
        # Get the rest of the word
        whole_word = word[1:]
        # Make the rest of the Pig Latin word
        pla_word = whole_word + first_letter + 'ay'
        #  Return the pig latin word
        return pla_word
    else:
        return
# Prompt the user to enter a sentence
input_sentence = input('Enter a sentence: ')
# Split the input into a list
words = input_sentence.split()
# Empty list for pig latin words
platin_words = []
# Loop for the words in the list
for word in words:
    # Convert using the function to Pig Latin
    converted_word = pla_convert(word)
    # Add to list for Pig Latin words
    platin_words.append(converted_word)
# Make it into a single string
pla_sentence = ' '.join(platin_words)

# Print English
print('\nEnglish', input_sentence)
# Print Pig Latin
print('Pig Latin: ', pla_sentence)

