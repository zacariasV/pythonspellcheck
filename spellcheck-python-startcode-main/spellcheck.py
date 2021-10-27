# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

from os import truncate
import re  # Needed for splitting text with a regular expression
import time

def wordSearch(arrayType, option):
    #prompt a word to spell check using the dicitionary by linear search
    word = input("Please enter a word:").lower()

    #inform user search is starting
    if option == "1" or option == "3":
        print("\nLinear Search starting...")
    elif option == "2" or option == "4":
        print("\nBinary Search starting...")

    #start a timer
    start_time = time.time()

    #begin task
    if option == "1" or option == "3":
        validation = linearSearch(arrayType, word)
    elif option == "2" or option == "4":
        validation = binarySearch(arrayType, word)

    #end timer
    end_time = time.time()
    #calculate time
    elapse_time = end_time - start_time

    # determine if word is true
    if validation != -1:
        print(f"\n{word} is IN the dictionary at position {validation}. ({elapse_time} seconds)")
    else: 
        print(f"\n{word} is NOT IN the dictionary. ({elapse_time}) seconds")

def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    for i in range(len(aliceWords)):
        aliceWords[i] = aliceWords[i].lower()

    # Print first 50 values of each list to verify contents
    print(dictionary[0:50])
    print(aliceWords[0:50])
    
    option = getMenuSelection()
    # Take action based on menu selection 
    if option == "1" or option == "2":
        wordSearch(dictionary, option)
    elif option == "3" or option == "4":
        wordSearch(aliceWords, option)
    elif option == "5":
        print("\nGoodbye")
    else:
        print("\nERROR")
        return None
# end main()


def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()

def getMenuSelection():
    print("\nMAIN MENU")
    print("1: Spell Check a Word (Linear Search)"
        "\n2: Spell Check a Word (Binary Search)"
        "\n3: Spell Check Alice In Wonderland (Linear Search)"
        "\n4: Spell Check Alice In Wonderland (Binary Search)"
        "\n5: Exit")
    return input("Enter a menu option:")

def linearSearch(anArray, item):
    for i in range(len(anArray)):
        if anArray[i] == item:
            return i
    
    #Went through for loop without finding item, so... 
    return -1

def binarySearch(anArray, item):
    LowIndex = 0
    UpIndex = len(anArray) - 1

    while LowIndex <= UpIndex:
        midIndex = (LowIndex + UpIndex) // 2
        if item == anArray[midIndex]:
            return midIndex
        elif item < anArray[midIndex]:
            UpIndex = midIndex - 1
        else:
            LowIndex = midIndex + 1
    # Went through loop without finding item, so... 
    return -1

# Call main() to begin program
main()
