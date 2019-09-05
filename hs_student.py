from student import *

class HighSchoolStudent(Student):

    school_name = "Milford High School"

    def get_school_name(self):
        return "School: " + self.school_name

    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + "-HS"