SOFTWARE INSTRUCTIONS

***IMPORTANT***
When an error ocoures, the app will not close. You will get an error message and will be sent back to the main menu.

MAIN MENU:

Upon starting the app you will be greeted with a list of numbered options. Typing a number will execute the corsponding function. IF ANYTHING OTHER THAN NUMBERS 11 WILL END THE PROGRAM.

OPTION 1/ADD TO LIST:

When initiating this function, you will be asked to type an integer. ANYTHING OTHER THAN AN INT WILL CAUSE AN ERROR. After the integer is typed, it will be add to your list, your list will be prited, and you will be sent back to the main menu.

OPTION 2/REMOVE FROM LIST:

When initiating this function, you will be shown your list. Then you will be asked to type which integer you want to delete. ANYTHING OTHER THAN AN INT WILL CAUSE AN ERROR. TYPING AN INTEGER THAT IS NOT IN THE LIST WILL CAUSE AN ERROR. After you type an integer, you will get a confermation message conferming that it has been deleted, and you will be sent back to the main menu.

OPTION 3/ADD A BUNCH OF NUMBERS

When initiating this function, you will be asked to type an integer. ANYTHING OTHER THAN AN INT WILL CAUSE AN ERROR. This will be the number of integers that will be added. Then you will be asked to type another integer. ANYTHING OTHER THAN AN INT WILL CAUSE AN ERROR. This will be how high the numbers will go. The program will then add however many random numbers you typed. The random numbers will be between 0 and the number you typed. Then you will be sent back to the main menu.

OPTION 4/RETURN THE VALUE AT AN INDEX POSITION

When initiating this function, you will be asked to type an integer. ANYTHING OTHER THAN AN INT WILL CAUSE AN ERROR. After you type an integer, you will be shown the itam in that index pposition and you will be sent back to the main menu. (Remeber that computer count starting at 0 so the first item in your list is at index position 0.

OPTION 5/SORT LIST

When initiating this function, your list will be sortred. This mean that a second list will be created. This second list will be the same as your original, but all items are listed least to greatest. All duplicate numbers will also be deleted. You will be asked to type y or n. If you type n, you will be sent back to the main menu. If you type y, your will be shown your sorted list and be sent back to the main menu.

(Because of how binary search works, you must sort your list befor using it)

OPTION 6/RANDOM CHOICE

When initiating this function, you will be shown a random item from your list and you will be sent back to the main menu.

OPTION 7/LINER SEARCH

When initiating this function, you will be asked to type an integer. ANYTHING OTHER THAN AN INT WILL CAUSE AN ERROR. You will then be shown the index position of each of the instances of your number, as well as how many times it shows up, and you will be sent back to the main menu.

OPTION 8/RECURSIVE BINARY SEARCH

When initiating this function, you will be ask to type an integer. Then you will be shown what index position you number shows up at. Then you will be sent back to the main menu.

OPTION 9/ITERITIVE BINARY SEARCH

When initiating this function, you will be ask to type an integer. Then you will be shown what index position you number shows up at. Then you will be sent back to the main menu.

(RECURSIVE BINARY SEARCH and ITERITIVE BINARY SEARCH do the exact same thing, just in different ways)

OPTION 10/PRINT LIST

When initiating this function, if a sorted list exists, you will be shown your original and sorted list. If a sorted list does not exist, you will be shown 
just you original list. Then you will be sent back to the main menu.

OPTION 11/CLEAR LIST

When initiating this function, you will be asked to type y or n. If you type n, you will be sent back to the main menu. If you type y, both of your lists will be cleared and you will be sent back to the main menu.

BINARY SEARCH

Binary search is a method of searching through data by spliting the list in half. After the list is split in half, the program check if the number its serching for is more or less than the middle of the data set. If its less, the greater half of list is ignored, and the proces repats using the other half. If it is more, the oposit happens. Binary search will only work if your list in 2 items or longer. There are 2 differen't kinds of binary search, recursive and iterative. As said befor, the function loops until it finds the correct item. Iterative does this by changing which list it is slpitig and going back to the top of a while loop if the number isn't found. Recursive loops by redefining its self and runing again.

MY CHANGES

I made 3 changes to the code. I added the fuctions edit and clear list, and changed how print list works. 

CLear list simply clears the list using the clear function. Here is the code:

def clearList():
    clearChoice = input('Are you sure you want to clear your list? y/n   ')
    if clearChoice == 'y':
        myList.clear()
        uniqueList.clear()
        print('Your list has been cleared')
        
    else:
        print('Your list has NOT been claered')

Edit list first takes an input from the user. That number is then converted to an integer. If the integer is in the list, it will be revoved using the remove fuction. Here is the code:

def editList():
    print(myList)

    edit = input('What item would you like to delete?   ')

    myList.remove(int(edit))

    print('{} has been removed'.format(edit))

The change I made to print list is insted of asking if the user wants to see the sorted or un-sorted list it will just print both. Here is the code:

def printLists():
    if len(uniqueList) == 0:
        print(myList)
    else:
        print(myList)
        print(uniqueList)

I made the changes because preliusly, the only way to get rid of any of anything in the list was to exit the program completly and restart. Now you can clear the whloe list without closeing the pogram and you can also delete spesific items.