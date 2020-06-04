#!/usr/bin/python
# decode Caesar Cipher  

def decode(encryptedText): 
	UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
	
	upperLength = len(UPPER_LETTERS)
	lowerLength = len(LOWER_LETTERS)

	decryptedText = ""
	
	for char in encryptedText:
		if char in UPPER_LETTERS:
			
			num = UPPER_LETTERS.find(char) # get the number of the character
			num = num - 1
			
			if num >= upperLength:
				num = num - upperLength
			elif num < 0:
				num = num + upperLength
			decryptedText = decryptedText + UPPER_LETTERS[num]
			
		elif char in LOWER_LETTERS:
			
			num = LOWER_LETTERS.find(char) # get the number of the character
			num = num - 1
			
			if num >= lowerLength:
				num = num - lowerLength 
			elif num < 0:
				num = num + lowerLength 
			decryptedText = decryptedText + UPPER_LETTERS[num]
			
		else:
			decryptedText = decryptedText + char
			
	return decryptedText

if __name__ == "__main__": 
	
	in_f = open("encryptedText.txt", "r")
	out_f = open("decryptedText.txt", "w")
	out_f.write(decode(in_f.read().upper()))
	in_f.close()
	out_f.close()
	
	f = open("decryptedText.txt", "r")
	print("decoded Text:")
	print(f.read())
	f.close()
