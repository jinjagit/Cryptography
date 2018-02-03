#  Affine Cipher - by Simon Tharby 2018

#  To encode: E(x) = (ax + b) mod m
#  a, x, b = members of set Z26 AND a is member of set {1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25}

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']


def encodeAffine(a, b, message):
    encoded = ""
    for i in range(0, len(message)):
        for j in range (0, 26):
            if message[i] == alphabet[j]:
                x = (a * j + b)%26
                encoded = encoded + alphabet[x]
    print("Encoded with a = %d, b = %d; %s " % (a, b, encoded))

    return encoded


def calcThirdCipher(a1, b1, a2, b2):
    a3 = (a1*a2)%26
    b3 = ((a2*b1)+b2)%26

    return a3, b3


a1 = 3
b1 = 5
a2 = 11
b2 = 7

message = "KINDNESS"
encoded = ""
print()
print("message to encode: " + message)
print()

encoded = encodeAffine(a1, b1, message)
print("Re-encode 1st result with 2nd Affine Cipher;")
encoded = encodeAffine(a2, b2, encoded)

a3, b3 = calcThirdCipher(a1, b1, a2, b2)
print()
print("Encode with single (derived) Affine Cipher;")
encoded = encodeAffine(a3, b3, message)