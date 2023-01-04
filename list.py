# store multiple items in as single variable
# ordered, changeable, allow duplicate values
veges = ['Kales', 'pumkin', 'cabbage']
print(veges)
print(len(veges))
print(type(veges))

# list()
mylist = list(('maize', 'banana', 'rice'))
print(mylist)

# Access list
print(veges[-3:-2])
if 'pumkin' in veges:
    print('Yes pumkin in veges.')
else:
    print('No pumkin')

# Change list items
veges[1] = 'sukuma wiki'
print(veges)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
# Insert()
thislist.insert(3, 'spinach')
print(thislist)

# Append()
thislist.append('Tomato')
print(thislist)

# Extend() - add items of another list
thislist.extend(veges)
print(thislist)


# Remote()
thislist.remove('apple')
print(thislist)

# pop()
thislist.pop(1)
thislist.pop()
print(thislist)

# del
del thislist[0]
print(thislist)

# del thislist
# print(thislist)

# Clear()
thislist.clear()
print(thislist)