from os.path import join
import os

path = join(os.getcwd(), r"Day10\File_handling")
os.chdir(path)


file1 = open("log1.txt", "r")
print(file1.read())
file1.close()

# file1 = open(path + "\log.txt", "r")
# print(file1.read())
file2 = open("log2.txt", "w")
file2.writelines(
    """
file with write attribute
first line
second line
third line"""
)
file2.close()


file3 = open("log2.txt", "a")
file3.writelines(
    """
forth line
fifth line
sixth line"""
)
file3.close()

# With context manager

with open("log1.txt", "r") as file1:
    print(file1.readlines())
    file1.seek(0)
    print(file1.read())

with open("log1.txt", "r") as file1, open("log4.txt", "w") as file2:
    contents = file1.read()
    file2.writelines(contents)
