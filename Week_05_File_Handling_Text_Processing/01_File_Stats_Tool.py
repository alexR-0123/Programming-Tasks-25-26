"""
TASK: 01 File Stats Tool

# Read a .txt file and compute:
Task:
- Number of lines
- Number of words
- Number of characters
- Most frequent word

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

filename = input("Enter the name of the file")

with open(filename, "r") as file:
    text = file.read()
    
lines = text.splitlines()
line_nums = len(lines)
char_nums = len(text)

words = text.split()
word_nums = len(words)
word_count = {}

for word in words:
    word = word.lower()
    
    if word in word_count:
        words_count[word] +=1
    else:

        word_nums[word] = 1
        
        
most_frequent_word = max(words_count, key=word_count.get)

print("Number of lines: ", lines_nums)
print("Number of characters: ", char_nums)
print("Number of words: ", word_nums)
print("Most frequent word: ", most_frequent_word)
print("It appears: ", word_count[most_frequent_word], "times")




def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    pass


if __name__ == "__main__":
    main()
