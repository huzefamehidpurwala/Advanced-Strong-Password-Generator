# Advanced-Strong-Password-Generator
Python CLI Program for Random-Strong Password with advanced logics of exception handling concepts and libraries

```
from sys import argv
from random import choice
from string import ascii_letters, punctuation, digits
# from os import system


def makepass(x, pas="") -> str:
    assert x > 5, "Length of Password should be greater than 8"

    x = x - len(pas)

    while x != 0:
        i = choice(digits + ascii_letters + punctuation)

        # implement this logic accordingly to get formatted password
        # if (any(char in special_chars for char in pwd) and
        #         sum(char in digits for char in pwd) >= 2):
        #     break

        pas = i + pas
        x -= 1

    return pas


try:
    pas = makepass(int(argv[1]), argv[2])

except IndexError:
    # print("Please give the length of the password to generate in the CLI Command itself!")
    pas = makepass(int(input("How long the password should be: ")), input("Enter any keyword to add at the end: "))

except AssertionError as e:
    print(e)
    pas = makepass(int(input("How long the password should be: ")), argv[2])

except ValueError:
    # print("Please give an integral value for the length of the password to generate!")
    pas = makepass(int(input("How long the password should be: ")), argv[2])

# except Exception:
#     print("Some Error Occurred, Please try again later!")

print("Your password is:", pas)
# system('echo "' + pas + '" | clip')
input()
```
