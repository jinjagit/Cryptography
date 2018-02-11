# Substitution Cipher 2 - by Simon Tharby - 26/01/18

print()
print("Attacking a substitution cipher with letter frequency analysis:")

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']

encoded = "LRVMNIR BPR SUMVBWVR JX BPR LMIWV YJERYRKBI JX QMBM WI BPR XJVNI MKD YMIBRUT JX IRHX WI BPR RIIRKVR " \
           "JX YMBINLMTMIPW UTN QMUMBR DJ W IPMHH BUT BJ RHNVWDMBR BPR YJERYRKBI JX BPR QMBM MVVJUDWKO BJ YT " \
           "WKBRUSURBMBWJK LMIRD JK XJUBT TRMUI JX IBNDT WB WI KJB MK RMIT BMIQ BJ RASHMWK RMVP YJERYRKB MKD WBI " \
           "IWOKWXWVMKVR MKD IJYR YNIB URYMWK NKRASHMWKRD BJ OWER M VJYSHRBR RASHMKMBWJK JKR CJNHD PMER BJ LR " \
           "FNMHWXWRD MKD WKISWURD BJ INVP MK RABRKB BPMB PR VJNHD URMVP BPR IBMBR JX RKHWOPBRKRD YWKD VMSMLHR JX " \
           "URVJOKWGWKO IJNKDHRII IJNKD MKD IPMSRHRII IPMSR W DJ KJB DRRY YTIRHX BPR XWKMH MNBPJUWBT LNB YT " \
           "RASRUWRKVR CWBP QMBM PMI HRXB KJ DJNLB BPMB BPR XJHHJCWKO WI BPR SUJSRU MSSHWVMBWJK MKD WKBRUSURBMBWJK " \
           "W JXXRU YT BPRJUWRI WK BPR PJSR BPMB BPR RIIRKVR JX JQWKMCMK QMUMBR CWHH URYMWK WKBMVB"

print()
print("Encoded message:   " + encoded)

# Create letter frequency attack procedure:
# count number of each letter in message and create ordered list (highest freq. to lowest)

# create list of 26 integers, and set all to zero:

frequency = list(range(26))
for x in range(0, 26):
    frequency[x] = 0

# count frequency of each letter in message and store as integer in list (in place of alphabet letter index)

for x in range(0, len(encoded)):

    for y in range(0, 26):
        if encoded[x] == alphabet[y]:
            frequency[y] = frequency[y]+1

maxval = max(frequency)

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

def getChar (message):
    errorFound = 1

    while (errorFound == 1):
        char = input(message)
        if len(char) != 1:
            print("ERROR! Input only a single letter")
            errorFound = 1
        elif (ord(char) < 65) | ((ord(char) > 90) & (ord(char) < 97)) | (ord(char) > 122):
            print("ERROR! Input only a single letter")
            errorFound = 1
        else:
            errorFound = 0

    if (ord(char) > 96) & (ord(char) < 123):
        char = chr(ord(char) - 32)

    return char

def replaceChars (inputString):

    print()
    identical = 1
    while (identical == 1):
        char1 = getChar("input 1st character to switch: ")
        char2 = getChar("input 2nd character to switch 1st with: ")
        if char1 != char2:
            identical = 0
        else:
            print("ERROR! 1st and 2nd characters must be different")

    inputString = inputString.replace(char1, "*")
    inputString = inputString.replace(char2, char1)
    inputString = inputString.replace("*", char2)
    return inputString

decodedPlus = decoded

exit = 0
while (exit == 0):
    decodedPlus = replaceChars(decodedPlus)

    print()
    print(decodedPlus)