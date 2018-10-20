
##f=open("02-rainfall.txt")
##records=[]
##record=int(f.readline())
##while record<9999:
##    records.append(record)
##    record=int(f.readline())
##
##count=len(records)
##print(count ,round(sum(records)/count))

f=open("02-rainfall.txt")
record=int(f.readline())
acumulator=0
count=0
while record<9999:
    count+=1
    acumulator+=record
    record=int(f.readline())

print(count ,round(acumulator/count))
