from user import user_menu
from admin import admin_menu
from connection import admin_username, admin_password


def admin_login():
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")

    if username == admin_username and password == admin_password:
        print("Login successful.")
        admin_menu()
    else:
        print("Invalid username or password.")


def main():
    while True:
        print("Welcome to the Online Bookstore")
        print("1. User Mode")
        print("2. Admin Mode")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                user_menu()
            elif choice == 2:
                admin_login()
            elif choice == 3:
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

        except ValueError:
            print("Invalid input. Please enter a numeric choice.")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
