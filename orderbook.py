import time
import itertools
import heapq
import random

def random_orders(n=100000):
    sides = ["BUY", "SELL"]
    for _ in range(n):
        side = random.choice(sides)
        qty = random.randint(1, 1000)
        price = round(random.uniform(10, 100), 2)
        yield Order(side, qty, price)

def parse_order(line):
    side, rest = line.strip().split()
    qty, price = rest.split("@")
    return Order(side, int(qty), float(price))


class OrderBook:
    def __init__(self):
        self.buys = []
        self.sells = []

    def add_order(self, order):
        if order.side == "BUY":
            heapq.heappush(self.buys, (-order.price, order.timestamp, order))
        else:  # SELL
            heapq.heappush(self.sells, (order.price, order.timestamp, order))

    def process_order(self, order):
        trades = []

        if order.side == "BUY":
            while order.qty > 0 and self.sells and self.sells[0][0] <= order.price:
                best_price, _, sell_order = heapq.heappop(self.sells)
                trade_qty = min(order.qty, sell_order.qty)

                order.qty -= trade_qty
                sell_order.qty -= trade_qty
                trades.append((trade_qty, best_price))

                if sell_order.qty > 0:
                    heapq.heappush(self.sells, (best_price, sell_order.timestamp, sell_order))

        else:
            while order.qty > 0 and self.buys and -self.buys[0][0] >= order.price:
                best_price, _, buy_order = heapq.heappop(self.buys)
                best_price = -best_price 

                trade_qty = min(order.qty, buy_order.qty)
                order.qty -= trade_qty
                buy_order.qty -= trade_qty
                trades.append((trade_qty, best_price))

                if buy_order.qty > 0:
                    heapq.heappush(self.buys, (-best_price, buy_order.timestamp, buy_order))

        if order.qty > 0:
            self.add_order(order)

        return trades

    def __repr__(self):
        buys_sorted = sorted(self.buys, reverse=True)
        sells_sorted = sorted(self.sells)
        return (f"BUYS: {[o for _, _, o in buys_sorted]}\n"
                f"SELLS: {[o for _, _, o in sells_sorted]}")

class Order:
    _ids = itertools.count(0)

    def __init__(self, side, qty, price, timestamp=None):
        self.id = next(Order._ids)
        self.side = side
        self.qty = qty
        self.price = price
        self.timestamp = timestamp or time.time()

    def __repr__(self):
        return f"{self.side} {self.qty}@{self.price:.2f} (id={self.id})"

def benchmark(n=100000):
    book = OrderBook()
    start = time.perf_counter()
    for order in random_orders(n):
        book.process_order(order)
    end = time.perf_counter()
    elapsed = end - start
    print(f"Processed {n} orders in {elapsed:.4f} seconds "
          f"({n/elapsed:.0f} orders/sec)")


if __name__ == "__main__":
    print("\n--- Benchmark ---")
    benchmark(100000)
    print("\n--- Processing orders.txt ---")
    book = OrderBook()
    with open("orders.txt") as f:
        for line in f:
            if not line.strip():
                continue  # skip empty lines
            order = parse_order(line)
            trades = book.process_order(order)

            for qty, price in trades:
                print(f"TRADE {qty} @ {price:.2f}")

    print("\nFinal Order Book:")
    print(book)

