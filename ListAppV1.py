'''
Program gaols
1 Get an input
2 Turn input to int
3 Add int to list
4 Pull values from specific index positions
'''

import random
import turtle

myList = []
p = turtle.write 
s = turtle.getscreen()

print('Hello there, lets work with lists')

def mainProgram():
    while True:
        try:

            print('Choose one of the following options. Type a number only')
            choice = input('''
1. Add to list
2. Add a bunch a numbers
3. Return the value at an index position
4. Print list
5. Random choice
6. Linear Search
7. End the program
''')
                
            if choice == '1':
                addToList()
                
            elif choice == '2':
                addABunch()
                    
            elif choice == '3':
                indexValues()
                
            elif choice == '4':
                print(myList)

            elif choice == '5':
                randomSearch()
                
            elif choice == '6':
                linearSearch()
                
            else:
                break
            
        except:
            print('An error occurred')
                
def addToList():
    newItem = input('Please type an integer  ')
    myList.append(int(newItem))
    print(myList)

def addABunch():
    print("we're gona add a bunch of numbers")
    numToAdd = input('How many ints do you want to add  ')
    numRange = input('How high do you want the numbers to go  ')
    for x in range(0, int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
    print('Your list is done')

def indexValues():
    indexPos = input('What position would you like to index?  ')
    print(myList[int(indexPos)])

def randomSearch():
    print("Here's a random value from your list")
    print(myList[random.randint(0, len(myList)-1)])

def linearSearch():
    print("We're gona search in the worst way possible")
    searchItem = input('What are you looking for?  ')
    count = 0
    for x in range(len(myList)):
        if myList[x] == int(searchItem):
            print('Your item is at index {}'.format(x))
            count = count + 1
    print('Your item showed up {} times'.format(count))
            

if __name__ == '__main__':
    mainProgram()
