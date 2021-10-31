name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
count=dict()
for line in handle :
    if line.startswith('From '):
        words=line.split()
        hour=words[5].split(':')
        count[hour[0]]=count.get(hour[0],0)+1
for k,v in sorted(count.items()):
    print(k,v)
