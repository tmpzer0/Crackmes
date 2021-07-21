import random
import string
import subprocess

#key length -> 9 
#7 < 9 <=10

#min ascii value 112 -> p
#max ascii value 126 -> ~

#min key ascii 1008 > 999

def keys(chars = 'pqrstuvwxyz{|}~', N=9):
	return ''.join(random.choice(chars) for _ in range(N))

passwd = keys()
print("Key: " +passwd)

subprocess.run(["./keygen.bin"],text=True ,input=passwd)

print("\nUsed: " +passwd)
