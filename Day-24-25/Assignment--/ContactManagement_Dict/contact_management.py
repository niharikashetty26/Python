class Contact:
    def __init__(self):
        self.contacts={}

    def add_contact(self,name,email,phone):
        if name in self.contacts:
            print(f"Contact name : {name} already exist");
        else:
            self.contacts[name]={"email":email,"phone":phone}
            print(f"Contact {name} added successfully")
    def update_contact(self,name,email=None,phone=None):
        if name in self.contacts:
            if phone:
                self.contacts[name]["phone"] = phone
            if email:
                self.contacts[name]["email"]=email
            print(f"Successfully updated {name}")
        else:
            print(f"{name} not found to be updated")
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Deleted {name} successfully")
        else:
            print(f"{name} does not exist")

    def list_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("All Contacts:")
            for name, details in self.contacts.items():
                print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")
