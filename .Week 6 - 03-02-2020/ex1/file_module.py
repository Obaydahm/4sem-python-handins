import sys
import csv
import argparse

parser = argparse.ArgumentParser(description="Read CSV file")
parser.add_argument(
    "-pf", "--printfile", metavar="", required=True, help="Prints file content"
)

args = parser.parse_args()

# 1.A. def print_file_content(file) that can print content of a csv file to the console
def print_file_content(file):
    with open(file) as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        for row in reader:
            print(",".join(row))


# 1.B. def write_list_to_file(output_file, lst) that can take a list of tuple and write each element to a new line in file
# 1.B.a rewrite the function so that it gets an arbitrary number of strings instead of a list
def write_list_to_file(output_file, *args):
    with open(output_file, "w") as csv_file:
        for e in args:
            csv_file.write(e + "\n")
    print_file_content(output_file)


# 1.C def read_csv(input_file) that take a csv file and read each row into a list
def read_csv(input_file):
    csv_content = []
    with open(input_file) as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            csv_content.append(",".join(row))
    print(csv_content)


if __name__ == "__main__":
    print_file_content(args.printfile)
    # print_file_content("test.csv")
    # write_list_to_file("b.csv", "hej", "med", "dig", "bro")
    # read_csv("b.csv")
