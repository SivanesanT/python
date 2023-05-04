#51.abstraction and encapsulation in python
# abstraction means namma run time la use pannurathu but encapsulation means namma code aluthurathu
class library:
    def __init__(self,books):
        self.book=books

    def list_books(self):
        print("available Books:")
        for books in self.book:
            print(books)

    def borrow_book(self,borrow_book):
        if borrow_book in self.book: #kudutha input at the borrow book  in run time athu in the list book la available lannum pakkurom
            print("You get the book")
            self.book.remove(borrow_book)
        else:
            print("Book is not available")

    def receive_book(self,receive_book):
        print("you have returned the book")
        self.book.append(receive_book)

books=['c','c++','java','python']

o=library(books)
msg="""
      1.display book
      2.Borrow book
      3.Return book
    """
while True:
    print(msg)
    ch=int(input("Enter the choice:"))
    if ch==1:
        o.list_books()
    elif ch==2:
        book=input("enter the book name to borrow: ")
        o.borrow_book(book)
    elif ch==3:
        book=input("enter the book name to return:")
        o.receive_book(book)
    else:
        print("thank you come again")
        quit()












