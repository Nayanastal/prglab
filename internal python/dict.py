def sort_students_descending():
    student = {}
    
    # Number of students to enter
    num_students = int(input("Enter the number of students: "))
    
    # Accept student name and marks as key-value pairs
    for _ in range(num_students):
        name = input("Enter student's name: ")
        marks = float(input(f"Enter marks for {name}: "))
        student[name] = marks
    
    # Sort the dictionary by student name in descending order
    sorted_student = dict(sorted(student.items(), key=lambda item: item[0], reverse=True))
    
    # Display the sorted dictionary
    print("\nSorted list of students (in descending order by name):")
    for name, marks in sorted_student.items():
        print(f"{name}: {marks}")

# Call the function to execute
sort_students_descending()
