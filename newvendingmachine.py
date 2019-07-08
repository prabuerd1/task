class VM:
    def stock_details(self):
        stocks = [{'product_code': 1, 'product': 'fruity', 'price': 20, 'stock': 20},
        {'product_code': 2, 'product': 'bovanto', 'price': 22, 'stock': 20},
        {'product_code': 3, 'product': 'mazza', 'price': 30, 'stock': 20},
        {'product_code': 4, 'product': 'slice', 'price': 32, 'stock': 20},]
        self.display(stocks)
        return stocks

    def display(self,stocks):
        print("****Welcome to Megam Cool***")
        print("Select your product based on product code below")
        print("product_code  product    price  stock")
        print("______________________________________")
        print("     1       fruity   20     ",stocks[0]['stock'])
        print("     2       bovanto  22     ",stocks[1]['stock'])
        print("     3       mazza    30     ",stocks[2]['stock'])
        print("     4       slice    32     ",stocks[3]['stock'])
        print("______________________________________")
        self.select_product(stocks)

    def select_product(self,stocks):

        product_order_list =[]
        bill = 0

        ch= int(input("Enter your cooldrings choice: "))
        if ch <=4 and ch >0:
            qty =int(input("Enter Quantity: "))

            for s1 in stocks:
                product_order_count ={'product_code':0,'product':0,'qty':0 ,'price':0, }
                if ch == s1.get('product_code') :
                    if qty <= s1.get('stock') and qty > 0 :
                        bill += qty * s1.get('price')

                        print("Your chosen product is ",s1.get('product'))
                        print("Your chosen product price is ",s1.get('price'))
                        print("Your chosen product quantity is ",qty)
                        print("Your bill value is ",bill)
                        balance = self.get_cash(bill) - bill
                        print("your balance cash is ",balance)

                        self.denomination(balance)

                        product_order_count['product_code']= s1.get('product_code')
                        product_order_count['product']= s1.get('product')
                        product_order_count['price']= s1.get('price')
                        product_order_count['qty']= qty

                        product_order_list.append(product_order_count)
                    else:
                        print("Please enter correct & less than quantity of stock avail is ",s1.get('stock'))
                        self.select_product(stocks)
        else:
            print("Sorry,please chose valid product code")
            self.select_product(stocks)

        return product_order_list

    def get_cash(self,bill):
        print("Please pay your payment of Rs",bill)
        print("The valid cash dinominations are 2000,500,200,100,50,10,5,2,1")

        coin_count_list = []
        cash = 0

        while cash <= bill:

            coin_count ={'coin':0,'count':0}
            coin = int(input("Enter your cash "))
            count = int(input("Enter cash dinomination "))

            if coin == 1 or coin == 2 or coin == 5 or coin == 10 or coin == 50 or coin == 100 or coin == 200 or coin == 500 or coin == 2000 :
                cash += (coin * count)
                coin_count['coin']= coin
                coin_count['count']= count
                coin_count_list.append(coin_count)

                if cash < bill:
                    print("need more for your bill is ", bill - cash)
            else:
                print("Please enter valid cash")

        print("Total colected cash is = ",cash)

        return cash

    def denomination(self,balance):

        coins = [2000,500,200,100,50,10,5,2,1]
        balance_count_list =[]

        for c in range(9):
            balance_count = {'coin':0,'count':0}
            if(balance >= coins[c]):
                coin_value = coins[c]
                count = int(balance / coin_value)
                balance = int(balance % (coin_value * count))
                balance_count['coin'] = coin_value
                balance_count['count'] = count
                balance_count_list.append(balance_count)
                print("balance_count=",balance_count)

        return balance_count_list


v = VM()
v.stock_details()
