
student = {
    "name": "Nayana",
    "roll_number": "41",
    "registration_number": "MES24MCA-2041",
    "department": "MCA",
    "semester": "1 st"
}
print("\n student list:\n",student)
total_marks=int(input("\nEnter the total marks;"))
student["total_mark"] =total_marks 
print("\n \n student list updated with adding totalmark:\n",student)

if student["total_mark"] >= 90:
    student["grade"] = "A"
elif student["total_mark"] >= 82:
    student["grade"] = "B"
elif student["total_mark"] >= 75:
    student["grade"] = "C"
elif student["total_mark"] >= 60:
    student["grade"] = "D"
elif student["total_mark"] >= 50:
    student["grade"] = "P"
else:
    student["grade"] = "F"
print("\n \n student list updated with adding grade:\n",student)



del student["roll_number"]

print("\n \n student list by removing delete roll number:\n",student)
