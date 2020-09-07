largest = None
smallest = None
while True:
    numb=input("Enter a number: ")
    if numb == "done" :
        break
    try:
        num = int(numb)
        if largest is None:
            largest=num
        else:
            if num>largest:
                largest=num
        if smallest is None:
            smallest=num
        else:
            if num<smallest:
                smallest=num
    except :
        print("Invalid input")
    

print("Maximum is", largest)
print("Minimum is", smallest)