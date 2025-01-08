class Student:
    def __init__(self):
        
        self.MCAS1 = []
        self.MCAS3 = []

    def add_student_to_mcas1(self, student_name, position=3):
        
        if position <= len(self.MCAS1):
            self.MCAS1.insert(position - 1, student_name)
        else:
            
            self.MCAS1.append(student_name)

    def search_student_in_mcas1(self, student_name):
        
        if student_name in self.MCAS1:
            return f"Student {student_name} found in MCAS1."
        else:
            return f"Student {student_name} not found in MCAS1."

    def merge_and_display_students(self):
        
        all_students = self.MCAS1 + self.MCAS3
        return "All students in MCA: " + ", ".join(all_students)


student_class = Student()
student_class.MCAS1 = ["Alice", "Bob", "Charlie"]
student_class.MCAS3 = ["David", "Eva", "Frank"]


student_class.add_student_to_mcas1("Grace", 3)


search_result = student_class.search_student_in_mcas1("Grace")


merged_students = student_class.merge_and_display_students()


print(search_result)
print(merged_students)
