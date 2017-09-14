# Accidentally I messed up this quote from Richard Feynman.
# Two words are out of place
# Your task is to fix it by swapping the right words with code

# Also, print the sentence to the output with spaces in between.

# “What I cannot create, I do not understand.”

words = ["What", "I", "do", "create,", "I", "cannot", "not", "understand."]

first_word = words.index('do')
second_word = words.index('cannot')

def fixed_quote(words):
    words[first_word], words[second_word] = words[second_word], words[first_word]
    print(words)

fixed_quote(words)