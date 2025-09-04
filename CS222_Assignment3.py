def studentInfoTool():
    students = {}

    try:
        with open('students.txt', 'r') as file:
            for line in file:
                parts = line.strip().split(' , ')
                if len(parts) == 5:
                    studentId, lastName, firstName, major, gpa = parts
                    students[studentId] = [lastName, firstName, major, gpa]
    except FileNotFoundError:
        print("Error File Not Found")
    
    