# Defining  the structure for storing contacts
contacts = []

# Function to add a new contact
def add_contact(name, phone, email, address):
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print(f"Contact '{name}' added successfully.")

# Function to display all contacts
def view_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        print("\n--- Contact List ---")
        for idx, contact in enumerate(contacts):
            print(f"{idx + 1}. {contact['name']} - {contact['phone']}")

# Function to search for a contact
def search_contact(search_term):
    found_contacts = [contact for contact in contacts if search_term.lower() in contact["name"].lower() or search_term in contact["phone"]]
    if found_contacts:
        print("\n--- Search Results ---")
        for contact in found_contacts:
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}\n")
    else:
        print(f"No contacts found for '{search_term}'.")

# Function to update a contact
def update_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print(f"\nUpdating contact '{name}'. Leave a field blank to keep the current value.")
            new_phone = input(f"Enter new phone number ({contact['phone']}): ") or contact["phone"]
            new_email = input(f"Enter new email ({contact['email']}): ") or contact["email"]
            new_address = input(f"Enter new address ({contact['address']}): ") or contact["address"]

            contact["phone"] = new_phone
            contact["email"] = new_email
            contact["address"] = new_address

            print(f"Contact '{name}' updated successfully.")
            return

    print(f"No contact found with the name '{name}'.")

# Function to delete a contact
def delete_contact(name):
    global contacts
    contacts = [contact for contact in contacts if contact["name"].lower() != name.lower()]
    print(f"Contact '{name}' deleted successfully.")

# Main menu
def contact_book():
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            add_contact(name, phone, email, address)
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_term = input("Enter name or phone number to search: ")
            search_contact(search_term)
        elif choice == "4":
            name = input("Enter the name of the contact to update: ")
            update_contact(name)
        elif choice == "5":
            name = input("Enter the name of the contact to delete: ")
            delete_contact(name)
        elif choice == "6":
            print("Exiting the Contact Book application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

# Run the Contact Book application
contact_book()
