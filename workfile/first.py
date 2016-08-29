#
import re

print (10/3)

t = ['hello', 'my', 'name', 'is']


def searchInWords (word, k):
    try:
        return k.index(word)
    except:
        return -1



print searchInWords ('hewllo', t)

f = open('text.txt', 'r')

newW = []
#print f.read(1)
for line in f:
    #print line
    result = re.findall( r'\w+'  , line)
    for word in result:
        #print word
        if (searchInWords(word, newW) < 0):
            #print word
            newW.append(word.lower())

f.close()
print t
print newW

entering = 0

for word in newW:
    if (searchInWords(word, t) >= 0):
        entering +=1

print entering/float(len(newW)) * 100
