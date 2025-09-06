def studentInfoTool():
    students = {}

    try:
        with open('students.txt', 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 5:
                    studentId, lastName, firstName, major, gpa = parts
                    students[studentId] = [lastName, firstName, major, gpa]
    except FileNotFoundError:
        print("Error File Not Found")
        return
    
    print("Choose an option:\n1) Search by last name\n2) Search by major\n3) Quit\n")
    loop = True
    while loop == True:    
        userChoice = input("Enter: ")
        if userChoice == "1":
            userSearch = input("Enter last name to search for: ")
            print(students[userSearch])
        elif userChoice == "2":
            userSearch = input("Enter major to search for: ")
            print(students[major])
        elif userChoice == "3":
            print("Goodbye!")
            loop = False
        else:
            print("Invalid input try again")

studentInfoTool()
    
    