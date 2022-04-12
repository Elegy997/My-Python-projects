from os import write
from calculation import Calculation
import datetime

class Printing:
    def __init__(self, user, side1, side2, side3):
        self.user = user
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def print_metodh(self):
        calculating = Calculation(self.side1, self.side2, self.side3)
        calculating.calculate(self.side1, self.side2, self.side3)
        date = datetime.datetime.now().strftime("%Y/%m/%d")
        f=open("Poul_Tom.txt", "w")
        f.write(f"Calculation page")
        f.write("\n")
        f.write(f"user name:")
        f.write("\n")
        f.write(f"a side: {self.side1} m")
        f.write("\n")
        f.write(f"b side: {self.side2} m")
        f.write("\n")
        f.write(f"c side: {self.side3} m")
        f.write("\n")
        f.write(f"perimeter: {calculating.perimeter} m")
        f.write("\n")
        f.write(f"area: {calculating.area} m2")
        f.write("\n")
        f.write("Created in: Miami,")
        f.write(date)
        f.close()