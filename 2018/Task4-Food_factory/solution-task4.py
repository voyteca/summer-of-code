"""Solution to Task 4 of Summer of Code 2018"""

__author__      = "Wojciech Czubak"
__copyright__   = "Copyright 2018"

#PART 1
from functools import reduce
print(reduce((lambda t, itemTime:t+itemTime),[int(l.split()[1]) for l in open("04-preparation.txt")]))

#PART 2
tasks={}
tasksTimes={}

def getTaskTime(task):
    dTime=0
    if task in tasksTimes:
        return tasksTimes[task]
    tasksTimes[task]=int(tasks[task][0])
    for dependsOn in tasks[task][1:]:
        dependsOnTime=getTaskTime(dependsOn)        
        if dependsOnTime>dTime: dTime=dependsOnTime
    tasksTimes[task]+=dTime
    return  tasksTimes[task]

for l in open("04-preparation.txt"):
    taskAsList=l.strip().split()
    tasks[taskAsList[0]]=taskAsList[1:]

for task in tasks.keys():
    getTaskTime(task)

print(max(tasksTimes.values()))
