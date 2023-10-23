def named(**kwargs):
    print(kwargs)

# def named(name, age):
#     print(name, age)

details = {"name": "Bob", "age": 25}

named(**details)

