students = [{"name":"John",
             "maths":21,
             "english":90,
             "science":50},
             {"name":"Sarah",
             "maths":80,
             "english":60,
             "science":55},
             {"name":"Lisa",
             "maths":35,
             "english":67,
             "science":20},
             {"name":"Thabo",
             "maths":89,
             "english":75,
             "science":45},
             {"name":"Thandeka",
             "maths":25,
             "english":95,
             "science":100}
             ]

results = []

for student in students:
    Average = (student["maths"] + student["english"] + student["science"])/3
    #print(f"{student}, your average is {Average}")
    if Average >= 80:
        grade = "A"
    elif 79> Average >=70:
        grade = "B"
    elif 69> Average >=60:
        grade = "C"
    elif 59> Average >=50:
        grade = "D"
    elif Average < 50:
        grade = "F"

    if Average >= 50:
        status = "PASS"
    else:
        status = "FAIL"
    results.append(
    {
        "name": student["name"],
        "average": Average,
        "grade": grade,
        "status": status
    })


for pupil in results:
 class_average = sum(pupil["average"] for pupil in results) / len(results)
 highest_mark = max(pupil["average"] for pupil in results)
 lowest_mark = min(pupil["average"] for pupil in results)

print("\n==============================")
print("       CLASS GRADE REPORT")
print("==============================")
for pupil in results:
    print(f"Name: {pupil['name']}")
    print(f"Average: {pupil['average']:.2f}")
    print(f"Grade: {pupil['grade']}")
    print(f"Status: {pupil['status']}")
    print("------------------------------")

print("\n========== CLASS STATISTICS ==========")
print(f"Class Average: {class_average:.2f}")
print(f"Highest Average: {highest_mark:.2f}")
print(f"Lowest Average: {lowest_mark:.2f}")
print("======================================")










