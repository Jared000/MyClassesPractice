class OperationStrategy:
    def cal(self, a,b):
        pass 

class Sum(OperationStrategy):
    def cal(self,a,b):
        return a+b
    
class Minus(OperationStrategy):
    def cal(self, a, b):
        return a-b
    
class Multi(OperationStrategy):
    def cal(self, a, b):
        return a*b
    
class Calculator:
    def __init__(self, strategy):
        self.strategy = strategy
    
    def set_strategy(self, strategy):
        self.strategy = strategy

    def result(self, a,b):
        return self.strategy.cal(a,b)

obj = Calculator(Multi())

print(obj.result(8,3))
obj.set_strategy(Sum())

print(obj.result(2,9))