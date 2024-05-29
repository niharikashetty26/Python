from contact_management import Contact

def main():
    manager=Contact()

    while True:
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Delete Contact")
        print("4. Show Contacts")
        print("5. Exit")

        choice=input("You want to add, update, delete or see all the contacts?")
        if choice=="1":
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            email = input("Enter contact email address: ")
            manager.add_contact(name,email,phone)

        elif choice=="2":
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            email = input("Enter contact email address: ")
            manager.update_contact(name,email if email else None,phone if phone else None)

        elif choice=="3":
            name = input("Enter contact name: ")
            manager.delete_contact(name)

        elif choice=="4":
            manager.list_contacts()
        elif choice =="5":
            print("You are logged out")
            break
        else:
            print("Invalid operation")

main()


