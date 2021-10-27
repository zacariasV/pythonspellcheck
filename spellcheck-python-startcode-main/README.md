# spellcheck-python-startcode
Python start code for Spell Check Assignment

Part A: User Word Check
Allow the user to enter a single word and to select which search algorithm to use: linear or binary.
Search the contents of the dictionary for the word the user entered using the specified search algorithm.  
Output to the page whether the word was found or not and how long the search took.

Part B: Alice In Wonderland Word Check
Allow the user to specify which search algorithm to use. 
Search the contents of the dictionary, using the search algorithm specified by the user, for each of the words from the Alice in Wonderland story.
Output to the page a total count of all the words that were not found in the dictionary and how long it took to check all of the words.




Main Menu
1: Spell Check a Word (Linear Search)
2: Spell Check a Word (Binary Search)
3: Spell Check Alice In Wonderland (Linear Search)
4: Spell Check Alice In Wonderland (Binary Search)
5: Exit
Enter menu selection (1-5): 1
Please enter a word: hello

Linear Search starting...
hello is IN the dictionary at position 32019. (0.0029914379119873047 seconds)

Main Menu
1: Spell Check a Word (Linear Search)
2: Spell Check a Word (Binary Search)
3: Spell Check Alice In Wonderland (Linear Search)
4: Spell Check Alice In Wonderland (Binary Search)
5: Exit
Enter menu selection (1-5): 1
Please enter a word: hola

Linear Search starting...
hola is NOT IN the dictionary. (0.00798654556274414) seconds

Main Menu
1: Spell Check a Word (Linear Search)
2: Spell Check a Word (Binary Search)
3: Spell Check Alice In Wonderland (Linear Search)
4: Spell Check Alice In Wonderland (Binary Search)
5: Exit
Enter menu selection (1-5): 4

Binary Search starting...
Number of words not found in dictionary: 2017 (0.35611438751220703 seconds)







Tips
Lowercase
The dictionary is all lowercase, so the user entered words and the words from Alice in Wonderland should be converted to lowercase before you check if they are in the dictionary or not.

Timing
The general idea behind timing how long some code takes to run is as follows:
Get the current time before you run the code (startTime)
Run the code
Get the current time after the code has executed (endTime)
Time Elapsed = endTime - startTime

