student = {
    "name": "Nayana",
    "roll_number": "41",
    "registration_number": "MES24MCA-2041",
    "department": "MCA",
    "semester": "1 st"
}
student["total_mark"] = 80 

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
print(student)

print()

del student["roll_number"]

print(student)
