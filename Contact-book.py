

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)
        print(f"Contact '{name}' added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        print("\nContact List:")
        for idx, contact in enumerate(self.contacts, 1):
            print(f"{idx}. {contact.name}, Phone: {contact.phone}")

    def search_contact(self, search_term):
        found = False
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term == contact.phone:
                print(f"\nFound Contact: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")
                found = True
        if not found:
            print(f"No contact found for search term: {search_term}")

    def update_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print("Updating Contact Details")
                contact.phone = input("Enter new phone number: ")
                contact.email = input("Enter new email: ")
                contact.address = input("Enter new address: ")
                print(f"Contact '{name}' updated successfully!")
                return
        print(f"No contact found with name: {name}")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Contact '{name}' deleted successfully!")
                return
        print(f"No contact found with name: {name}")

# User Interface
def display_menu():
    print("\n--- Contact Management System ---")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def main():
    contact_manager = ContactManager()
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_manager.add_contact(name, phone, email, address)
        elif choice == '2':
            contact_manager.view_contacts()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            contact_manager.search_contact(search_term)
        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            contact_manager.update_contact(name)
        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_manager.delete_contact(name)
        elif choice == '6':
            print("Exiting Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
