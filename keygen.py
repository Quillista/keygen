import math
import random
import sys
#keygen
#sys.maxsize
tamseed=2**256
tamnonce=2**128
#metodo semilla
def newseed():
    seed = random.randrange(tamseed)
    rng = random.Random(seed)
    return seed

#metodo nonce
def newnonce():
    nonce = random.randrange(tamnonce)
    rng = random.Random(nonce)
    return nonce

#pruebas
seed1= newseed()

nonce1= newnonce()
print(seed1)
print(nonce1)


try:
    # Attempt to open the file
    with open('cseed.txt', 'r') as file:
        exists=True
        print("The file exists.")
except FileNotFoundError:
    exists=False
    print("The file does not exist.")

if(exists==False):
    f = open('cseed.txt', 'w')
    f.write(str(newseed()))
    f.close()


f = open('cseed.txt', 'r')
data= f.read()

data= int(data)
if(len(str(data))==len(str(tamseed))):
    print("si tiene el mismo tamaño")
else:
    print("no fue")
    print(data, tamseed)
    print(len(str(tamseed)))
    print(len(str(data)))

#print(data)



# for each in f:
#     print(each)

