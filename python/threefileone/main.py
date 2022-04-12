from printing import Printing

user = input("User name:")
side1 = input("triangle first side length (leg) (meter):")
side2 = input("triangle second side length (leg) (meter):")
side3 = input("triangle third side length (comprehensive) (meter):")

if side1.isnumeric() == False:
    print("Give me a number!")
else:
    side1int = float(side1)
if side2.isnumeric() == False:
    print("Give me a number!")
else:
    side2int = float(side2)    
if side3.isnumeric() == False:
    print("Give me a number!")
else:
    side3int = float(side3)

print = Printing(user, side1int, side2int, side3int)
print.print_metodh()