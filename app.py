from displays import CalculatorDisplays
from simple_calculator import SimpleCalculator

simple_cal_desc  = ''' calculator to handle simple calculation for addition, subtraction, division, multiplication of two numbers'''
advanced_calculator = ''' calculator to handle advanced calculation for addition, subtraction, division, multiplication calculation excluding the sin,cos,tan attributes but exceeding  two numbers'''

msg = "welcome to calculator"
exit_msg = "thank you for using our application"

# app starting 
print(msg)
# listing calculator types
(CalculatorDisplays).cal_type()