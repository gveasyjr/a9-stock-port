from stock_port import Stocks

stks = Stocks()
stks.buy('abc', 100, 10)
stks.print_portfolio()
stks.buy('xyz', 200, 88.0)
stks.print_portfolio()
stks.sell('abc', 50)
stks.print_portfolio()


