n = 24


def fizzBuzz(n):
    if n % 5 == 0 and n % 3 == 0:
        print("fizzBuzz")
    elif n % 3 == 0:
        print("fizz")
    elif n % 5 == 0:
        print("Buzz")


fizzBuzz(n)
