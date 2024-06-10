class GroceryList:
    def __init__(self):
        self.items = []

    def add(self, unit):
        self.items.append(unit)

    def total_cost(self):
        total = 0
        for unit in self.items:
            total += unit.cost()
        return total

    def print_grocery_list(self):
        print('=' * 40)
        print(' ' * 12 + "Tuan's Market" + " " * 12)
        print('=' * 40)
        print(f'{'Item:':<15}{'Qty':<5}{'Unit Price':<12}{'Total':<8}')
        print('=' * 40)
        for unit in self.items:
            print(f'{unit.item_name:<15}{unit.quantity:<5}{unit.price_per_unit:<12.2f}{unit.cost():<8.2f}')
        print('-' * 40)
        print(f'{'Purchase Price':<32}{self.total_cost():<8.2f}')
        print('-' * 40)


class GroceryItemOrder:
    def __init__(self, item_name, quantity, price_per_unit):
        self.item_name = item_name
        self.quantity = quantity
        self.price_per_unit = price_per_unit

    def cost(self):
        return self.quantity * self.price_per_unit

    def quantity(self):
        return self.quantity


def create_grocery_items():
    coca_cola = GroceryItemOrder('Coke', 1, 3)
    beef = GroceryItemOrder('Beef', 2, 27)
    milk = GroceryItemOrder('Milk', 1, 4)
    bread = GroceryItemOrder('Bread', 4, 4.75)
    return [coca_cola, beef, milk, bread]


if __name__ == '__main__':
    grocery_list = GroceryList()
    items = create_grocery_items()
    for item in items:
        grocery_list.add(item)

    grocery_list.print_grocery_list()
