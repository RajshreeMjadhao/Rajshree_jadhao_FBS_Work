# 1. Create a class Book with members as bid,bname,price and author.Add following
# methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook
# d. Add static variable count and also maintain count of objects created.

class Book:
    count = 0  
    def __init__(self, bid, bname, price, author):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        Book.count += 1  

    def __del__(self):
        Book.count -= 1
        print("Destructor Called")

    def getData(self):
        print("Book ID:", self.bid)
        print("Book Name:", self.bname)
        print("Price:", self.price)
        print("Author:", self.author)

   
    @staticmethod
    def showCount():
        print("Total Book Objects:", Book.count)



b1 = Book(1, "Wings of Fire", 300, "Abdul Kalam")
b2 = Book(2, "TCOLG", 220, "Prashant Paras")

b1.getData()
Book.showCount()
