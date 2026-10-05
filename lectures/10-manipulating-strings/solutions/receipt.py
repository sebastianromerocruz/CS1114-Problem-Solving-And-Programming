store_name = "The Corner Shop"

item1 = "Apple Juice"
price1 = 3.5

item2 = "Granola Bar"
price2 = 1.75

item3 = "Sparkling Water"
price3 = 2.0

tax_rate = 0.08

subtotal = price1 + price2 + price3
tax = subtotal * tax_rate
total = subtotal + tax

tax_row_header = f"Tax ({tax_rate:.2%})"

print(f"{store_name:^30}")
print(f"{item1:<20}${price1:>8.2f}")
print(f"{item2:<20}${price2:>8.2f}")
print(f"{item3:<20}${price3:>8.2f}")
print('-' * 30)
print(f"{'Subtotal':<20}${subtotal:>8.2f}")
print(f"{tax_row_header:<20}${tax:>8.2f}")
print(f"{'Total':<20}${total:>8.2f}")
