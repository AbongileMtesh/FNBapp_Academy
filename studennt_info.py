#Collecting students information
name = str(input("Enter your name: "))
surname = str(input("Enter your surname: "))
age = int(input("Enter your age: "))
favourite_num = float(input("Enter your favourite number: "))

print(f"Welcome, {name.upper().title()} {surname.upper().title()}")
print(f"Your age in months is: {age * 12}")
print(f"Your favorite number rounded off is {round(favourite_num,2)}")
print(f"{type(name)}, {type(surname)}, {type(age)},{type(favourite_num)}")
