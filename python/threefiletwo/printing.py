from os import write
from calculation import Calculation
import datetime

class Printing:
    def __init__(self, user, number):
        self.user = user
        self.number = number
    
    def printing_metod(self):
        calculate = Calculation(self.number)
        calculate.calculate(self.number)
        date = datetime.datetime.now().strftime("%Y/%m/%d")
        f = open("Bill_Adam.txt","w")
        f.write(f"Buyer name {self.user}")
        f.write("\n")
        f.write("CEO price")
        f.write(f"wage: {self.number} EUR")
        f.write("\n")
        f.write(f"Payable wage: {calculate.tax} EUR")
        f.write("\n")
        f.write(date)
        f.close()