import random
import time

class Stock:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price

    def update_price(self):
        # Simulate random price fluctuations (±5% change)
        change_percent = random.uniform(-0.05, 0.05)
        self.price += self.price * change_percent
        self.price = round(self.price, 2)

    def __str__(self):
        return f"{self.symbol}: ${self.price}"

class User:
    def __init__(self, name):
        self.name = name
        self.balance = 10000  # Starting balance
        self.portfolio = {}  # Track stocks owned (symbol: quantity)

    def buy_stock(self, stock, quantity):
        total_cost = stock.price * quantity
        if total_cost <= self.balance:
            self.balance -= total_cost
            if stock.symbol in self.portfolio:
                self.portfolio[stock.symbol] += quantity
            else:
                self.portfolio[stock.symbol] = quantity
            print(f"Bought {quantity} shares of {stock.symbol} at ${stock.price} each.")
        else:
            print("Insufficient funds to complete the purchase.")

    def sell_stock(self, stock, quantity):
        if stock.symbol in self.portfolio and self.portfolio[stock.symbol] >= quantity:
            total_sale = stock.price * quantity
            self.balance += total_sale
            self.portfolio[stock.symbol] -= quantity
            if self.portfolio[stock.symbol] == 0:
                del self.portfolio[stock.symbol]
            print(f"Sold {quantity} shares of {stock.symbol} at ${stock.price} each.")
        else:
            print(f"Not enough shares of {stock.symbol} to sell.")

    def print_portfolio(self):
        print(f"Portfolio of {self.name}:")
        for symbol, quantity in self.portfolio.items():
            print(f"{symbol}: {quantity} shares")
        print(f"Balance: ${self.balance}")

class StockMarket:
    def __init__(self):
        self.stocks = {}
        self.users = {}

    def add_stock(self, symbol, price):
        self.stocks[symbol] = Stock(symbol, price)

    def get_stock(self, symbol):
        return self.stocks.get(symbol)

    def add_user(self, user):
        self.users[user.name] = user

    def update_stock_prices(self):
        # Update all stock prices randomly
        for stock in self.stocks.values():
            stock.update_price()

    def show_stock_prices(self):
        print("Stock Market Prices:")
        for stock in self.stocks.values():
            print(stock)

    def simulate_market(self):
        # Simulate the market for 10 rounds
        for _ in range(10):
            self.update_stock_prices()
            self.show_stock_prices()
            time.sleep(2)  # Wait for 2 seconds before next round

# Example usage
if __name__ == "__main__":
    # Create a Stock Market
    market = StockMarket()

    # Add some stocks to the market
    market.add_stock("AAPL", 150.00)
    market.add_stock("GOOGL", 2800.00)
    market.add_stock("AMZN", 3500.00)

    # Create a user
    user = User("John Doe")

    # Add user to the market
    market.add_user(user)

    # User buys some stocks
    user.buy_stock(market.get_stock("AAPL"), 10)
    user.buy_stock(market.get_stock("GOOGL"), 5)

    # User sells some stocks
    user.sell_stock(market.get_stock("AAPL"), 5)

    # Print user portfolio
    user.print_portfolio()

    # Simulate the market
    market.simulate_market()
