"""Solution to Task 5 of Summer of Code"""

__author__      = "Wojciech Czubak"
__copyright__   = "Copyright 2018"

import re #regular expression module

#PART 1 & 2

def expand(line):
    i=line.find(':')
    while i>-1:
        replacement=getReplacement(line,i)
        line=line.replace(replacement[0],replacement[1],1)
        i=line.find(':')
    return line

def getReplacement(line,codeStart):
    replaceSub=line[codeStart:line.find(':',line.find(':',codeStart+1)+1)+1]
    if replaceSub=='':return
    codeList=replaceSub[1:].split(':')
    chQty=int(codeList[0])
    repeat=int(codeList[1])-1
    replaceWith=line[codeStart-chQty:codeStart]*repeat
    replacement=[replaceSub,replaceWith]   
    return replacement

charsCompressed=0
charsUncompressed=0
for l in open("05-instructions.txt"):
    line=re.sub('<[^>]*>','',l)
    charsCompressed+=len(re.sub('\s','',line))
    charsUncompressed+=len(re.sub('\s','',expand(line)))
    
print(charsCompressed,charsUncompressed)
