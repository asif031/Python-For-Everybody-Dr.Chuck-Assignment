hrs = input("Enter Hours:")
h = float(hrs)
rate=float(input("enter rate per hour"))
if h>40:
    pay=40*rate+(h-40)*1.5*rate
else:
	pay=h*rate
print(pay) 