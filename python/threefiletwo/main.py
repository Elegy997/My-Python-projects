from printing import Printing

user =input("Give me your name!: ")
number =input("Give me the number!")

if number.isnumeric() == False:
    print("I need number!")
else:
    numberint = float(number)

    writeinfile = Printing(user, numberint)
    writeinfile.printing_metod()