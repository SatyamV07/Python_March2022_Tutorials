# print(0 / 0)
# print(0/0))


# print(dir(__builtins__))

print()

# print(int("ABC"))

# x = 10
# if x > 5:
#     raise Exception("x should not exceed 5. The value of x was: {}".format(x))

from ast import Assert
import sys

# assert "linux" in sys.platform, "this code runs only on Windows"


def windows_interaction():
    assert "win32" in sys.platform, "Function can only run on windows systems"
    print("Lets execute something")


# ======================================================
# try:
#     windows_interaction()

# except AssertionError as error:
#     print(error)
#     print("Windows function not executed")

print()
# ======================================================
# try:
#     with open("file.log") as file:
#         read_data = file.read()

# except FileNotFoundError as fnf_error:
#     print(fnf_error)
# #     # print("Could not open file.log")

# ======================================================
print()


# try:

#     windows_interaction()
#     with open("file.log") as file:
#         read_data = file.read()

# except FileNotFoundError as fnf_error:
#     print(fnf_error)

# except AssertionError as assertion_error:
#     print(assertion_error)
#     print("Windows windows_interation() function wasn't executed")
print()
# ======================================================

# try:
#     windows_interaction()

# except AssertionError as error:
#     print(error)

# else:
#     print("Executing the else clause")
# ======================================================

print()

# try:
#     windows_interaction()

# except AssertionError as error:
#     print(error)

# else:
#     try:
#         with open("file.log") as file:
#             read_data = file.read()

#     except FileNotFoundError as fnf_error:
#         print(fnf_error)

# ======================================================

print()

try:
    windows_interaction()

except AssertionError as error:
    print(error)

else:
    try:
        with open("file.log") as file:
            read_data = file.read()

    except FileNotFoundError as fnf_error:
        print(fnf_error)

finally:
    print("Cleaning up everything irrespective of any exceptions")
