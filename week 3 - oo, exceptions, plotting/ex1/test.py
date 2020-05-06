from random import choice, randint
import matplotlib.pyplot as plt
from DataSheet import DataSheet
from Course import Course
from Student import Student
import csv

# Create a function that can generate n number of students with random: name, gender, courses (from a fixed list of course names), grades, img_url

male_names = ["Peter", "William", "George", "Hassan", "Phil"]
female_names = ["Jane", "Wendy", "Amanda", "Julie"]
teachers = ["Anthony", "Adam", "Andrew", "Yesam", "Michael"]
genders = ["male", "female"]
courses_names = ["Science", "Math", "Research", "Software", "Business"]
classrooms = [200, 201, 202, 203, 204, 205, 206, 207]
ects = [5, 10, 15, 20, 25, 30]
grades = [-3, 0, 2, 4, 7, 10, 12]

# 7. Create a function that can generate n number of students with random: name, gender, courses (from a fixed list of course names), grades, img_url
def generate_students():
    students = []
    for i in range(0, 5):
        courses = []
        for j in range(0, 4):
            courses.append(
                Course(
                    choice(courses_names),
                    choice(classrooms),
                    choice(teachers),
                    choice(ects),
                    choice(grades),
                )
            )
        gender = choice(genders)
        name = None
        if gender is "male":
            name = choice(male_names)
        else:
            name = choice(female_names)
        students.append(Student(name, gender, DataSheet(courses), "picture.com"))
    return students


# 7A. Let the function write the result to a csv file with format stud_name, course_name, teacher, ects, classroom, grade, img_url
def write_students():
    students = generate_students()
    with open("students.csv", "w") as csv_file:
        csv_file.write(
            "stud_name, gender, course_name, teacher, ects, classroom, grade, img_url\n"
        )
        for s in students:
            for c in s.data_sheet.courses:
                csv_file.write(
                    "{sname},{gender},{cname},{teacher},{ects},{classroom},{grade},{img}\n".format(
                        sname=s.name,
                        gender=s.gender,
                        cname=c.name,
                        teacher=c.teacher,
                        ects=c.ects,
                        classroom=c.classroom,
                        grade=c.grade,
                        img=s.image_url,
                    )
                )


# 8. Read student data into a list of Students from a csv file:
def read_students():
    students = []
    with open("students.csv", "r") as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        headers = next(reader)
        for row in reader:
            student_exists = False
            for student in students:
                if row[0] == student.name:
                    student.data_sheet.add_course(
                        Course(row[2], row[5], row[3], row[4], int(row[6]))
                    )
                    student_exists = True
            if not student_exists:
                data_sheet = DataSheet(
                    [Course(row[2], row[5], row[3], row[4], int(row[6]))]
                )
                students.append(Student(row[0], row[1], data_sheet, row[7]))

    # A. loop through the list and print each student with name, img_url and avg_grade.
    for student in students:
        print(
            "Student:",
            student.name,
            "\nAvg grade:",
            student.get_avg_grade(),
            "\n Img:",
            student.image_url,
            "\n\n",
        )

    # B. sort the list by avg_grade
    students.sort(key=lambda x: x.get_avg_grade(), reverse=True)
    print("Sorted:")
    for student in students:
        print(
            "Student:",
            student.name,
            "\nAvg grade:",
            student.get_avg_grade(),
            "\n Img:",
            student.image_url,
            "\n\n",
        )
    return students


# create a bar chart with student_name on x and avg_grade on y-axis
def draw_barplot():
    students = read_students()
    x_names = [s.name for s in students]
    y_avg_grade = [s.get_avg_grade() for s in students]

    plt.bar(x_names, y_avg_grade)

    plt.title("Students and grades")
    plt.xlabel("Students")
    plt.ylabel("Average grades")

    plt.tight_layout()
    plt.show()


# 9. ake a method on Student class that can show progression of the study in % (add up ECTS from all passed courses divided by total of 150 total points (equivalent to 5 semesters))
def ects_progression():
    students = read_students()
    for student in students:
        print(
            "Student:",
            student.name,
            "- ECTS completion:",
            round(student.get_ects_progressions()),
            "%",
        )


ects_progression()
# write_students()
# draw_barplot()
# read_students()
# students = generate_students()
# print(students[0])
# print(students[0].get_avg_grade())

