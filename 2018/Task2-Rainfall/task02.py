
"""Solution to Task 2 of Summer of Code 2018"""

__author__      = "Wojciech Czubak"
__copyright__   = "Copyright 2018"

f=open("02-rainfall.txt")
record=int(f.readline())
acumulator=0
count=0
while record<9999:
    count+=1
    acumulator+=record
    record=int(f.readline())

print(count ,round(acumulator/count))
