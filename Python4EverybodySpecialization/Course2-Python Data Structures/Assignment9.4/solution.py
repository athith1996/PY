name = "mbox-short.txt"
handle = open(name)
x=dict()
for line in handle:
    if line.startswith('From '):
        words=line.split()
        x[words[1]]=x.get(words[1],0)+1

bigcount=0
bigmail=0
for mail,count in x.items() :
    if count is None or count > bigcount :
        bigcount=count
        bigmail=mail
print(bigmail,bigcount)
