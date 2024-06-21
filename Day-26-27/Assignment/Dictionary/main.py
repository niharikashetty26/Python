from contact_manager import ContactManager

def main():
    manager = ContactManager()

    while True:

        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Delete Contact")
        print("4. List All Contacts")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            email = input("Enter contact email address: ")
            manager.add_contact(name, phone, email)
        elif choice == '2':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            email = input("Enter contact email address: ")
            manager.update_contact(name, phone if phone else None, email if email else None)
        elif choice == '3':
            name = input("Enter contact name to delete: ")
            manager.delete_contact(name)
        elif choice == '4':
            manager.list_contacts()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please choose again.")

main()
