def add(x,y):
    return x + y

nums = [3,5]
print(add(*nums))

nums = {"x": 15, "y": 25}
print(add(nums["x"], nums["y"]))

nums = {"x": 15, "y": 25}
print(add(x=nums["x"], y=nums["y"]))

nums = {"x": 15, "y": 25}
print(add(**nums))
