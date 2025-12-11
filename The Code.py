import os
books={}
def clear_screen():
  os.system("cls" if os.name=="nt" else "clear")
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
    clear_screen()
    while True:
      clear_screen()
      isbn=int(input("Enter ISBN :"))
      titl=input("Enter The Titl :")
      author=input("Enter The Author :")
      books[isbn]={}
      books[isbn]['name']=titl
      books[isbn]['katp']=author
      books[isbn]['available']=True
      print(f" The Book '{books[isbn]['name']}' By '{books[isbn]['katp']}' Has Added Successfully!")
      dis=input("Do You Want To Add More Books? (y/n)")
      if dis=='n':
        break

  #list books
  elif choice==4:
    clear_screen()
    for var in (books):
      print(f"ISBN: {var}, Titl: {books[var]['name']}, Author: {books[var]['katp']} ")
  #Check out Book 
  elif choice ==2:
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
  #Check In Book
  elif choice==3:
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
  elif choice==5:
    print("\n Exit The Program....")
    break
  else:
    print("Invalid Choice !")
