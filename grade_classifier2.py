student = {}

student["name"] = input("Enter your name: ")
student["Subject 1"] = float(input("Enter your mark for subject 1: "))
student["Subject 2"] = float(input("Enter your mark for subject 2: "))
student["Subject 3"] = float(input("Enter your mark for Subject 3: "))

Average = (student["Subject 1"]+student["Subject 2"]+student["Subject 3"])/3

if Average >= 80:
    grade = "A" 
elif 79> Average >=70:
    grade = "B"
elif 69> Average >= 60:
    grade = "C"
elif 59> Average >=50 :
    grade ="D"
else:
    grade = "F"

if Average > 50:
    status = "Pass"
else:
    status = "Fail"

if student["Subject 1"] < 40:
    print("need intervention")
elif student["Subject 2"] < 40:
    print("need intervention")
elif student["Subject 3"] < 40:
    print("need intervention")

    print(f"marks for {student['Subject 1']} is: {student['Subject 1']}")
# print(f"marks for {subjects[1]} is: {marks1}")
# print(f"marks for {subjects[2]} is: {marks2}")


# print(f"Average of {Average} achived for all subjects")
# print(f"{grade}")
# print(status)
# print(f" {flags}")
