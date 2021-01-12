for number in range (1, 100):
    if (number / 3) == 1:
        print("Fizz")
    elif (number /5) == 1:
        print("Buzz")
    elif (number/3) == 1 and (number/5) == 1:
        print("FizzBuzz")
    else:
        print(number)