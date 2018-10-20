##counter=0
##for l in open("01-mowmaster.txt"):
##    if not l.startswith("#"):
##        counter+=1
##
##print(counter)

##count=len([l for l in open("01-mowmaster.txt") if not l.startswith("#")])
#print(len([l for l in open("01-mowmaster.txt") if not l.startswith("#")]))

##mx=1
##my=x=y=0
##
##for l in open("01-mowmaster.txt"):
##    mxTemp=mx
##    if l[0]=="C":       
##        mx=0 if abs(mx)==1 else 1 if my==1 else -1
##        my=0 if abs(my)==1 else -1 if mxTemp==1 else 1
##    elif l[0]=="A":
##        dxTemp=mx
##        mx=0 if abs(mx)==1 else -1 if my==1 else 1
##        my=0 if abs(my)==1 else 1 if mxTemp==1 else -1
##
##    elif l[0]=="F":
##        x+=int(l[1:])*mx
##        y+=int(l[1:])*my
##
##print(abs(x)+abs(y))

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
