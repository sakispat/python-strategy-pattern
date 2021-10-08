import inquirer
from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def doTshirt(self): pass


# Price T-Shirt Credit/Debit Card
class TshirtCreditOrDebitCard(Strategy):
    def doTshirt(self):
        return 'Buy Credit/Debit Card'


# Price T-Shirt Money/Bank Transfer
class TshirtMoneyOrBankTransfer(Strategy):
    def doTshirt(self):
        return 'Buy Money/Bank Transfer'


# Price T-Shirt Crash
class TshirtCash(Strategy):
    def doTshirt(self):
        return 'Buy Cash'


class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def executeStrategy(self):
        return self.strategy.doTshirt()


def main():
    # Title Menu
    print('*' * 20, 'Choose the T-Shirt you want.', '*' * 20)
    print()

    # All Context Strategy Price T-Shirts
    ctx1 = Context(TshirtCreditOrDebitCard())
    ctx2 = Context(TshirtMoneyOrBankTransfer())
    ctx3 = Context(TshirtCash())

    '''
    There is a list for each t-shirts in color, size, fabric 
    where you can lectures with space as many classes. 
    In the end you can choose how to pay T-shirts
    '''
    tshirts_lists = [
        inquirer.Checkbox('color', message='What Color T-Shirt:', choices=['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']),
        inquirer.Checkbox('size', message='What Size T-Shirt:', choices=['XS', 'S', 'L', 'M', 'XL', 'XXL', 'XXXL']),
        inquirer.Checkbox('fabric', message='What Fabric T-Shirt:', choices=['Wool', 'Cotton', 'Polyester', 'Rayon', 'Linen', 'Cashmere', 'Silk']),
        inquirer.List('price', message='Price to Credit/Debit Card or Money/Bank Transfer or Cash:', choices=[ctx1.executeStrategy(), ctx2.executeStrategy(), ctx3.executeStrategy()])
    ]
    answers = inquirer.prompt(tshirts_lists)
    print(f'The T-Shirt Color {answers["color"]}, Size {answers["size"]} and Fabric {answers["fabric"]} with {answers["price"]}')


if __name__ == '__main__':
    main()
