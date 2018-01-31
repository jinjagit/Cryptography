#  Affine Cipher - by Simon Tharby 2018

#  To encode: E(x) = (ax + b) mod m
#  a, x, b = members of set Z26 AND a is member of set {1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25}

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']

def encodeAffine (a, b, message):
    encoded = ""
    for i in range(0, len(message)):
        for j in range (0, 26):
            if message[i] == alphabet[j]:
                x = (a * j + b)%26
                encoded = encoded + alphabet[x]
    print()
    print("Encoded with a = %d, b = %d; %s " % (a, b, encoded))
    return encoded

#  To decode: D(x) = c(x - b) mod m
#  Where c is the multiplicative inverse of a

aSet = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
cSet = [1, 9, 21, 15, 3, 19, 7, 23, 11, 5, 17, 25]  #  set of multiplicative inverse(s) of respective values of a

def decodeAffine (a, b, encoded):
    decoded = ""
    c = 0
    for n in range(0, 12):
        if a == aSet[n]:
            c = cSet[n]
    for i in range(0, len(encoded)):
        for j in range (0, 26):
            if encoded[i] == alphabet[j]:
                x = (c * (j - b))%26
                decoded = decoded + alphabet[x]
    print("Decoded with a = %d, b = %d; %s " % (a, b, decoded))
    return decoded

message = "ATTACK"
encoded = ""
print()
print("message to encode: " + message)

encoded = encodeAffine(9, 13, message)  #  Example in Understanding Cryptography, by Paar and Pletzl, pages 20-21
decodeAffine(9, 13, encoded)
encoded = encodeAffine(3, 13, message)
decodeAffine(3, 13, encoded)
encoded = encodeAffine(21, 13, message)
decodeAffine(21, 13, encoded)
encoded = encodeAffine(3, 22, message)
decodeAffine(3, 22, encoded)



