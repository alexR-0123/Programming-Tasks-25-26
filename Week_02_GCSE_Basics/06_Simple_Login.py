"""
TASK: 06 Simple Login

# Skills: Selection, string comparison
Start with a correct username/password (extend if saved in a text file separately):
- Ask for login
- Print "Welcome" or "Access Denied {number} attempts remaining"
Only allow 3 attempts and close the file

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
print("Enter username and password for access")
username = ""
password = ""
count = 0  
while username != "iplaygtaVI" and password != "iplayGTAVI12345" and count < 3:
        username = input("Enter username ")
        password = input("Enter password ")
        
        if username == "iplaygtaVI" and password == "iplayGTAVI12345":
            print("Access granted. You may enter now")
            break
        else:
            print("Access denied. Think again")
            count = count + 1



def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    pass


if __name__ == "__main__":
    main()
