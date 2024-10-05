
class ItemToPurchase:
    item_name = ''
    item_price = 0.0
    item_quantity = 0

    def __init__(self, item_name = None, item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
    
    def print_item_cost(self):
        '''Bottled Water 10 @ $1 = $10'''
        print(self.item_name, self.item_quantity, '@ ${:.2f}'.format(self.item_price), '= ${:.2f}\n'.format(self.item_price * self.item_quantity))
    


print('Item 1\n')

name1 = input('Enter the item name\n')
price1 = float(input('Enter the item price\n'))
quantity1 = int(input('Enter the item quantity\n'))

item1 = ItemToPurchase(name1, price1, quantity1)
print('Item 2\n')

name2 = input('Enter the item name\n')
price2 = float(input('Enter the item price\n'))
quantity2 = int(input('Enter the item quantity\n'))

item2 = ItemToPurchase(name2, price2, quantity2)

print('TOTAL COST\n')
item1.print_item_cost()
item2.print_item_cost()
print('Total: ${:.2f}\n'.format(item1.item_price * item1.item_quantity + item2.item_price * item2.item_quantity))