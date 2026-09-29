library = []
def add_books():
    book = input("enter book name to be added")
    library.append(book)
    print(f"'{book}' has been added")

def issue_book():
    book = input("enter book name to be issurd:")
    if book in library:
        library.remove(book)
        print(f"'{book}' has been issued")
    else:
        print("book not found")

def return_book():
    book = input("enter book name to be returned:")
    library.append(book)
    print(f"'{book}' has been return")  

def view_books():
    if not library:
        print("no book are present in the library")

    else:
        print("list of books")
        idx = 1
        for book in library:
            print(f"{idx}.{book}")
            idx +=1

        print() 

while(True):
    print("-------library management system--------")
    print("1. add book")
    print("2. issue book")
    print("3. return book") 
    print("4. view books")
    print("5.exit")  

    choice = int(input("enter your choice :"))

    if choice == 1:
        add_books()  
    elif choice == 2:
        issue_book() 
    elif choice == 3:
        return_book()           
    elif choice == 4:
        view_books()
    elif choice == 5:
        print("exiting library system")
        break

    else:
        print("invalid choice")




            

        



    