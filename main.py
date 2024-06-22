import uuid
import csv
import os
from student import Student


def getStudents() -> None:
    searchby = input(
        "What are you searching by?\noptions: firstname - lastname - dob - gender "
    )


def createstudent():
    first = input("Enter first name: ")
    last = input("Enter last name: ")
    dOb = input("Enter date of birth: ")
    gender = input("Enter gender: ")
    addy = input("Enter address: ")
    ph_num = input("Enter phone number: ")
    email = input("Enter email: ")
    new_student = Student(first, last, dOb, gender, addy, ph_num, email)
    studentlist.append(new_student)
    print("student created: " + str(first + " " + last) + "\n")
    with open("studentList.csv", mode="a", newline="") as fin:
        csvout = csv.writer(fin)
        csvout.writerow(
            [
                new_student.f_name,
                new_student.l_name,
                new_student.date_of_birth,
                new_student.gender,
                new_student.address,
                new_student.phone_number,
                new_student.email,
                new_student.id,
            ]
        )
    fin.close()


def printlist(list):
    for student in list:
        print(str(student) + "\n")


# import csv
# import os


def deleteByIdOrName(students_list):
    try:
        orig_file = "studentList.csv"
        temp_file = "temp_file.csv"

        value = input("Enter last name or student ID to remove. ctrl+c to go back: ")

        to_remove = [
            p for p in students_list if value == str(p.id) or value == str(p.l_name)
        ]

        for p in to_remove:
            print("removed " + p.f_name + " " + p.l_name + "\n")

        with open(orig_file, mode="r") as file_in, open(
            temp_file, "w", newline=""
        ) as file_out:
            csv_in = csv.reader(file_in)
            csv_out = csv.writer(file_out)

            for row in csv_in:
                if not any(p.id == row[7] or p.l_name == row[1] for p in to_remove):
                    csv_out.writerow(row)
            file_in.close()
            file_out.close()
        os.remove(orig_file)
        os.rename(temp_file, orig_file)

        for p in to_remove:
            students_list.remove(p)

    except KeyboardInterrupt:
        print("\n")
    except Exception as e:
        print(f"An error occurred: {e}")


def changeNameByIdOrName(list):
    try:
        value = input("Enter name or ID:")
        to_change = [p for p in list if value == str(p.name) or value == str(p.id)]

        for p in to_change:
            oldname = p.name
            print(oldname)
    except KeyboardInterrupt:
        print("\n")
        return


def readCsvFile():
    with open("studentList.csv", mode="r") as fin:
        csvin = csv.reader(fin)
        for line in csvin:
            if line is None:
                break
            studentlist.append(
                Student(line[0], line[1], line[2], line[3], line[4], line[5], line[6])
            )
        fin.close()


# PROGRAM STARTS

studentlist = []
readCsvFile()
running = True
while running:
    entry = input(
        "| 1: Create User | 2: Print List | 3: Delete User | 4: Change Name | 5: Quit |\n"
    )

    if entry == "1":
        createstudent()
    elif entry == "2":
        printlist(studentlist)
    elif entry == "3":
        # value = input("Enter an ID: ")
        deleteByIdOrName(studentlist)
    elif entry == "4":
        changeNameByIdOrName(studentlist)
    elif entry == "5":
        running = False
    elif entry == "6":
        getStudents(studentlist)
    else:
        print("Try again")
