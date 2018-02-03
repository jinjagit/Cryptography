# Affine Cipher, Chosen Plaintext Attack - by Simon Tharby 2018
# Homework; Question 1.14, page 27, Understanding Cryptography, by Paar and Pletzl

# This code assumes the attacker is able to have 2 letters encoded and receives knowledge of their respective encoded
# outputs. It also assumes one letter is the first letter in the alphabet used (an 'A' in this case), and this letter
# is first in the pair. (Though the last point is arbitrary: We need the letter with value 0 to be encoded, and to
# know which it is in the encrypted output.)

# To encode: E(x) = (ax + b) mod m
# a, x, b = members of set Z26 AND a is member of set {1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25}

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']

def encodeAffine (a, b, message):
    encoded = ""
    for i in range(0, len(message)):
        for j in range (0, 26):
            if message[i] == alphabet[j]:
                x = (a * j + b)%26
                encoded = encoded + alphabet[x]
                char2 = j  # to return index of 2nd character, since it is always last in these tests
    print("Encoded with a = %d, b = %d; %s " % (a, b, encoded))
    return encoded, char2

#  Analyze to find value of a and b for this Affine Cipher

aSet = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

def analyzeChosen (encoded, char2):
    a = -1
    b = -1
    x = -1
    for i in range (0,26):
        if encoded[0] == alphabet[i]:
            b = i
    for i in range(0, 26):
        if encoded[1] == alphabet[i]:
            x = i
    for i in range(0, len(aSet)):  # iterating through encoding, using b value to find a (? can replace with algo?)
        if x == ((aSet[i] * char2+b))%26:
            a = aSet[i]
    print()
    print("chosen plaintext attack reveals a = %d, b = %d" % (a, b))

message = "AT"
encoded = ""
print()
print("message to encode: " + message)

encoded, char2 = encodeAffine(9, 13, message)
analyzeChosen(encoded, char2)

message = "AZ"
encoded = ""
print()
print("message to encode: " + message)

encoded, char2 = encodeAffine(21, 4, message)
analyzeChosen(encoded, char2)

message = "ZA"
encoded = ""
print()
print("TESTING 'BAD' VERSION, WHERE 'A' IS NOT FIRST LETTER")
print("message to encode: " + message)

encoded, char2 = encodeAffine(21, 4, message)
analyzeChosen(encoded, char2)
