#!/usr/bin/python
# Encode Caesar Cipher  

def encode(plainText): 
	UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
	
	upperLength = len(UPPER_LETTERS)
	lowerLength = len(LOWER_LETTERS)

	cipherText = ""
	
	for char in plainText:
		if char in UPPER_LETTERS:
			
			num = UPPER_LETTERS.find(char) # get the number of the character
			num = num + 1
			
			if num >= upperLength:
				num = num - upperLength
			elif num < 0:
				num = num + upperLength
			cipherText = cipherText + UPPER_LETTERS[num]
			
		elif char in LOWER_LETTERS:
			
			num = LOWER_LETTERS.find(char) # get the number of the character
			num = num + 1
			
			if num >= lowerLength:
				num = num - lowerLength 
			elif num < 0:
				num = num + lowerLength 
			cipherText = cipherText + UPPER_LETTERS[num]
			
		else:
			cipherText = cipherText + char
			
	return cipherText

if __name__ == "__main__": 
	
	in_f = open("plaintext.txt", "r")
	out_f = open("ciphertext.txt", "w")
	out_f.write(encode(in_f.read().upper()))
	in_f.close()
	out_f.close()
	
	f = open("ciphertext.txt", "r")
	print("Encoded Text:")
	print(f.read())
	f.close()
