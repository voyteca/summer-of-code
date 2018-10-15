"""Solution to Task 4 of Summer of Code"""

__author__      = "Wojciech Czubak"
__copyright__   = "Copyright 2018"

#PART 1 & 2
groups={} #dict of sets
ID=0
for l in open("06-friendships.txt"):
    friends=set(l.split()) #make set of friends
    isInGroup=[]
    for key,group in groups.items():
        if friends & group: #check if one of friends is already in any of the groups
            if len(isInGroup)==0:
                groups[key].update(friends) #if yes merge sets
            isInGroup.append(key) #record which group has a friend

    #if there is no record creat new group of friends
    if len(isInGroup)==0:
        groups[ID]=set(friends)
        ID+=1
    #or if a friends has been recorded more than once merge all these groups
    elif len(isInGroup)>1:
        for groupID in isInGroup[1:]:
            groups[isInGroup[0]]=groups[isInGroup[0]].union(groups[groupID])
            del groups[groupID]
     
print(len(groups))
print(max([len(group) for  group in groups.values()]))

