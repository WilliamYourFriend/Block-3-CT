'''
Program gaols
1 Get an input
2 Turn input to int
3 Add int to list
4 Pull values from specific index positions
'''

# Importing the random library and creating two empty lists.
import random

myList = []
uniqueList = []

# A greeting to the user.
print('Hello there, lets work with lists')

# The main program, will be the first thing to run when staring the app.
def mainProgram():

# A loop so the user can continue touse the app until they are done.
    while True:

# I think this has to do with the except thing at the end.
        try:
# Allows the user to choose which function to use by getting an input. After the program has the input, an if statment will run a certint function based on the input.
# The except thing does somthing IDK.
            print('Choose one of the following options. Type a number only')
            choice = input('''
1. Add to list
2. Remove from list
3. Add a bunch a numbers
4. Return the value at an index position
5. Sort list
6. Random choice
7. Linear Search
8. recursiveBinarySearch
9. iterativeBinartSearch
10. Print list
11. Clear List
12. End the program
''')
                
            if choice == '1':
                addToList()

            elif choice == '2':
                editList()
                
            elif choice == '3':
                addABunch()
                    
            elif choice == '4':
                indexValues()
                
            elif choice == '5':
                sortList(myList)

            elif choice == '6':
                randomSearch()
                
            elif choice == '7':
                linearSearch()

            elif choice == '8':
                binSearch = input('What number are you looking for?   ')
                recursiveBinarySearch(uniqueList, 0, len(uniqueList)-1, int(binSearch))

            elif choice == '9':
                binSearch = input('What number are you looking for?   ')
                result = iterativeBinartSearch(uniqueList, int(binSearch))
                if result != -1:
                    print('Your number is at index position {}'.format(result))
                else:
                    print('Your number isnt here')

            elif choice == '10':
                printLists()

            elif choice == '11':
                clearList()
                
            else:
                break
            
        except:
            print('An error occurred')

# The program takes an input from the user, turns the input from a string to an int, and adds it to the list. Also prints the list.
def addToList():
    newItem = input('Please type an integer  ')
    myList.append(int(newItem))
    print(myList)

# Gets two inputs from the user that are used as ranges. numToAdd sets the range of the loop and numRange sets the range of the random number generator. Both inpust
# must be changed to ints.
def addABunch():
    print("we're gona add a bunch of numbers")
    numToAdd = input('How many ints do you want to add  ')
    numRange = input('How high do you want the numbers to go  ')
    for x in range(0, int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
    print('Your list is done')

# Delets an items that show multiple times in the list and sorts it from least to geatest. Also prints the list if the user wants.
def sortList(myList):
    for x in myList:
        if x not in uniqueList:
            uniqueList.append(x)
    uniqueList.sort()
    showMe = input('Wanna see the sorted list? y/n   ')
    if showMe.lower() == 'y':
        print(uniqueList)

# Gets an input from the user, turns the inpust to an int, and prints the item is the index positon of the int.
def indexValues():
    indexPos = input('What position would you like to index?  ')
    print(myList[int(indexPos)])

# FIrst this function subtracts 1 from the lenght of the list becuase computers start counting from 0. The lenght - 1 is used as the range for an RNG. Then the
# function prints the item in the index position of the random number.
def randomSearch():
    print("Here's a random value from your list")
    print(myList[random.randint(0, len(myList)-1)])

# Basicly, the function checks every item in the list to see if it is the search item.
def linearSearch():
    print("We're gona search in the worst way possible")
    searchItem = input('What are you looking for?  ')
    count = 0
    for x in range(len(myList)):
        if myList[x] == int(searchItem):
            print('Your item is at index {}'.format(x))
            count = count + 1
    print('Your item showed up {} times'.format(count))

# Cuts the list in half and checks if the search term is more or less than the mid point. If it is more, then lower half of the the list will be disregarded and the
# greater half wil be split in half and the the procese will continue until the search term is found. Loops through recertion.
def recursiveBinarySearch(uniqueList, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if uniqueList[mid] == x:
            print("Oh what luck. Your number is at position {}".format(mid))
        elif uniqueList[mid] > x:
            return recursiveBinarySearch(uniqueList, low, mid - 1, x)
        else:
            return recursiveBinarySearch(uniqueList, mid + 1, high, x)

    else:
        print("Your list isn't here")

# Cuts the list in half and checks if the search term is more or less than the mid point. If it is more, then lower half of the the list will be disregarded and the
# greater half wil be split in half and the the procese will continue until the search term is found. Loops normaly.
def iterativeBinartSearch(uniqueList, x):
    low = 0
    high = len(uniqueList) - 1
    mid = 0

    while low <=high:
        mid = (high + low) // 2

        if uniqueList[mid] < x:
            low = mid + 1

        elif uniqueList[mid] > x:
            high = mid - 1

        else:
            return mid
    return -1

# Prints the list. Will give the option to print the unique list if it exists.
def printLists():
    if len(uniqueList) == 0:
        print(myList)
    else:
        print(myList)
        print(uniqueList)

# Clears the list using the python "clear" function.
def clearList():
    clearChoice = input('Are you sure you want to clear your list? y/n   ')
    if clearChoice == 'y':
        myList.clear()
        uniqueList.clear()
        print('Your list has been cleared')
        
    else:
        print('Your list has NOT been claered')

# Edits the list by getting an input and using the python "remove" function. The input must be turned into an int.
def editList():
    print(myList)

    edit = input('What item would you like to delete?   ')

    myList.remove(int(edit))

    print('{} has been removed'.format(edit))        
        
if __name__ == '__main__':
    mainProgram()
