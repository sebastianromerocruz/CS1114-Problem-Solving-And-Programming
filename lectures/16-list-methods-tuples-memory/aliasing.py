lst1 = [1, 2, 3]
lst2 = lst1
lst3 = [1, 2, 3]

print(id(lst1) == id(lst2))
print(id(lst1) == id(lst3))

lst1.append(4)
lst2.append(5)
lst3.append(6)

print(lst1, lst2, lst3, sep='\n')
