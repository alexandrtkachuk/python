import re
import sys

print (10/3)

t = ['hello', 'my', 'name', 'is']


def searchInWords (word, k):
    try:
        return k.index(word)
    except:
        return -1




#result = re.match(r'==next==$', '==next==f')
#print "None!!" if result == None


#sys.exit()

print searchInWords ('hewllo', t)

f = open('text.txt', 'r')

newW = []
tempL = []
#print f.read(1)
for line in f:
    #print line
    endLine = re.match(r'==next==$', line)
    if endLine != None:
        newW.append(tempL)
        tempL = []
        continue
    result = re.findall( r'\w+'  , line)
    for word in result:
        #print word
        if (searchInWords(word, newW) < 0):
            #print word
            tempL.append(word.lower())

newW.append(tempL)
f.close()

print newW

iterat = 0

for lib in newW:
    iterat += 1
    entering = 0
    for word in lib:
        if (searchInWords(word, t) >= 0):
            entering +=1
    print iterat
    print entering/float(len(lib)) * 100

#print entering/float(len(newW)) * 100
