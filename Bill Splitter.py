#This is the python code to make a simple bill splitter...

#Print startup message...

print("Thank You for visiting us!")
print("If you're a group then you can use our bill splitter service to split your bills equally.")

#Ask the user to give inputs...

a = float(input("Total Amount to be paid : "))

b = int(input("Total No. of people at party : "))

c = (round(float( a / b),1))

print("Cost per person: $",c)