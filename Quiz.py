class 붕어빵:
    def __init__(self, taste, price):
        self.taste = taste
        self.price = price
        self.total = 0
    def sell(self):
        self.total += self.price
        print(f"{self.taste}을 {self.price}에 팔았습니다.")

    def eat(self):
        print(f"{self.taste}을 먹습니다.")

슈크림_붕어빵 = 붕어빵("슈크림", 1000)
슈크림_붕어빵.sell()
슈크림_붕어빵.sell()
슈크림_붕어빵.sell()
슈크림_붕어빵.sell()

print(슈크림_붕어빵.total)