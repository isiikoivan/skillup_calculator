class SimpleCalculator:
    
    def __init__(self, num1=0, num2=0):
        self.num1 = num1
        self.num2 = num2

    def addition_print(self):
        print(self.num1 + self.num2)
    
    
    
    def subtraction_print(self):
        print(self.num1-self.num2)
        
        
    def division_print(self):
        print(self.num1 / self.num2)    
    
    
    def multiplication_print(self):
        print(self.num1*self.num2 )
    
# # Example usage:
# calculator = SimpleCalculator(5, 3)
# calculator.addition_print()