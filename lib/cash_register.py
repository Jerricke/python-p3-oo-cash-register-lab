#!/usr/bin/env python3


class CashRegister:
    def __init__(self, discount=0, total=0):
        self.discount = discount
        self.total = total
        self.items = []
        self.transaction = {}

    def add_item(self, title, price, qty=1):
        self.total = self.total + price * qty
        for n in range(qty):
            self.transaction[title] = self.transaction.get(title, 0) + price
            self.items.append(title)

    def apply_discount(self):
        if self.discount != 0:
            self.total -= self.total * self.discount / 100
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        last_transaction = self.transaction.get(self.items[-1])
        print(self.transaction)
        self.total = self.total - last_transaction
        print(self.total)

    pass


if __name__ == "__main__":
    mac = CashRegister(20)
    mac.add_item("tomato", 1.76, 2)
    print(mac.total)
    print(mac.transaction)
    print(mac.void_last_transaction())
