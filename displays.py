from simple_calculator import SimpleCalculator
class CalculatorDisplays (SimpleCalculator):

    # declarations
     global calculator_type
     global calculator_action
     global math_symbols
     global new_str
    # app declarations
     calculator_action = ['addition','subtraction','multiplication','division','clear','exit']
     calculator_type =  ['simple calculator','advanced calculator']
     math_symbols =['+','-','*','/']

    # displaying cal types
     def cal_type():
        i=1
        for cal_type in  calculator_type:
            print( str(i) + " ) "+cal_type)
            i = i+1
        
        # taking input calculator type
        cal_type_input = input('Choose Calculator Type you wish to proceed with : \n ')
        if int(cal_type_input) == 1:
            print('\n')
            (CalculatorDisplays).cal_action()   
            print('\n')
            
        elif int(cal_type_input) == 2:
           print('Advance Not Set yet')
           print('\n')
           advance_input = input("Enter combination to be calculated eg (2 + 3 * 8 - 1) : \n")
           in_data = advance_input.replace(" ", "")
           print(in_data)

            # Define math symbols to search for
           math_symbols = ['+', '-', '*', '/']

            # Loop through each math symbol
           for mtc_sym in math_symbols:
                    print(mtc_sym)
                    print(in_data)
                    symbol_index = in_data.find(mtc_sym)
                    print(symbol_index)

                    if symbol_index != -1:  # Check if the symbol is found
                        # Create a new string with spaces around the symbol
                        new_sign = " " + mtc_sym + " "
                        new_str = in_data.replace(mtc_sym, new_sign)
                        in_data = new_str  # Update in_data for next iteration or to be returned
                        print(new_str)

                    print(in_data)  # Print the final modified string

            # spaces on the other hands
            # print(right_hand_item)
            # print(left_hand_item)
            # print(new_concat_str)
            # print(new_str)
            
            
            # replace component at a given index
            
            
            
            # padding at that point
            # print('air')
            # print(" ".join(in_data[add_symbol]))
           
            # print('\n')
            # # print(in_data)
            
            # # print(add_symbol )
            # print('\n')
            # # print(new_concat_str)
            # print('\n')
            # print(right_hand_item)
            # print('\n')
            # print(left_hand_item)
           (CalculatorDisplays).advance_calculator(advance_input)
           print('\n')
            

        else:
            print('\n')
            print("UNKOWN REQUEST")        
            print('\n')
            (CalculatorDisplays).cal_type()

     def cal_action():
            i =1
            for cal_action in calculator_action:
                print(str(i)+ " ) " + cal_action)
                i= i+1
            choosen_item =  int(input('Select action to execute : \n'))
            (CalculatorDisplays).input_detatils(choosen_item)
            print('\n')
        
     def input_detatils(action_in):
        simp_cal = SimpleCalculator()
        simp_cal.num1=int(input('Enter first number : '))
        simp_cal.num2 = int(input('Enter second number : '))   
        if action_in == 1:
            simp_cal.addition_print()
        elif action_in == 2:
            simp_cal.subtraction_print()
        elif action_in == 3:
            simp_cal.multiplication_print()
        elif action_in ==4:
            simp_cal.division_print()
        elif action_in == 5:
            simp_cal.num2 = 0
            simp_cal.num1 =0
            print('Function Not Set Yet')
            (CalculatorDisplays).cal_action()
        elif action_in==6:
            simp_cal.num2 = 0
            simp_cal.num1 =0
            print('Function Not Set Yet')
            (CalculatorDisplays).cal_type()
        else:
            print('invalid input pliz')
            (CalculatorDisplays).cal_action()
            
            
     def advance_calculator(text_input):
         print('advance calculator starting ')
         (CalculatorDisplays).cal_type()

         