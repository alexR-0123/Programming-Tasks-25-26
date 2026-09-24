"""
TASK: 03 2D Array Adder

# 2D Array Added
Create a 2D arraw and allow user to:
- Append new values in
- read all current values
- delete a chosen entry

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

data = []

#displays the options to what you can pick from
while True:
    print("Pick an option")
    print("1. append a new value")
    print("2. show the values")
    print("3. delete a value")
    print("4. exit")
    
    choice = int(input("Enter your choice"))
    if choice == 1:
        value = input("Enter your value")
        data.append([value])
        print("Your value has been appended")
        
    elif choice ==2:
        print("Current values in data: ")
        for i in range(len(data)):
            print(i, data[i])
            
    elif choice ==3:
        print("Current values in data: ")
        for i in range(len(data)):
            num = int(input("Enter the number you want to delete"))
            
        if num < len(data):
            data.pop(num)
            print("The value has been deleted")
        else:
            print("Number is not valid")
            
    elif choice ==4:
        print("Exitting")
        break
    
    else:
        print("Please enter one of the choices presented")

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    pass


if __name__ == "__main__":
    main()
