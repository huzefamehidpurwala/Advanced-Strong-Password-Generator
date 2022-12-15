# Advanced-Strong-Password-Generator
Python CLI Program for Random-Strong Password with advanced logics of exception handling concepts and libraries

```
from sys import argv                                    # to take length of the password from the user from the cli command itself
from random import choice                               # to select random elements from an iterable
from string import ascii_letters, punctuation, digits   # string of characters, special_chars and digits
from os import system
pas = 'aws'                                             # password should have these three characters in the sequece at last

try:
    x = int(argv[1]) - 3
    assert x > 5, "Length of Password should be greater than 8"

    while x != 0:
        i = choice(ascii_letters + punctuation + digits)

        # implement this logic accordingly to get formatted password
        # if (any(char in special_chars for char in pwd) and
        #         sum(char in digits for char in pwd) >= 2):
        #     break

        pas = i + pas                                   # concatenating random characters before the three characters required at last
        x -= 1

except IndexError:
    print("Please give the length of the password to generate in the CLI Command itself!")

except AssertionError as e:
    print(e)

except ValueError:
    print("Please give an integral value for the length of the password to generate!")

except Exception:
    print("Some Error Occurred, Please try again later!")

else:
    print("Your password is:", pas)
    system(f"echo '{pas}' | clip")                    # to copy the password automatically to clipboard
```
