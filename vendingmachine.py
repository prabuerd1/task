
class Stock:
    def display_stocks():
        stocks = [{'item_code': 1, 'item': 'fruity', 'price': 20, 'stock': 20},
        {'item_code': 2, 'item': 'bovanto', 'price': 22, 'stock': 20},
        {'item_code': 3, 'item': 'mazza', 'price': 30, 'stock': 20},
        {'item_code': 4, 'item': 'slice', 'price': 32, 'stock': 20},]

        print("item_code item  price  stock")

        for items in stocks:
            print(items.get('item_code'),items.get('item'), items.get('price'), items.get('stock'))

        return 0

    def update_stock(self):
        # after purchase stock will updated in stock
        return

    def stock_check(self):
        #before purchase itel will be checked in stock if availabile or not
        return

    def get_item(self):
        #item will get from stock for purchase
        return
s = Stock
s.display_stocks()


class Cash:
    def insert_cash(self):
        coins =[1,2,5,10,50,100]
        #gets cash from user as input
        return

    def calculate(self):
        #calculate the total cash by user input
        return

    def cash_denomination(self):
        # gives dinomonation for cash
        return

class Sales:
    def get_order(self):
        #gets purchase order from user
        return

    def bill_value(self):
        #based on products calculate the bill value
        return

    def balance_cash(self):
        #based on the bill value
        return
    def order_details(self):
        #display the final order deails after finish transactions
        return
