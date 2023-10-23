def myfunction(**kwargs):
    print(kwargs)

myfunction(**"Bob") # Error, must be mapping
myfunction(**None) # Error