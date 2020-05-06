from Course import Course


class DataSheet:
    def __init__(self, courses: list):
        self.courses = courses

    def get_grades_as_list(self):
        return [course.grade for course in self.courses]

    def get_ects_as_list(self):
        return [course.ects for course in self.courses]

    def add_course(self, course: Course):
        self.courses.append(course)

    def __repr__(self):
        return "DataSheet(%r)" % (self.courses)
