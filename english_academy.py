# Asks user for date

validweek = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
weekday = input('Please enter the weekday (Monday-Sunday): ').upper()

if weekday not in validweek:
    print("Error in Weekday: please enter as it's full name. \n ex: Monday")
    exit()

month = int(input('Please enter the the month (in numbers): '))
if month > 12 or month < 1:
    print("Error in Month: please enter a valid month. \n ex: 7")
    exit()

day = int(input('Please enter the day of the month: '))
if day > 31:
    print("Error in Day: please enter a valid date. \n ex: 24")
    exit()

if weekday == "MONDAY" or weekday == "TUESDAY" or weekday == "WEDNESDAY":
    exams = input("Were there exams today? Y/n: ").upper()
    if exams == "Y":
        passed = int(input("How many students passed? "))
        failed = int(input("How many students failed? "))
        stud_total = passed + failed
        percent_passed = ((passed / stud_total) * 100) // 1
        print(f"{percent_passed}% of students passed the exam.")
    else:
        print("Have a nice day")
        
elif weekday == "THURSDAY":
    assists = int(input("What is the percentage of students that assisted with Oral Practice? %"))
    if assists > 50:
        print("The majority of students assisted.")
    else:
        print("The minority of students assisted.")

elif weekday == "FRIDAY":
    if (month == 1 and day == 1) or (month == 7 and day == 1):
        students = int(input("How many students are there? "))
        cost = int(input("How much does each student have to pay? $"))
        tcost = students * cost
        print(f"The total income will be ${tcost}")
    else:
        print("Have a nice day")

else:
    print("We are closed for today")