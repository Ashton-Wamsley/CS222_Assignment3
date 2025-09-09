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
            searchFound = False
            for studentId, data in students.items():
                if data[0] == userSearch:
                    print(f"{studentId}, {data[0]}, {data[1]}, {data[2]}, {data[3]}")
                    searchFound = True
            if not searchFound:
                print(f"No student found with the last name of {userSearch}")

        elif userChoice == "2":
            userSearch = input("Enter major to search for: ")
            searchFound = False
            for studentId, data in students.items():
                if data[2] == userSearch:
                    print(f"{studentId}, {data[0]}, {data[1]}, {data[2]}, {data[3]}")
                    searchFound = True
            if not searchFound:
                print(f"No students found with the major of {userSearch}")
        
        elif userChoice == "3":
            print("Goodbye!")
            loop = False
        
        else:
            print("Invalid input try again")

studentInfoTool()
    
    