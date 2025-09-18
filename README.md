# Python Order-Matching Engine

A simplified **order-matching engine** implemented in Python, simulating a live trading system.  
This project demonstrates core skills for quantitative software engineering: **data structures, algorithmic logic, performance benchmarking, and real-time system simulation**.

---

## Features

- **Order Book Management**  
  - Maintains separate **buy** (max-heap) and **sell** (min-heap) order books.  
  - Ensures orders are matched efficiently based on price and timestamp.  

- **Order Matching Engine**  
  - Automatically executes trades when buy/sell orders cross.  
  - Supports **partial fills** and leftover orders.  

- **File Input**  
  - Processes orders from a file (`orders.txt`) for batch testing.  

- **Performance Benchmarking**  
  - Processes 100k+ orders and measures throughput (orders/sec).  
  - Comparison of different data structures (`heapq` vs `bisect`) to analyze speed trade-offs.  

- **Debugging & Correctness**  
  - Assertions ensure buy orders are sorted descending, sell orders ascending.  
  - Handles tricky edge cases like multiple partial fills and same-price orders.  

- **Optional Networking Mode**  
  - Runs a simple **TCP server** to accept live orders from clients (`nc` or custom scripts).  
  - Demonstrates real-time processing of multiple orders.

---

## Installation

1. Clone the repository:

```bash
git https://github.com/DhvaniMistry/order-matching-engine.git
cd order-matching-engine
````

2. Ensure Python 3.10+ is installed.

3. (Optional) Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Usage

### 1. Batch mode (file input)

Create `orders.txt` with orders, e.g.:

```
BUY 100@10.50
SELL 50@10.40
BUY 30@10.60
SELL 80@10.55
```

Run the engine:

```bash
python3 orderbook.py
```

Output:

```
TRADE 50 @ 10.40
TRADE 30 @ 10.55
Final Order Book:
BUYS: [BUY 100@10.50 (id=0)]
SELLS: [SELL 50@10.55 (id=3)]
```

---

### 2. Performance Benchmarking

The engine automatically runs a benchmark processing 100,000 random orders:

```bash
--- Heapq Benchmark ---
Processed 100000 orders in 0.2062 seconds (484998 orders/sec)
```

---

### 3. Optional Networking Mode (Real-time orders)

Run the server:

```bash
python3 orderbook.py
```

In another terminal, connect using `nc`:

```bash
nc 127.0.0.1 9999
```

Send orders:

```
BUY 50@12.00
SELL 20@11.90
```

Server responds with:

```
TRADE 20 @ 11.90
OK
```

---

## Project Structure

```
order-matching-engine/
├─ orderbook.py       # Main engine code
├─ orders.txt         # Sample order file for testing
├─ README.md
```

---

## Skills Demonstrated

* **Python programming** (classes, data structures, heapq, bisect)
* **Algorithmic problem solving** (matching engine logic)
* **Performance analysis** (benchmarking and optimization)
* **Debugging & correctness** (assertions, edge case handling)
* **Networking** (TCP server for live order processing)
* **Real-world trading concepts** (order books, partial fills, best bid/ask)

---