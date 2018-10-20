"""Solution to Task 1 of Summer of Code 2018"""

__author__      = "Wojciech Czubak"
__copyright__   = "Copyright 2018"

# PART 1
print(len([l for l in open("01-mowmaster.txt") if not l.startswith("#")]))

# PART 2
rotation={'C':{0:1,1:2,2:3,3:0},'A':{0:3,1:0,2:1,3:2}}
directions=[[1,0],[0,-1],[-1,0],[0,1]]
direction=0
x=y=0
for l in open("01-mowmaster.txt"):
    if l[0]=='F':
        x+=int(l[1:])*directions[direction][0]
        y+=int(l[1:])*directions[direction][1]
    elif l[0]!="#":
        direction=rotation[l[0]][direction]
                           
print(abs(x)+abs(y))
