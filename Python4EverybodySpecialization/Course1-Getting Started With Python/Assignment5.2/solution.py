largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
    	inum=int(num)
    except:
        print('Invalid input')
    if largest == None :
        largest=inum
    elif inum > largest:
        largest=inum
    if smallest == None :
        smallest=inum
    elif inum < smallest :
        smallest=inum

print("Maximum is",largest)
print("Minimum is",smallest)
