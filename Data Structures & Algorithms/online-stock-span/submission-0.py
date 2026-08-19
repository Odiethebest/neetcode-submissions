class StockSpanner:

    def __init__(self):
        self.arr = []

    def next(self, price: int) -> int:
        self.arr.append(price)
        i = len(self.arr) - 2
        while i >= 0 and self.arr[i] <= price:
            i -= 1
        return len(self.arr) - i - 1