import os
books={}
def clear_screen():
  os.system("cls" if os.name=="nt" else "clear")

def add_book():
    clear_screen()
    isbn=int(input("Enter ISBN :"))
    titl=input("Enter The Titl :")
    author=input("Enter The Author :")
    books[isbn]={}
    books[isbn]['name']=titl
    books[isbn]['katp']=author
    books[isbn]['available']=True
    print(f" The Book '{books[isbn]['name']}' By '{books[isbn]['katp']}' Has Added Successfully!")

def list_books():
  clear_screen()
  for var in (books):
    print(f"ISBN: {var}, Titl: {books[var]['name']}, Author: {books[var]['katp']}  available:{books[var]['available']}")

def check_out():
  clear_screen()
  theb=int((input("Enter ISBN to check out :")))
  if theb in books:
    if books[theb]['available']==True:
      books[theb]['available']=False
      print(f"{books[theb]['name']} Checked out successfully...")
    elif books[theb]['available']==False:
      print(f"Sorry {books[theb]['name']} Is NOT available")
    else:
      print(f"Sorry I can't Find {theb} ")

def check_in():
  clear_screen()
  theb=int(input("Enter ISBN To check in :"))
  if theb in books:
    if books[theb]['available']==False:
      print(f"{books[theb]['name']} Checked in Successfully !")
      books[theb]['available']=True
    elif books[theb]['available']==True:
      print(f"{books[theb]['name']} Already available !")
  else:
    print(f"Sorry I Can't Find {theb}")
  

  
def home():
  print("Menu:")
  print("1. Add Book")
  print("2. Check Out Book")
  print("3. Check In Book")
  print("4. List Books")
  print("5. Exit")

while True:
  home()
  choice=int(input(":"))
  #Adding An Book
  if choice==1:
    while True:
      add_book()
      keep_going=input("Do you Want To Add Anthor Book?(y/n)").lower()
      if keep_going=='n':
        break
  #list books
  elif choice==4:
    list_books()
  #Check out Book 
  elif choice ==2:
    while True:
      check_out()
      keep_going=input("Do you Want To check out Anthor Book?(y/n)").lower()
      if keep_going=='n':
        break
  #Check In Book
  elif choice==3:
    while True:
      check_in()
      keep_going=input("Do you Want To check out Anthor Book?(y/n)").lower()
      if keep_going=='n':
        break
  elif choice==5:
    print("\n Exit The Program....")
    break
  else:
    print("Invalid Choice !")
