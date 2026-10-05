ticker1 = "AAPL"
shares1 = 50
price1  = 189.3046

ticker2 = "GOOGL"
shares2 = 10
price2  = 2741.8800

ticker3 = "TSLA"
shares3 = 25
price3  = 242.5000

ticker4 = "AMZN"
shares4 = 8
price4  = 3421.1264

value1 = shares1 * price1
value2 = shares2 * price2
value3 = shares3 * price3
value4 = shares4 * price4
total_value = value1 + value2 + value3 + value4

print(f"{'Ticker':<8}{'Shares':>8}{'Price':>12}{'Value':>14}")
print(f"{ticker1:<8}{shares1:>8}{price1:>12,.2f}{value1:>14,.2f}")
print(f"{ticker2:<8}{shares2:>8}{price2:>12,.2f}{value2:>14,.2f}")
print(f"{ticker3:<8}{shares3:>8}{price3:>12,.2f}{value3:>14,.2f}")
print(f"{ticker4:<8}{shares4:>8}{price4:>12,.2f}{value4:>14,.2f}")
print('-' * 44)
print(f"{'Total Portfolio Value:':<32}${total_value:,.2f}")
