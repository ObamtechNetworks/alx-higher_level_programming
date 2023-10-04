#!/usr/bin/python3
def fizzbuzz():
    fiz, buz, fbz = "Fizz", "Buzz", "FizzBuzz "
    for i in range(1, 101):
        print(
                "{}".format(
                    fbz if i % 15 == 0 else fiz if i % 3 == 0 else
                    buz if i % 5 == 0 else i),
                end=' ')
