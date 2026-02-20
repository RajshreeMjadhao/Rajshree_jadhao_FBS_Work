# 3. Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# j. Constructor (Support both parameterized and parameterless)
# k. Destructor
# l. ShowBook
# m. For each size of shirt price should change by 10%.
# (eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and
# xlarge=1300) Use static concept.


class Shirt:
    size_price = {"Small": 0,"Medium": 10,"Large": 20,"ExtraLarge": 30}

    def __init__(self, sid, sname, stype, price, size):
        self.sid = sid
        self.sname = sname
        self.stype = stype
        self.price = price
        self.size = size.lower()
        self.upPrice()

    def upPrice(self):
        increase = Shirt.size_price.get(self.size, 0)
        self.price = self.price + (self.price * increase / 100)

    def getData(self):
        print("Shirt ID:", self.sid)
        print("Shirt Name:", self.sname)
        print("Type:", self.stype)
        print("Size:", self.size)
        print("Price:", self.price)

    # def __del__(self):
    #     print("Destructor called")


s1 = Shirt(201, "H&M", "Casual", 1250, "Small")
s1.getData()
