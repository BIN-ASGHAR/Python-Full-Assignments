phrase = "i am not here in Future!"

print(phrase.capitalize()) # Capital the first letter of given sentence
print(phrase.replace("am" , "will")) # Replace the give word
print(phrase.upper())  # To convert sentence in upper case
print(phrase.lower()) # To convert sentence in lower case
print(phrase.index('here')) # To check index of specific character
print(len(phrase))  # To check the length of Sentence
print(phrase[23])   # To get the selected letter

phrase_here = phrase.count("here") # count the how many times a specific letter appears in sentence
print(phrase_here)