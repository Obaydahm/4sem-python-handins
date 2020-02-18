class Course:
    """
  """

    # 3. Each course has name, classroom, teacher, ETCS and optional grade if course is taken.
    def __init__(self, name, classroom, teacher, ects, grade=None):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ects = ects
        self.grade = grade

    def __repr__(self):
        return "Course(%r, %r, %r,%r,%r)" % (
            self.name,
            self.classroom,
            self.teacher,
            self.ects,
            self.grade,
        )

    def __str__(self):
        return "The course {name} takes place in classroom {room} with Mr. {teacher}.\nThe course consists of {ects} ETCS, and the grade given was {grade}.".format(
            name=self.name,
            room=self.classroom,
            teacher=self.teacher,
            ects=self.ects,
            grade=self.grade,
        )

