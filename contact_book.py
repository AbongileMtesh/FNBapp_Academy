contacts = [{"name": "Amanda", "phone": "0987654321", "email": "Amanda@gmail.com"},
            {"name": "Phindile", "phone": "0123456789", "email": "Phindile@gmail.com"}]


def add_contact(name, phone, email):
    new_contact = {"name": name, "phone": phone, "email": email}
    contacts.append(new_contact)


def search_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact
    return None


def delete_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            return True
    #return False


def view_all():
    print(contacts)


while True:
    user_input = int(input(
        "Enter number 1,2,3,4,5\n"
        "1: add\n"
        "2: search\n"
        "3: delete\n"
        "4: view\n"
        "5: exit\n"
        "Choice: "
    ))

    if user_input == 1:
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        add_contact(name, phone, email)
    elif user_input == 2:
        name = input("Search name: ")
        result = search_contact(name)
        if result:
            print(result)
        else:
            print("Contact not found")
    elif user_input == 3:
        name = input("Delete name: ")
        if delete_contact(name):
            print("Contact deleted")
        else:
            print("Contact not found")
    elif user_input == 4:
        view_all()
    elif user_input == 5:
        break
    else:
        print("Invalid option")
        break

   

