fname = input("Enter file name: ")
fh = open(fname)
tot=0
count=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    s=line.find(':')
    val=line[s+1:]
    fval=float(val)
    count=count+1
    tot=tot+fval

print('Average spam confidence:',tot/count)
