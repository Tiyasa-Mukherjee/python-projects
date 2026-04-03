# 1. Contact Book
# - Store contacts in a dictionary
# - Add, search, delete, update contacts
# - Save by name, get number
# Uses: dictionaries, loops, input, functions

def contact_add(book):
    name = input("Enter contact name :")
    number = input("Enter contact number :")
    book[name] = number
    print("Contact added successfully.")
    print(f"Contact Book : \n {book}")

def contact_search(book):
    name = input("Enter contact name to search : ")
    if name in book:
        print(f"{name} : {book[name]}")
    else:
        print("Contact not found.")

def contact_delete(book):
    name = input("Enter contact you want to delete :")
    if name in book:
        del book[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")
    print(f"Contact Book : \n {book}")

def contact_update(book):
    name = input("Enter contact name to update :")
    if name in book:
        number = input("Enter new contact number :")
        book[name]=number
        print("Contact updated successfully.")
    else:
        print("Contact not found.")
    print(f"Contact Book : \n {book}")

print("====== CONTACT BOOK ======")
print("Welcome to the Contact Book!")
contacts = {}
while True:
    print("\n 1. Add Contact ")
    print(" 2. Search Contact ")
    print(" 3. Delete Contact ")
    print(" 4. Update Contact ")
    print(" 5. Exit !")
    choice = int(input("Enter your choice (1,2,3,4,5) : "))
    if choice == 1:
        contact_add(contacts)
    elif choice == 2:
        contact_search(contacts)
    elif choice == 3:
        contact_delete(contacts)
    elif choice == 4:
        contact_update(contacts)
    elif choice == 5:
        print("Exiting Contact Book ....")
        break
    else:
        print("Invalid Choice . Please Try Again !")