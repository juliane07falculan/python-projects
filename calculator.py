def addition(addend1, addend2):
    print(addend1 + addend2) 
def subtraction(minuend, subtrahend):
    print(minuend - subtrahend) 
def multiplication(factor1, factor2):
    print(factor1 * factor2) 
def division(dividend, divisor):
    print(dividend / divisor) 

def computation():
    print('a - addition | b - subtraction | c - multiplication | d - division')
    first_number = int(input('first_number: '))
    second_number = int(input('second_number: '))
    select_operation = input('operation: ').lower()
    if select_operation == 'a':
        addition(first_number, second_number)
    elif select_operation == 'b':
        subtraction(first_number, second_number)
    elif select_operation == 'c':
        subtraction(first_number, second_number)
    elif select_operation == 'd':
        subtraction(first_number, second_number)
    else:
        print('Thank you, bye!')
  
computation()