firstname = input("Enter your firstname: ")
lastname = input("Enter you lastname: ")
bio = input("Enter a short bio about yourself: ").strip()

username = f"{firstname[0]}{lastname}".lower()
fullname = f"{firstname} {lastname}".title()
bio_num = len(bio)
bio_replace = bio.replace("I am", "I'm")



print(fullname)
print(username)
print(bio)
print(bio_num)
print(bio_replace)