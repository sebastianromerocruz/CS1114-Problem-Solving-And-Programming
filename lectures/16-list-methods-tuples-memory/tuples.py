dubrovnik = ("Croatia", "Dubrovnik-Neretva", 21.35, 3, "UTC+1", "Saint Blaise")
print(dubrovnik)

for element in dubrovnik:
    print(element)

for index in range(len(dubrovnik)):
    print(f"Element #{index}: {dubrovnik[index]}")

print(dubrovnik[1:3], dubrovnik.count(3), dubrovnik.index("UTC+1"))


def get_min_and_max(values):
    return min(values), max(values)


lowest, highest = get_min_and_max([4, 9, 2])
print(lowest, highest)

print(type((5,)), type((5)))

azuna = ("Ayumu", "Setsuna", "Shizuku")
azuna[0] = "Shioriko"  # raises a TypeError: tuples are immutable
