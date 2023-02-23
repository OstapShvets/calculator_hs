try:
    num1 = float(input("Please,type a number:"))
    num2 = float(input("Type another number:"))
except ValueError:
    print("It must be only numbers!")
    exit()

value_operator = input("Please, choose your option: \n1 '+' \n2 '-' \n3 '*' \n4 '**' \n5 '/'")

if value_operator in ['1', '2', '3', '4', '5']:
    result = None
    if value_operator == '1':
        result = num1 + num2
    elif value_operator == '2':
        result = num1 - num2
    elif value_operator == '3':
        result = num1 * num2
    elif value_operator == '4':
       try:

           if result > 20000:
             print("Result too large")
           else:
               result = num1 ** num2
       except NameError:
           print("Result too large")
       except TypeError:
           print("Error")
    elif value_operator == '5':
        try:
            if num2 == 0:
                print("It can be 0!")
            else:
                result = num1 / num2
                print(result)
        except:
            print("Error")
else:
    print("Only numbers from 1 to 5")
print(result)