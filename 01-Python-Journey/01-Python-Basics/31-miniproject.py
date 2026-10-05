import json
import re


class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return (
            f"Name  : {self.name}\n"
            f"Phone : {self.phone}\n"
            f"Email : {self.email}"
        )

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email
        }


class ContactBook:
    def __init__(self):
        self.contacts = []
        self.filename = "contacts.json"
        self.load_contacts()

    def valid_phone(self, phone):
        return re.match(r"^[0-9]{10}$", phone)

    def valid_email(self, email):
        return re.match(r"^[\w.-]+@[\w.-]+\.\w+$", email)

    def add_contact(self):
        name = input("Enter name: ").strip()
        phone = input("Enter phone number: ").strip()
        email = input("Enter email: ").strip()

        if not name:
            print("Name cannot be empty.")
            return

        if not self.valid_phone(phone):
            print("Invalid phone number. Enter exactly 10 digits.")
            return

        if not self.valid_email(email):
            print("Invalid email address.")
            return

        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        self.save_contacts()
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return

        print("\n------------ CONTACTS -----------")
        for contact in self.contacts:
            print(contact)
            print("------------------------------")

    def search_contact(self):
        name = input("Enter name to search: ").strip()

        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print("\nContact Found!")
                print(contact)
                return

        print("Contact not found.")

    def update_contact(self):
        name = input("Enter name to update: ").strip()

        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print("\nCurrent details:")
                print(contact)

                new_name = input(
                    "Enter new name (press Enter to keep old): "
                ).strip()
                new_phone = input(
                    "Enter new phone (press Enter to keep old): "
                ).strip()
                new_email = input(
                    "Enter new email (press Enter to keep old): "
                ).strip()

                if new_name:
                    contact.name = new_name

                if new_phone:
                    if self.valid_phone(new_phone):
                        contact.phone = new_phone
                    else:
                        print("Invalid phone. Old phone kept.")

                if new_email:
                    if self.valid_email(new_email):
                        contact.email = new_email
                    else:
                        print("Invalid email. Old email kept.")

                self.save_contacts()
                print("Contact updated successfully!")
                return

        print("Contact not found.")

    def delete_contact(self):
        name = input("Enter name to delete: ").strip()

        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                self.save_contacts()
                print("Contact deleted successfully!")
                return

        print("Contact not found.")

    def save_contacts(self):
        try:
            data = [contact.to_dict() for contact in self.contacts]

            with open(self.filename, "w") as file:
                json.dump(data, file, indent=4)

        except Exception as e:
            print("Error saving contacts:", e)

    def load_contacts(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)

            for item in data:
                contact = Contact(
                    item["name"],
                    item["phone"],
                    item["email"]
                )
                self.contacts.append(contact)

        except FileNotFoundError:
            self.contacts = []

        except json.JSONDecodeError:
            print("Contact file is empty or corrupted.")
            self.contacts = []

        except Exception as e:
            print("Error loading contacts:", e)


def main():
    contact_book = ContactBook()

    while True:
        print("------------ CONTACT BOOK ----------")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                contact_book.add_contact()

            elif choice == 2:
                contact_book.view_contacts()

            elif choice == 3:
                contact_book.search_contact()

            elif choice == 4:
                contact_book.update_contact()

            elif choice == 5:
                contact_book.delete_contact()

            elif choice == 6:
                print("Thank you for using Contact Book!")
                break

            else:
                print("Please choose a number between 1 and 6.")

        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()
