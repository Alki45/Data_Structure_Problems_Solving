class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        price={}
        for i,p in enumerate(products):
            price[p]=prices[i]
        self.price=price
        self.discount=discount
        self.n=n
        self.customer_count=0


    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.customer_count += 1
        subtotal = 0
        for i,p in enumerate(product):
            subtotal += self.price[p]* amount[i]

        if self.customer_count % self.n == 0:
            subtotal *= (100 - self.discount) / 100

        return round(subtotal, 2)

        


# Your Cashier object will be instantiated and called as such:

# obj = Cashier(n, discount, products, prices)

# param_1 = obj.getBill(product,amount)