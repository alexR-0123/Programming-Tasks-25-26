"""
TASK: 05 Shopping List

# Skills: Loops, lists
Allow the user to add itemds to a shopping list until they type DONE
When they type DONE, print the list and ask if they want to edit any item.
They should select an item by number and allow them to ammend the item.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
shopping_list = []
print("Enter your shopping list")
print("Type DONE when you are finished. \n")

while True:
    item = input("Add an item")
    if item.upper() == "DONE":
        break
    shopping_list.append(item)
    
print("\nYour shopping list is: ")
for i in range(len(shopping_list)):
    print(f"{i+1}.{shopping_list[i]}")
    
change_item = input("\Would you like to change an item? (yes/no)").lower()
if change_item == "yes":
    item_num = int(input("Enter the number of the item"))
    changed_item = input("Enter the item you would like to add instead")
    shopping_list[item_num - 1] = chnaged_item
        
print("\nYour shopping list: ")
for i in range(len(shopping_list)):
        print(f"{i+1}. {shopping_list[i]}")
def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    pass


if __name__ == "__main__":
    main()
