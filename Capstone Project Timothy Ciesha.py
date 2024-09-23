# Yellow Pages App

contacts = {}

# sample data
contacts["Lionel Messi"] = {
    "number": "081234567890",
    "address": "Jl. Leo No. 10, Argentina",
    "email": "leomessi@gmail.com",
    "category": "personal"
}

contacts["PT Maju Jaya"] = {
    "number": "02187654321",
    "address": "Jl. Macet Raya Blok A5, Cikarang",
    "email": "info@majujaya.com",
    "category": "business"
}

contacts["Steph Curry"] = {
    "number": "087811223344",
    "address": "Golden street, USA",
    "email": "stephcurry@gmail.com",
    "category": "personal"
}

contacts["Toko ABC"] = {
    "number": "02198765432",
    "address": "Jl. Gatot Subroto No. 123, Semarang",
    "email": "tokoabc@gmail.com",
    "category": "business"
}

contacts["Doctor Tirta"] = {
    "number": "081122334455",
    "address": "Jl. Kesehatan No. 8, Jakarta",
    "email": "dr.tirta@yahoo.com",
    "category": "business"
}

contacts["Doctor Tulang"] = {
    "number": "087810982347",
    "address": "Jl. Tulang Rusuk, Cengkareng",
    "email": "dr.tulang@gmail.com",
    "category": "business"
}

contacts["Toko Listrik"] = {
    "number": "02128753322",
    "address": "Jl. Kesetrum, Cikupa",
    "email": "tokolistrik@gmail.com",
    "category": "business"
}

contacts["Cristiano Ronaldo"] = {
    "number": "087777777777",
    "address": "Jl. Cristiano, Portugal",
    "email": "cr7@gmail.com",
    "category": "personal"
}


# Function to display the menu
def show_menu():
    print("\nYellow Pages Menu:")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Edit Contact")
    print("5. Delete Contact")
    print("6. Sort Contacts") 
    print("7. Filter Contacts") 
    print("8. Exit\n")

    choice = input("Enter your choice (1-8): ")
    return choice

def validate_email(email):
    return '@' in email and '.' in email

def validate_phone_number(number):
    return 10 <= len(number) <= 13

def validate_category(category):
    return category.lower() in ['personal', 'business']

# Function to add a contact
def add_contact():
    name = input("Enter name: ")
    if name.lower() in (key.lower() for key in contacts):
        print("Contact already exists!")
        return
    
    # Validate phone number
    while True:
        number = input("Enter phone number (10-13 digits): ")
        if validate_phone_number(number):
            break
        else:
            print("Invalid number. Ensure it is between 10-13 digits.")
    
    address = input("Enter address: ")
    
    # Validate email
    while True:
        email = input("Enter email: ")
        if validate_email(email):
            break
        else:
            print("Invalid email. Ensure it contains '@' and '.'")
    
    # Validate category
    while True:
        category = input("Enter category (personal/business): ")
        if validate_category(category):
            break
        else:
            print("Invalid category. Choose 'personal' or 'business'.")
    
    contacts[name] = {
        "number": number,
        "address": address,
        "email": email,
        "category": category.lower()
    }
    print("Contact successfully added!")


# Function to view all contacts
def view_contacts():
    if len(contacts) == 0:
        print("No contacts saved yet.")
    else:
        print("-" * 116)
        print("Name" + ' ' * (20 - len("Name")) + "| " +
              "Number" + ' ' * (15 - len("Number")) + "| " +
              "Address" + ' ' * (40 - len("Address")) + "| " +
              "Email" + ' ' * (25 - len("Email")) + "| " +
              "Category" + ' ' * (10 - len("Category")))
        
        print("-" * 116)
        
        for name, info in contacts.items():
            print(name + ' ' * (20 - len(name)) + "| " +
                  info['number'] + ' ' * (15 - len(info['number'])) + "| " +
                  info['address'] + ' ' * (40 - len(info['address'])) + "| " +
                  info['email'] + ' ' * (25 - len(info['email'])) + "| " +
                  info['category'] + ' ' * (10 - len(info['category'])))
        
        print("-" * 116)

# Function to search for a contact
def search_contact():
    name = input("Enter the name you want to search: ").lower() 
    contact_found = False 
    
    print("-" * 116)
    for key in contacts:
        if name in key.lower():  
            info = contacts[key] 
            print(key + ' ' * (20 - len(key)) + "| " +
                  info['number'] + ' ' * (15 - len(info['number'])) + "| " +
                  info['address'] + ' ' * (40 - len(info['address'])) + "| " +
                  info['email'] + ' ' * (25 - len(info['email'])) + "| " +
                  info['category'] + ' ' * (10 - len(info['category'])))
            contact_found = True 
            print("-" * 116)

    if not contact_found:
        print("Contact not found.")


