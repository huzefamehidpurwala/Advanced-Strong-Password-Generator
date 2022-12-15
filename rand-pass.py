from sys import argv
from random import choice
from string import ascii_letters, punctuation, digits
# from os import system
pas = 'aws'

try:
    x = int(argv[1]) - 3
    assert x > 5, "Length of Password should be greater than 8"

    while x != 0:
        i = choice(ascii_letters + punctuation + digits)

        # implement this logic accordingly to get formatted password
        # if (any(char in special_chars for char in pwd) and
        #         sum(char in digits for char in pwd) >= 2):
        #     break

        pas = i + pas
        x -= 1

except IndexError:
    print("Please give the length of the password to generate in the CLI Command itself!")

except AssertionError as e:
    print(e)

except ValueError:
    print("Please give an integral value for the length of the password to generate!")

# except Exception:
#     print("Some Error Occurred, Please try again later!")

else:
    print("Your password is:", pas)
    # system(f"echo '{pas}' | clip")
    input()
