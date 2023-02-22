try:
    value_float_1 = float(input("Please type a number: "))
    value_float_2 = float(input("Please type another number: "))
except ValueError:
    print("It must be only numbers")
    exit()

value_operator = input("Please choose operator:\n 1 '+'\n 2 '-'\n 3 '*'\n 4 ''\n 5 '/'\nYour answer: ")

if value_operator in ['1', '2', '3', '4', '5']:
    if value_operator == '1':
        result = value_float_1 + value_float_2
    elif value_operator == '2':
        result = value_float_1 - value_float_2
    elif value_operator == '3':
        result = value_float_1 * value_float_2
    elif value_operator == '4':
        result = value_float_1 / value_float_2
    elif value_operator == "5":
        try:
            if value_float_2 == 0:
                print("It can not be 0")
            else:
                result = value_float_1 / value_float_2
        except:
            print("Error")
else:
    print("It can be only 1,2,3,4 and 5")
    result = None

if result is not None:
    print(result)
