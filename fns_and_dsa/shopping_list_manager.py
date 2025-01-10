shopping_list = []

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    global shopping_list
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter the item to be added in the list: ")
            shopping_list.append(item)
        elif choice == '2':
            to_be_removed = input("Enter the item to be removed: ")
            if to_be_removed in shopping_list:
                 shopping_list.remove(to_be_removed)
                 print(f"{to_be_removed} successfully removed.")
            else:
                print(f"{to_be_removed} not found in the list.")      
        elif choice == '3':
            # Display the shopping list
            if shopping_list:
                print("Shopping list: ")
                for e in shopping_list:
                    print(f"-{e}")
            else:
                print("The shopping list is empty!")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()