#!/usr/bin/python
# Encode Reverse Cipher  

def encode(plainText): 

	cipherText = ""
	
	i = len(plainText) - 1
	while i >= 0:
		cipherText = cipherText + plainText[i]
		i = i - 1

	return cipherText

if __name__ == "__main__": 
	
	in_f = open("plaintext.txt", "r")
	out_f = open("ciphertext.txt", "w")
	out_f.write(encode(in_f.read()))
	in_f.close()
	out_f.close()
	
	f = open("ciphertext.txt", "r")
	print("Encoded Text:")
	print(f.read())
	f.close()
