#!python3

class Buyer:
    def __init__(self, val, name, age):
        self.value = val
        self.name = name
        self.age = age
        self.support = 100 if age<20 else (150 if age>60 else 0)
        self.virtual_value = 2*val-1000
        self.expected_profit = self.virtual_value + self.support

    def threshold_value(self, threshold_profit):
        return (threshold_profit + (1000-self.support))/2


def sellHouse(buyers:list):
    """
    :param buyers: list of potential buyers

    >>> sellHouse ([Buyer(400,"a",30)])
    No buyer gets the house
    >>> sellHouse ([Buyer(600,"a",30)])
    a gets the house and pays 500.0
    >>> sellHouse ([Buyer(600,"a",30),Buyer(400,"b",30)])
    a gets the house and pays 500.0
    >>> sellHouse ([Buyer(600,"a",30),Buyer(700,"b",30)])
    b gets the house and pays 600.0

    >>> sellHouse ([Buyer(400,"a",10)])
    No buyer gets the house
    >>> sellHouse ([Buyer(600,"a",10)])
    a gets the house and pays 450.0
    >>> sellHouse ([Buyer(600,"a",10),Buyer(400,"b",10)])
    a gets the house and pays 450.0
    >>> sellHouse ([Buyer(600,"a",10),Buyer(700,"b",10)])
    b gets the house and pays 600.0

    >>> sellHouse ([Buyer(600,"a",10),Buyer(550,"b",70)])
    a gets the house and pays 575.0
    """
    # max_value_buyer = max(buyers, key = lambda buyer: buyer.value)
    # Find the buyer with the largest value

    buyers.sort(key = lambda buyer: buyer.expected_profit, reverse=True)
    # Order the buyers from high profit to low profit

    max_profit_buyer = buyers[0]
    if max_profit_buyer.expected_profit > 0:
        if len(buyers) >= 2:
            second_profit_buyer = buyers[1]
            threshold_profit = max(0,second_profit_buyer.expected_profit)
            price = max_profit_buyer.threshold_value(threshold_profit)
        else:
            price = max_profit_buyer.threshold_value(0)
        print(max_profit_buyer.name+" gets the house and pays "+str(price))
    else:
        print("No buyer gets the house")



if __name__=="__main__":
    sellHouse ([Buyer(600,"a",40),Buyer(450,"b",40)])
