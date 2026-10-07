digits = input("Enter a 10-digit phone number: ")

area_code = digits[0:3]
prefix = digits[3:6]
line_number = digits[6:10]

print(f"({area_code}) {prefix}-{line_number}")
