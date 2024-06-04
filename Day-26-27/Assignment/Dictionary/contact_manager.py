
class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email):
        if name in self.contacts:
            print(f"Contact with name '{name}' already exists.")
        else:
            self.contacts[name] = {'phone': phone, 'email': email}
            print(f"Contact '{name}' added successfully.")

    def update_contact(self, name, phone=None, email=None):
        if name in self.contacts:
            if phone:
                self.contacts[name]['phone'] = phone
            if email:
                self.contacts[name]['email'] = email
            print(f"Contact '{name}' updated successfully.")
        else:
            print(f"Contact with name '{name}' not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact with name '{name}' not found.")

    def list_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("All Contacts:")
            for name, details in self.contacts.items():
                print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")


