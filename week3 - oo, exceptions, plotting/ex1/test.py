from random import choice, randint
from DataSheet import DataSheet
from Course import Course
from Student import Student

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
    for i in range(0, 3):
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
            "stud_name, course_name, teacher, ects, classroom, grade, img_url\n"
        )
        for s in students:
            for c in s.data_sheet.courses:
                csv_file.write(
                    "{sname},{cname},{teacher},{ects},{classroom},{grade},{img}\n".format(
                        sname=s.name,
                        cname=c.name,
                        teacher=c.teacher,
                        ects=c.ects,
                        classroom=c.classroom,
                        grade=c.grade,
                        img=s.image_url,
                    )
                )


# write_students()
students = generate_students()
print(students[0])
print(students[0].get_avg_grade())

