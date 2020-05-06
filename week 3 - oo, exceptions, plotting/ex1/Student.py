from DataSheet import DataSheet


class Student:
    # 4. In Student create init() so that a Student can be initiated with name, gender, data_sheet and image_url
    def __init__(self, name: str, gender: str, data_sheet: DataSheet, image_url: str):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url

    # 6. In student create a method: get_avg_grade()
    def get_avg_grade(self):
        grades = self.data_sheet.get_grades_as_list()
        sum = 0
        for grade in grades:
            sum += grade
        return sum / len(grades)

    def get_ects_progressions(self):
        ects_list = self.data_sheet.get_ects_as_list()
        sum = 0
        for ects in ects_list:
            sum += int(ects)
        return (100 / 150) * sum

    def __repr__(self):
        return "Student(%r,%r,%r,%r)" % (
            self.name,
            self.gender,
            self.data_sheet,
            self.image_url,
        )
