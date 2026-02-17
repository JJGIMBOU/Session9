a = [] #simple list
print(a)
a = [1, 2, 3, 19]
print(a)
a = [-7.1, None, ["Bob", "Jane"], True, 1000]
print(a)
print(len(a))

print(a[2])
a[2] = "Now I changed the List!"
print(a)
print(a[::-1])
# Slice to only get: None, True
print(a[1::2])
#to get now I changed the list & -7.1
print(a[2::-2])
#or
print(a[::-1][2::2])

a1 = [1, 2, 3]
a2 = [4, 5, 6]

print(a1 + a2*3 + a1) # you can add lists, multiply list by an integer
for elem in a1 + a2: # you can do a for to get items from the list
    print(elem)