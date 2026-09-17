"""
TASK: 02 Times Tables

# Skills: Loops,input validation
Ask the user for a number, print the multiplication from 1 to 12 in a readable format:

Extend by using a function you can call for easy entry

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
def times_table(n, i=1):
    if i == 11:
        return
    print(n, "*", i, "=", n * i)
    i = i + 1
    times_table(n, i)
if __name__ == "__main__":
    n = int(input("Enter a number less than 13"))
times_table(n)
def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    pass

