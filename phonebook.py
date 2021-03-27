import sys
import os
import csv
from csv import writer
from csv import reader

directory_list = []
#Load existing data into list
with open('directory.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)
directory_list = data
print(directory_list)


def main():
    #Welcome message
    print("Welcome to Directory.\n")

    #Get user input
    entry = int(input(
    """What would you like to do?\n
    1. Display all contacts
    2. Search for contact.
    3. Create new contact.
    4. Delete contact.
    5. Exit\n
    Enter your command (1, 2, 3, 4, 5): """))
    print('\n')

    #Function Calls
    if entry == 1:
        displayAll()
    elif entry == 2:
        search()
    elif entry == 3:
        create()
    elif entry == 4:
        delete()
    elif entry == 5:
        sys.exit()
    else:
        print("Invalid response.")

    #Update csv file
    with open('directory.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(directory_list)
    

def create():
    #Empty list to store data
    person = []
    #Get user input
    name = input("Enter name: ")
    number = input("Enter number: ")
    address = input("Enter address: ")
    relationship = input("Enter relationship: ")
    #Append to list
    person.append(name)
    person.append(number)
    person.append(address)
    person.append(relationship)

    #Append to directorylist
    directory_list.append(person)
    
    print('\nContact added.\n')


def displayAll():
    #Iterate through list and print
    if not directory_list:
        print("Contact directory is empty.")
    else:
        for i in directory_list:
            for j in i:
                print(j)
            print('', sep='\n')

def search():
    #Get input to search for
    searchBy = input("Whose contact info would you like to see: ")
    print('\n')
    #Iterate through list and dislpay corresponding data
    for i in directory_list:
        if i[0] == searchBy:
            print("Name: " + i[0])
            print("Number: " + i[1])
            print("Address: " + i[2])
            print("Relationship: " + i[3])
            print("\n")


def delete():
    delete_element = input("Whose contact would you like to remove: ")
    removed = False
    for i in directory_list:
        if i[0] == delete_element:
            directory_list.remove(i)
            removed = True

    print("Contact removed.")


main()
