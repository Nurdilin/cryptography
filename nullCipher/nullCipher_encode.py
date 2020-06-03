#!/usr/bin/python
# Encode Null Cipher  

dictionary = {'A' : "Alpha", 
	'B' : "Bravo", 
	'C' : "Charlie", 
	'D' : "Delta",
	'E' : "Echo", 
	'F' : "Foxtrot",
	'G' : "Golf",
	'H' : "Hotel",
	'I' : "India",
	'J' : "Juliett", 
	'K' : "Kilo",
	'L' : "Lima",
	'M' : "Mike",
	'N' : "November",
	'O' : "Oscar",
	'P' : "Papa",
	'Q' : "Quebec",
	'R' : "Romeo",
	'S' : "Sierra",
	'T' : "Tango", 
	'U' : "Uniform", 
	'V' : "Victor", 
	'W' : "Whiskey", 
	'X' : "Xray", 
	'Y' : "Yankee", 
	'Z' : "Zulu"}
		
def encode(plainText): 
	cipherText = "" 
	for character in plainText: 
		cipherText += str(dictionary[character])
	return cipherText.upper()  

if __name__ == "__main__": 
	f = open("plaintext.txt", "r")
	o = open("ciphertextDumb.txt", "w")
	o.write(encode(f.read()))
	f.close()
	o.close()
	
	f = open("ciphertextDumb.txt", "r")
	print("Dumb Encrypted text")
	print(f.read())
	f.close()
