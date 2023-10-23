from operator import itemgetter

def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}.")

friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},

]

def get_friend_name(friend):
    return friend["name"]

print(search(friends, "Adam Wool", get_friend_name))

# Lambda version (no get_friend_name version needed)
# print(search(friends, "Bob Smith", lambda friend: friend["name"]))

print(search(friends, "Anne Pun", itemgetter("name")))



