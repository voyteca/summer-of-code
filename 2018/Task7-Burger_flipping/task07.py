
"""Solution to Task 7 of Summer of Code 2018"""

__author__      = "Wojciech Czubak"
__copyright__   = "Copyright 2018"

#PART 1 & 2

data=[l.split() for l in open("07-flips.txt")]
sorters=set()

for instructions in data[1:]:
    #make burger list of lists, with boolean for the flip state
    burgers=[[burger,True] for burger in data[0][1:]]
    for inst in instructions[1:]:
        i=int(inst)
        burgers=burgers[:i][::-1]+burgers[i:] #rotate burgers        
        for s in range(i):burgers[s][1]=not burgers[s][1] #flip burgers

    #check if sorted   
    if  all(int(burgers[i][0]) <= int(burgers[i+1][0]) for i in range(len(burgers)-1)):
        sorters.add(instructions[0])
        
        if all(b[1] for b in burgers): #check if all are flipped back
            print ('best sorter:',instructions[0])
    
print ('number of working sorters:',len(sorters))


