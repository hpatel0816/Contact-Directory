import sys
import os
import csv
import operator

#List to store data
directory_list = []

#Person object constructor
class NewPerson():
  def __init__(self, name, number, address):
    self.name = name
    self.number = number
    self.address = address

#Main function
def main():
  # Load existing data from csv file
  with open('directory.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

    #Append to directory list as objects
    for element in data:
      person = NewPerson(element[0], element[1], element[2])
      global directory_list
      directory_list.append(person)
  
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

  #Sort the list
  directory_list = sortArray()

  #Update csv file
  with open('directory.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for item in directory_list:
      writer.writerow([item.name, item.number, item.address])
  

def sortArray():
  #Sort contacts alphabetically
  sorted_list = sorted(directory_list, key=operator.attrgetter('name'))
  return sorted_list


def create():
  #Get user input
  name = input("Enter name: ")
  number = input("Enter number: ")
  address = input("Enter address: ")
  
  #Create new person entry to append to list
  person = NewPerson(name, number, address)
  directory_list.append(person)
  print("\nContact added.")


def displayAll():
  #Check if list exists
  if not directory_list:
    print("Contact directory is empty.")
  #Iterate through list and print
  else:
    for i in directory_list:
      print("Name: " + i.name)
      print("Number: " + i.number)
      print("Address: " + i.address)
      print('\n')


def search():
  #Get name of person to search for
  searchBy = input("Whose contact info would you like to see: ")
  found = False
  
  #Iterate through list and dislpay the person's data if found
  for i in directory_list:
    if i.name == searchBy:
      found = True
      print("Name: " + i.name)
      print("Number: " + i.number)
      print("Address: " + i.address)
      print("\n")
  
  #If person was not found
  if not found:
    print("Contact doesn't exist.")


def delete():
  #Get name of person to remove
  delete_element = input("Whose contact would you like to remove: ")
  removed = False

  #Iterate through list to find remove person
  for i in directory_list:
    if i.name == delete_element:
      directory_list.remove(i)
      removed = True
  
  #Display message if removed or not
  if removed:
    print("Contact removed.")
  else:
    print("Unable to remove contact.")

main()
