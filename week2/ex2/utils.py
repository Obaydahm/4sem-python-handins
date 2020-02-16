from os import listdir
from os.path import isfile, isdir, join

"""
Exercise 2
Create a module called utils.py and put the following functions inside:
"""
# first function takes a path to a folder and writes all filenames in the folder to a specified output file
def func_1(path):
    filesInPath = [file for file in listdir(path) if isfile(join(path, file))]
    with open("./ex2/outputfiles/func1_output.txt", "w") as outputfile:
        for file in filesInPath:
            outputfile.write(file + "\n")


# second takes a path to a folder and write all filenames recursively (files of all sub folders to)
def func_2(path):
    listOfFiles = listdir(path)
    allFiles = list()
    for entry in listOfFiles:
        fullPath = join(path, entry)
        if isdir(fullPath):
            allFiles.append((entry, func_2(fullPath)))
        else:
            allFiles.append(entry)
    return allFiles


# third takes a list of filenames and print the first line of each
def func_3(*files):
    for file in files:
        with open(file) as f:
            print(f.readline().strip())


# fourth takes a list of filenames and print each line that contains an email (just look for @)
def func_4(*files):
    for file in files:
        with open(file) as f:
            for line in f.readlines():
                if "@" in line:
                    print(line)


# fifth takes a list of md files and writes all headlines (lines starting with #) to a file
# Make sure your module can be called both from cli and imported to another module
# Create a new module that imports utils.py and test each function.


def func_5(*files):
    for file in files:
        with open(file) as f:
            for line in f.readlines():
                if line.startswith("#"):
                    print(line.strip("#"))


if __name__ == "__main__":
    # func_1("./ex1")
    # print(func_2("."), "\n\n")
    # func_3("./test.txt", "./test2.txt")
    # func_4("./test.txt", "./test2.txt")
    func_5("./test.md", "./test2.md")
