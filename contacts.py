contacts = []  # Empty list to store contacts

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email (optional): ")

    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)  # Add contact to the list

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for i, contact in enumerate(contacts):
            print(f"{i+1}. Name: {contact['name']}")
            print(f"   Phone: {contact['phone']}")
            if contact["email"]:
                print(f"   Email: {contact['email']}")
            print()

def delete_contact():
    if not contacts:
        print("No contacts to delete.")
    else:
        view_contacts()  # Show contacts before deletion
        index = int(input("Enter the number of the contact to delete: ")) - 1
        if index >= 0 and index < len(contacts):
            del contacts[index]
            print("Contact deleted.")
        else:
            print("Invalid index.")

def search_contact():
    if not contacts:
        print("No contacts found.")
    else:
        search_term = input("Enter the name or phone number to search: ")
        found = False
        for contact in contacts:
            if search_term.lower() in contact["name"].lower() or search_term.lower() in contact["phone"].lower():
                print(f"Name: {contact['name']}")
                print(f"Phone: {contact['phone']}")
                if contact["email"]:
                    print(f"Email: {contact['email']}")
                print()
                found = True
        if not found:
            print("Contact not found.")

while True:
    print("\nContact List Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Delete Contact")
    print("4. Search Contact")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        search_contact()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
