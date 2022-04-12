class Calculation:
    def __init__(self, number):
        self.number = number
        self.tax = 0

    def calculate(self, number):
        self.tax = number * 0.8
