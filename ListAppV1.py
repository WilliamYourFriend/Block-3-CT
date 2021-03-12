'''
Program gaols
1 Get an input
2 Turn input to int
3 Add int to list
4 Pull values from specific index positions
'''

import random

myList = []

print('''Hello there, lets work with lists
''')

def mainProgram():
    while True:
        try:

            print('''Choose one of the following options. Type a number only
''')
            choice = input('''1. Add to list, 2. Return the value at an index position, 3. Random choice 4. End the program
''')
                
            if choice == '1':
                addToList()
                
            elif choice == '2':
                indexValues()
                    
            elif choice == '3':
                randomSearch()
                
            else:
                break
            
        except:
            print('''An error occurred
''')
                
def addToList():

    newItem = input('''Please type an integer
''')

    myList.append(int(newItem))

    print(myList)

def indexValues():

    indexPos = input('''What position would you like to index?
''')

    print(myList[int(indexPos)])

def randomSearch():
    
    print("""Here's a random value from your list
""")
    print(myList[random.randint(0, len(myList)-1)])

if __name__ == '__main__':
            mainProgram()
