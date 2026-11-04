lst = [1, 2, 3, 4]
part = lst[1:3]

print(id(lst) == id(part))
print(lst, part)

lst.pop()

print(lst, part)
