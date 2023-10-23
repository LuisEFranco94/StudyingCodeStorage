def double(x):
    return x * 2

sequence = [1, 3, 5, 9]
doubled = [double(x) for x in sequence]
doubled = map(double, sequence)

doubled = [(lambda x: x * 2)(x)for x in sequence]

doubled = list(map(lambda x: x * 2, sequence))
print(doubled)