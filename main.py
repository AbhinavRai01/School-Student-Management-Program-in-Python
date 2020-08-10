while True:
    print("Enter:")
    print("1 : Add student")
    print("2 : View student")
    try:
        addorview = int(input())
    except:
        print('Enter a valid number')
        continue

    if addorview == 1 or addorview == 2:
        break
    else:
        print("Enter a valid number")
        continue

if addorview == 1:
    number = open("number.txt", "r")
    serial = int(number.readline())
    number.close()
    print("Serial number = ", serial)
    name = input("Enter name : ")
    while True:
        try:
            roll = int(input("Enter roll number : "))
            break
        except:
            print("Enter valid roll number")
            continue
    while True:
        dob = input("Enter date of birth(DD/MM/YYYY) : ")
        if dob[0:1].isnumeric() and dob[2] == "/" and dob[3:4].isnumeric() and dob[5] == "/" and dob[6:7].isnumeric() and len(dob)==8:
            break
        else:
            print("Invalid Input")
            continue

    while True:
        admin = input("Enter admission number : ")
        if admin[0:2].isnumeric() and admin[3] == "/" and admin[4:5].isnumeric() and len(admin) == 6:
            break
        else:
            print("Invalid Input")
            continue

    classs = input("Enter class : ")
    sec = input("Enter section : ")

    filename = str(serial) + ".txt"
    student = open(filename, "a")

    student.write(name + "\n")
    student.write(str(roll) + "\n")
    student.write(dob + "\n")
    student.write(admin + "\n")
    student.write(classs + "\n")
    student.write(sec + "\n")

    student.close()

    numberr = open("number.txt", "w")
    serial1 = serial + 1
    numberr.write(str(serial1))
    numberr.close()

    print("Student added successfully")

else:
    print("Enter")
    print("1 : Search by serial number")
    print("2 : Search by name")
    print("3 : Search by class and section")
    while True:
        try:
            search = int(input())
            if search == 1 or search == 2 or search == 3:
                break
            else:
                print("Invalid input")
                continue
        except:
            print("Invalid input")
            continue

    if search == 1:
        import os.path

        serial = input("Enter serial number")
        file = serial + ".txt"
        if os.path.isfile(file):
            f = open(file, "r")
            print("Name :", f.readline(), "Roll :", f.readline(), "Date of Birth :", f.readline(), "Admin number :",
                  f.readline(), "Class :", f.readline(), "Section :", f.readline())
            f.close()

        print("Search complete")

    elif search == 2:
        name = input("Enter Name")
        length = len(name)
        num = open("number.txt", "r")
        s = int(num.readline())
        num.close()
        n = 0

        while n < s:
            file = str(n) + ".txt"
            f = open(file, "r")
            nam = f.readline()
            namme = (nam[0:length])

            n += 1
            if name == namme:
                print("Name :", nam, "Roll :", f.readline(), "Date of Birth :", f.readline(), "Admin number :",
                      f.readline(), "Class :", f.readline(), "Section :", f.readline())
                f.close()
                print("")

        print("Search complete")

    else:
        while True:
            classec = input("Enter class and section(Eg.9c)")
            if classec[0].isnumeric() and classec[1].isalpha():
                break
            else:
                print("Invalid Input")
                continue
        classs = classec[0]
        sec = classec[1]

        num = open("number.txt", "r")
        s = int(num.readline())
        num.close()
        n = 0

        while n < s:
            file = str(n) + ".txt"
            f = open(file, "r")

            name = f.readline()
            roll = f.readline()
            dob = f.readline()
            admin = f.readline()
            class_ = f.readline()[0]
            sec_ = (f.readline())[0]

            n += 1
            if class_ == classs and sec_ == sec:
                print("Name : ", name, "Roll : ", roll, "Date of Birth : ", dob, "Admin number : ", admin, "Class : ",
                      class_)
                print("Section :", sec_)
                print("")
        print("Search complete")
q = input()
