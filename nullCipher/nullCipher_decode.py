#!/usr/bin/python
# Decode Null Cipher  

def decode(encryptedText, charPosition): 

	decodedText = ""

	for word in encryptedText.split():
		if (word[charPosition] >= 'A' and word[charPosition] <= 'Z') or (word[charPosition] >= 'a' and word[charPosition] <= 'z'):
			decodedText += word[charPosition]
	return decodedText

if __name__ == "__main__": 
	
	keyPosition = 2 #key is the second letter of each word

	f = open("ciphertext.txt", "r")
	o = open("plaintext.txt", "w")
	o.write(decode(f.read(), keyPosition-1))
	f.close()
	o.close()
	
	f = open("plaintext.txt", "r")
	print("Decoded Text:")
	print(f.read())
	f.close()