while True:
    try:
        num1 = int(input("Enter a number: "))
        if num1 == 9:
            raise FileNotFoundError
        num2 = int(input("Enter another number: "))
        print(f'{num1} ÷ {num2} = {num1 / num2}')
    except ValueError:
        print("Please enter a number")
    except ZeroDivisionError:
        print("You divided by 0")
    except FileNotFoundError:
        print("We don't like the number 9 here")
    except:
        print('this hsouldn"t happen')