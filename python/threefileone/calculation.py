class Calculation:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.perimeter = 0
        self.area = 0

    def calculate(self, side1, side2, side3):
        self.perimeter = side1 + side2 + side3
        self.area = side1 * side2