# https://www.codewars.com/kata/52d1bd3694d26f8d6e0000d3/train/python

class VigenereCipher(object):
    def __init__(self, key, alphabet):
       self.key = key
       self.alphabet = alphabet
    
    def encode(self, text):
        key_string = ''
        encoded = ''
        num = 26 if self.alphabet[0] == 'a' else 46
        for pos in range(len(text)):
            key_string += self.key[pos % len(self.key)]
        for pos in range(len(text)):
            if text[pos] not in self.alphabet:
                encoded += text[pos]
            else:
                encoded += self.alphabet[(self.alphabet.find(text[pos]) + self.alphabet.find(key_string[pos])) % num]
        return encoded
    def decode(self, text):
        key_string = ''
        decoded = ''
        num = 26 if self.alphabet[0] == 'a' else 46
        for pos in range(len(text)):
            key_string += self.key[pos % len(self.key)]
        for pos in range(len(text)):
            if text[pos] not in self.alphabet:
                decoded += text[pos]
            else:                        
                decoded += self.alphabet[(self.alphabet.find(text[pos]) - self.alphabet.find(key_string[pos])) % num]
        return decoded


abc = "abcdefghijklmnopqrstuvwxyz"
key = "カタカナ"
c = VigenereCipher(key, abc)
print(c.encode('タモタワ'))
print(c.encode('CODEWARS'))
print(c.decode('yiuzsrzhot'))