rotation={'C':{0:1,1:2,2:3,3:0},'A':{0:3,1:0,2:1,3:2}}
directions=[[1,0],[0,-1],[-1,0],[0,1]]
direction=3
graffiti=set()
bladeDown=False

x=y=maxX=maxY=0
for l in open("03-graffiti.txt"):
    if l[0]=='F':
        if bladeDown:
            for i in range(1,int(l[1:])+1):
                x+=directions[direction][0]
                y+=directions[direction][1]
                graffiti.add(str(x)+','+str(y))
        else:
            x+=int(l[1:])*directions[direction][0]
            y+=int(l[1:])*directions[direction][1]

        if maxX<x:maxX=x
        if maxY<y:maxY=y
    elif l[0]=='D':
        bladeDown=True
        graffiti.add(str(x)+','+str(y))
    elif l[0]=='U':
        bladeDown=False
    elif l[0]!="#":
        direction=rotation[l[0]][direction]

print(len(graffiti))

# PRINT MESSAGE (PART 2)
x=0
y=maxY
row=''
while y>=0:
    while x<=maxX:
        if str(x)+','+str(y) in graffiti:
            row+='*'
        else:
            row+=' '
        x+=1
  
    print(row)
    x=0
    y-=1
    row=''

