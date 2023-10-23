#friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob","Anne"}
local = {"Rolf"}

# local_friends = friends.difference(abroad)
# print(local_friends)
# local_friends = friends.difference(friends)
# print(local_friends)

friends = local.union(abroad)
print(friends)

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

both = art.intersection(science)
print(both)





