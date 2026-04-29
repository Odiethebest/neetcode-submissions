import math

class AreaCalc:
    # TODO: Implement calculate method
    def __init__(self):
        pass
    
    def calculate(self, arg1: int, arg2: int = None):
        if arg2 == None:
            res = math.pi * arg1 ** 2
            return round(res, 2)
        else:
            res = arg1 * arg2
            return res

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))