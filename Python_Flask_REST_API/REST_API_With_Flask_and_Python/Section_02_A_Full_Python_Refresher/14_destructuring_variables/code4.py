person = ("Bob", 42, "Mechanic")
name, _, profession = person
print(name, profession)

head, *tail = [1, 2, 3, 4, 5]
print(head)
print(tail)

*head, tail = [1, 2, 3, 4, 5]
print(head)
print(tail)
