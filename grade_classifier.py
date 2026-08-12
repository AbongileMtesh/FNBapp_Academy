name = input("Enter your name: ")
subjects = ["Math","English","Physics"]
marks = float(input(f"Enter you marks for {subjects[0]}: "))
marks1 = float(input(f"Enter you marks for {subjects[1]}: "))
marks2 = float(input(f"Enter you marks for {subjects[2]}: "))

Average = (marks+marks1+marks2)/3


if Average >= 80:
    grade = "A" 
elif 79> Average >=70:
    grade = "B"
elif 69> Average >= 60:
    grade = "C"
elif 59> Average >=50 :
    grade ="D"
elif Average <50:
    grade = "F"

if Average > 50:
    status = "Pass"
else:
    status = "Fail"

flags = []

if marks < 40:
    flags.append("Math needs intervention")

if marks1 < 40:
    flags.append("English needs intervention")

if marks2 < 40:
    flags.append("Physics needs intervention")

print(f"marks for {subjects[0]} is: {marks}")
print(f"marks for {subjects[1]} is: {marks1}")
print(f"marks for {subjects[2]} is: {marks2}")


print(f"Average of {Average} achived for all subjects")
print(f"{grade}")
print(status)
print(f" {flags}")