# Function to edit a contact
def edit_contact():
    name_input = input("Enter the name of the contact you want to edit: ").lower() 
    
    contact_found = False
    for key in contacts: 
        if key.lower() == name_input:
            contact_found = True
            name = key 
            break

    if contact_found: 
        print("Enter new information (leave blank if you don't want to change):")

        # Validate phone number
        while True:
            number = input(f"Number ({contacts[name]['number']}): ") or contacts[name]['number']
            if validate_phone_number(number):
                break
            else:
                print("Invalid number. Ensure it is between 10-13 digits.")

        address = input(f"Address ({contacts[name]['address']}): ") or contacts[name]['address']

        # Validate email
        while True:
            email = input(f"Email ({contacts[name]['email']}): ") or contacts[name]['email']
            if validate_email(email):
                break
            else:
                print("Invalid email. Ensure it contains '@' and '.'")

        # Validate category
        while True:
            category = input(f"Category ({contacts[name]['category']}): ") or contacts[name]['category']
            if validate_category(category): 
                break
            else:
                print("Invalid category. Choose 'personal' or 'business'.")

        # Update the contact data
        contacts[name] = {
            "number": number,
            "address": address,
            "email": email,
            "category": category.lower()
        }
        print("Contact successfully updated!")
    else:
        print("Contact not found.")


# Function to delete a contact
def delete_contact(): 
    attempts = 0
    while attempts < 2:
        name_input = input("Enter the name of the contact you want to delete: ").lower() 

        for key in list(contacts):
            if key.lower() == name_input:
                del contacts[key] 
                print("Contact successfully deleted.")
                return 

        print("Contact not found.") 
        attempts += 1  

    print("You have tried 2 times. Go back to the main menu.")
    show_menu()

# Function to sort contacts
def sort_contacts():
    while True:
        print("Sort by:")
        print("1. Name")
        print("2. Phone Number")
        print("3. Category")

        choice = input("Choose sorting criteria (1-3): ")

        if choice == "1":
            sorted_contacts = dict(sorted(contacts.items(), key=lambda x: x[0].lower()))
            print("\nContacts sorted by name.")
            break
        elif choice == "2":
            sorted_contacts = dict(sorted(contacts.items(), key=lambda x: x[1]['number']))
            print("\nContacts sorted by phone number.")
            break
        elif choice == "3":
            sorted_contacts = dict(sorted(contacts.items(), key=lambda x: x[1]['category']))
            print("\nContacts sorted by category.")
            break
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")
    
    # Display sorted contacts
    display_contacts(sorted_contacts)

# function to display contacts
def display_contacts(contact_list):
    if len(contact_list) == 0:
        print("No contacts available.")
    else:
        print("-" * 116)
        print("Name" + ' ' * (20 - len("Name")) + "| " +
              "Phone Number" + ' ' * (15 - len("Phone Number")) + "| " +
              "Address" + ' ' * (40 - len("Address")) + "| " +
              "Email" + ' ' * (25 - len("Email")) + "| " +
              "Category" + ' ' * (10 - len("Category")))
        print("-" * 116)
        
        for name, info in contact_list.items():
            print(name + ' ' * (20 - len(name)) + "| " +
                  info['number'] + ' ' * (15 - len(info['number'])) + "| " +
                  info['address'] + ' ' * (40 - len(info['address'])) + "| " +
                  info['email'] + ' ' * (25 - len(info['email'])) + "| " +
                  info['category'] + ' ' * (10 - len(info['category'])))
        
        print("-" * 116)

# Function to filter contacts by category
def filter_contacts():
    while True:
        print("Filter by category:")
        print("1. Personal")
        print("2. Business")

        choice = input("Choose category (1-2): ")

        if choice == "1":
            filtered_contacts = {name: info for name, info in contacts.items() if info['category'] == 'personal'}
            print("\nShowing personal contacts:")
            break
        elif choice == "2":
            filtered_contacts = {name: info for name, info in contacts.items() if info['category'] == 'business'}
            print("\nShowing business contacts:")
            break
        else:
            print("\nInvalid choice. Please enter 1 or 2.")
    
    # Display filtered contacts
    display_contacts(filtered_contacts)


# Main program
(show_menu)

while True:
    choice = show_menu()

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        edit_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        sort_contacts()
    elif choice == "7":
        filter_contacts() 
    elif choice == "8":
        print("Thank you for using Yellow Pages. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
