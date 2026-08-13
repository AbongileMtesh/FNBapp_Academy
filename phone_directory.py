contacts = {"Alex": "0712345969","John":"0123456875","Mark":"0234567891"}

lookup_name = input("Enter the person you want to search: ").title()



if lookup_name in contacts:
    print(f"We found {lookup_name}, their number is {contacts[lookup_name]}")
    
else:
    print("Contact not found")
    