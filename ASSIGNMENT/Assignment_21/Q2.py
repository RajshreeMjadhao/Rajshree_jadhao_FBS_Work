# 2. Create class television that has members to hold the model number ,screen size
# and price. Take a member function to take input from user, If more than 4 digits
# are entered for model number, if screen size is smaller than 12 inches or greater
# than 70 inches or if the price is negative or greater than 5000 Rs, then throw an
# exception.
# Write a main() that instantiates an object and allows the user to enter and display
# data. If exception is caught, replace all data member values with zero


class Television:
    def __init__(self):
        self.model_no = 0
        self.screen_size = 0
        self.price = 0

    def input_data(self):
        try:
            self.model_no = int(input("Enter model number: "))
            if self.model_no > 9999:
                raise ValueError("Model number should be 4 digits")

            self.screen_size = int(input("Enter screen size: "))
            if self.screen_size < 12 or self.screen_size > 70:
                raise ValueError("Invalid screen size")

            self.price = int(input("Enter price: "))
            if self.price < 0 or self.price > 5000:
                raise ValueError("Invalid price")

        except ValueError as e:
            print("Exception:", e)
            self.model_no = 0
            self.screen_size = 0
            self.price = 0

    def display(self):
        print(f'MODELNUMBER:{self.model_no}\nSCREEN SIZE:{self.screen_size}\nPRICE:{self.price}')

tv = Television()
tv.input_data()
tv.display()