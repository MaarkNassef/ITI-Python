x = 9
i = 1
while i < x:
    if i**2 == x:
        print("It has a square root.")
        break
    else:
        i+=1

if i == x:
    print("It doesn't have a square root.")