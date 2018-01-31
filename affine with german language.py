#  Affine Cipher with German Language - by Simon Tharby 2018

#  To encode: E(x) = (ax + b) mod m
#  a, x, b = members of set Z30 AND a is member of set {1, 7, 11, 13, 17, 19, 23, 29}

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z', 'Ä', 'Ö', 'Ü', 'ß']

#  To decode: D(x) = c(x - b) mod m
#  Where c is the multiplicative inverse of a

aSet = [1, 7, 11, 13, 17, 19, 23, 29]
cSet = [1, 13, 11, 7, 23, 19, 17, 29]  #  set of multiplicative inverse(s) of respective values of a

def decodeAffine (a, b, encoded):
    decoded = ""
    c = 0
    for n in range(0, 8):
        if a == aSet[n]:
            c = cSet[n]
    for i in range(0, len(encoded)):
        for j in range (0, 30):
            if encoded[i] == alphabet[j]:
                x = (c * (j - b))%30
                decoded = decoded + alphabet[x]
    print("Decoded with a = %d, b = %d; %s " % (a, b, decoded))
    return decoded

encoded = "ÄUßWß "  #  Homework in Understanding Cryptography, by Paar and Pletzl, page 27
print()
print("message to decode: " + encoded)
decodeAffine(17, 1, encoded)
