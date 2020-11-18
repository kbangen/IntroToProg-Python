# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Kevin Bangen, 11/16/2020, Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "C:\_PythonClass\Assignment05\ToDoList.txt"   # An object that represents a file
objFile = None
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open(strFile, "r")
for row in objFile:
    strData = row.split(",")
    dicRow = {"Task":strData[0], "Priority":strData[1].strip()}
    lstTable.append(dicRow)
objFile.close()
print(lstTable)

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        for row in lstTable:
            print(row["Task"] + ", " + row["Priority"])
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = input("Please provide a task:")
        strPrior = input("Please provide a priority:")
        dicRow = {"Task": strTask, "Priority": strPrior.strip()}
        lstTable.append(dicRow)
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strDelete=input("Please provide task to delete:")
        for row in lstTable:
            if (row["Task"] == strDelete):
                lstTable.remove(row)
                print("Item deleted from list/Table!")
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open(strFile,"w")
        for row in lstTable:
            objFile.write(row["Task"] + ", " + row["Priority"]+ '\n')
        objFile.close()
        print("Data saved to file!")
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        input("Press enter to exit program!")
        break  # and Exit the program
