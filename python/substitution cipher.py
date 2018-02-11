# Substitution Cipher - by Simon Tharby - 26/01/18

import random  # including relevant library module

print()
print("Attacking a substitution cipher with letter frequency analysis:")

# 'randomizes' list: pseudo-random only, of course, so need seed to force different order:

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']

shuffled = alphabet.copy()

print()
x = int(input("Enter a seed (any integer): "))

random.seed(x)
random.shuffle(shuffled)

print()
print(alphabet)
print(shuffled)

original = "TOP SECRET DO NOT LET THE SECRET KEY TO OUR SUPER SECRET CODE FALL INTO ENEMY HANDS"
encoded = ""

for x in range(0, len(original)):

    if original[x] == " ":
        encoded = encoded + " "
    else:
        for y in range(0, 26):
            if original[x] == alphabet[y]:
                encoded = encoded + shuffled[y]

print()
print("Original message:  " + original)
print("Encoded message:   " + encoded)

# Create letter frequency attack procedure:
# count number of each letter in message and create ordered list (highest freq. to lowest)
# how to handle equal freq?

# create list of 26 integers, and set all to zero:

frequency = list(range(26))
for x in range(0, 26):
    frequency[x] = 0

# count frequency of each letter and store as integer in list (in place of alphabet letter index)

for x in range(0, len(encoded)):

    for y in range(0, 26):
        if encoded[x] == alphabet[y]:
            frequency[y] = frequency[y]+1

maxval = max(frequency)

print()
print(frequency)

# create list of alphabet letters, ordered by frequency of appearance in message
# equal frequencies ordered in order as found:

freqlist = alphabet.copy() # use a copy of alphabet list as a basis (items will be replaced)
n = 0
freqtest = 0

for x in range(0, maxval+1):
    freqtest = maxval-x
    for y in range(0, 26):
        if frequency[y] == freqtest:
            freqlist[n] = alphabet[y]
            n = n+1

print()
print("letters in encoded message ordered by frequency: ")
print(freqlist)

# use list of alphabet letters ordered by freq. in English language
# (using: https://en.wikipedia.org/wiki/Letter_frequency#Relative_frequencies_of_letters_in_the_English_language)

EnglishFreq = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'C', 'U', 'M', 'W', 'F', 'G', 'Y', 'P', 'B',
               'V', 'K', 'J', 'X', 'Q', 'Z']

# step through message a letter at a time, replacing each letter with it's freq. twin.

decoded = ""

for x in range(0, len(encoded)):
    if encoded[x] != " ":
        for y in range(0, 26):
            if encoded[x] == freqlist[y]:
                decoded = decoded + EnglishFreq[y]
    else:
        decoded = decoded + " "

print()
print("Decoded message:   " + decoded)