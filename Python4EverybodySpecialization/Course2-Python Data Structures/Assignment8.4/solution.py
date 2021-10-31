fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    l=line.rstrip()
    w=l.split()
    for x in w:
        if x not in lst :
            lst.append(x)
lst.sort()
print(lst)
