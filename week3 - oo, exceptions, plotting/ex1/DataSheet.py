from Course import Course


class DataSheet:
    def __init__(self, courses: list):
        self.courses = courses

    def get_grades_as_list(self):
        return [course.grade for course in self.courses]

    def __repr__(self):
        return "DataSheet(%r)" % (self.courses)
