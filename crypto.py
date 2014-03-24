__author__ = 'cypher odyssey'

import math
import random


class Crypto:

    #initialize function
    def __init__(self, seed, text):
        self.text=text
        self.seed=seed

    #Smearing function
    def smear(self):
        numcols= math.ceil(math.sqrt(len(self.text))) #Number of cols to form the right matrix
        padlen = int((numcols -(len(self.text) % numcols))%numcols) #padding length to fill in Matrix
        plaintext = self.text + ("#"*padlen) #adding on the padding characters need to make N*M Matrix
        rows = map(''.join,zip(*[iter(plaintext)]*int(numcols))) #breaking the plaintext into even blocks

        #sort rows in random fashion with the given seed
        random.seed(self.seed)
        randlist = [(random.random(),x) for x in rows]
        randlist.sort()

        #sort columns of each row in random fashion with the new given seed
        random.seed(self.seed+1)

        cipher = [] # will hold the final cipher after it has been transposed

        #transposition of columns
        for strip,value in randlist:
            value = [(random.random(),g) for g in value]
            value.sort()
            for n,m in value:
                cipher.append(m)

        #prints the cipher
        ccipher = ''.join (cipher)
        print "CIPHER:", ccipher

    def unsmear(self ,seed,cipher):
        random.seed(seed+1)#generate the seed
        #array to hold the random values. Note that copies will be made, hence the reason to have more than one.
        randvals = []
        randcopy =[]
        randcopy2 = []

        i=-1

        #fill randvals with the required random numbers (length of cipher)
        for f in range(0,len(cipher)):
            randvals.append(random.random())

        #make the necessary copies that will be used later on
        for k in range(0,len(cipher)):
            randcopy.append(randvals[k])
            randcopy2.append(randvals[k])

        numcols= math.ceil(math.sqrt(len(cipher))) #Number of cols to form the right matrix
        numrows = len(cipher)/numcols #Get the number of rows in the N*M matrix

        #This section slices the random values into N*M row/columns similar to what is done in smear()
        matrix = []
        for r in range(int(numrows)):
            randvals2 = []
            for c in range(int(numcols)):
                randvals2.append(randvals.pop(0))
            randvals2.sort()
            matrix.append(randvals2)
            del randvals2

        #Make a dictionary(hash) (key:value pair) of random values array matrix[]
        Dictionary = {}
        index=-1
        for key in matrix:
            for key2 in key:
                index = index+1
                Dictionary[key2]=index

        #unsmearing the values from the cipher , randcopy2 now holds the first stage of the unsmeared array
        x=-1
        for item in randcopy:
            x=x+1
            randcopy2[x] = cipher[Dictionary[item]]

        random.seed(seed)   #generate seed again
        p=-1
        tempvals=[]
        tempvallast = []

        #get the row lengths again
        rows = map(''.join,zip(*[iter(randcopy2)]*int(numcols)))
        #fill in the tempvals with the random values
        for item in rows:
            tempvals.append(random.random())

        tempvals2 = sorted(tempvals) #copy what is in tempvals but sorted

        #copy what is in tempvals into tempvallast
        for m in tempvals:
            tempvallast.append(m)

        #hash or dicitonary that will store the key:value pair of the random value array
        Dictionary2 ={}
        for u in tempvals2:
            p=p+1
            Dictionary2[u]=p

        #finally we unsmear the rows and we print it
        x=-1
        for item in tempvals:
            x=x+1
            tempvallast[x] = rows[Dictionary2[item]]

        print "PLAINTEXT:",''.join(tempvallast)
