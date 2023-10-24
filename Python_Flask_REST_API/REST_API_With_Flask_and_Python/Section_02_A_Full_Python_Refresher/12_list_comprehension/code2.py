friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = [friend for friend in friends if friend.startswith("S")]

##starts_s = []

# for friend in friends:
#     if friend.startswith("S"):
#         starts_s.append(friend)

print(starts_s)
print(friends is starts_s)
print("friends: ", id(friends), "starts_s", id(starts_s))