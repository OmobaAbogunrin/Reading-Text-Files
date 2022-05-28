# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is dpythonone. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from cgitb import text
from dataclasses import dataclass
from itertools import count


def read_file_content(filename):
    # [assignment] Add your code here 
    text = open("C:/Users/Abayomi/Desktop/Zuri/Reading-Text-Files/story.txt", encoding='utf8')
    data = text.read()
    #print (data)
    return data

read_file_content("./story.txt")
#print (check)


def count_words():
    text = read_file_content("./story.txt")
    #print (text)
    # [assignment] Add your code here
    counts = {}
    words = text.split()
    #words = words.lower()
    #print (words)

  

    # Iterate over each word in words
    for word in words:
        #print (word)
        # Check if the word is already in dictionary
        if word in counts:
            # Increment count of word by 1
            counts[word] = counts[word] + 1
        else:
            # Add the word to dictionary with count 1
            counts[word] = 1

    return counts
    
      
print(count_words())
    #return {"as": 10, "would": 20}