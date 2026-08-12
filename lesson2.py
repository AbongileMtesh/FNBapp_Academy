#Tracking individual letters
name = "Python"

print(name[0])
print(name[-1])
print(name[2])

#using te strings method
town = "  Johannesburg  "
print(town.upper())
print(town.strip())

#email address generating system

firstname =input("Enter your firstname: ").strip()
lastname = input("Enter your lastname: ").strip()

username = f"{firstname[0]}{lastname}"
print(f"Your email address is {username.lower()}@gmail.com")