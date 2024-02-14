class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        print("Contact List:")
        for i, contact in enumerate(self.contacts, start=1):
            print(f"{i}. Name: {contact.name}, Phone: {contact.phone_number}")

    def search_contact(self, search_term):
        search_results = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                search_results.append(contact)
        return search_results

    def update_contact(self, index, updated_contact):
        self.contacts[index] = updated_contact

    def delete_contact(self, index):
        del self.contacts[index]

def print_contact_details(contact):
    print("Name:", contact.name)
    print("Phone:", contact.phone_number)
    print("Email:", contact.email)
    print("Address:", contact.address)

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter contact name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email address: ")
            address = input("Enter address: ")
            contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(contact)
            print("Contact added successfully.")

        elif choice == "2":
            contact_book.view_contacts()

        elif choice == "3":
            search_term = input("Enter name or phone number to search: ")
            search_results = contact_book.search_contact(search_term)
            if search_results:
                print("Search results:")
                for i, contact in enumerate(search_results, start=1):
                    print(f"{i}. {contact.name}, {contact.phone_number}")
            else:
                print("No matching contacts found.")

        elif choice == "4":
            contact_book.view_contacts()
            try:
                index = int(input("Enter index of contact to update: ")) - 1
                if 0 <= index < len(contact_book.contacts):
                    print("Enter new details:")
                    name = input("Enter contact name: ")
                    phone_number = input("Enter phone number: ")
                    email = input("Enter email address: ")
                    address = input("Enter address: ")
                    updated_contact = Contact(name, phone_number, email, address)
                    contact_book.update_contact(index, updated_contact)
                    print("Contact updated successfully.")
                else:
                    print("Invalid index.")
            except ValueError:
                print("Invalid input.")

        elif choice == "5":
            contact_book.view_contacts()
            try:
                index = int(input("Enter index of contact to delete: ")) - 1
                if 0 <= index < len(contact_book.contacts):
                    contact_book.delete_contact(index)
                    print("Contact deleted successfully.")
                else:
                    print("Invalid index.")
            except ValueError:
                print("Invalid input.")

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
