#Basic if/else statement

age = int(input("Enter your age: "))
section_pass = input("Do you have VIP ticket? ").lower()

if age >= 18 and section_pass == "yes":
    print("Access granted to VIP!!")
elif age >= 18 and section_pass == "no":
    print("Access granted to general")
else :
    print("access denied!!")
    
