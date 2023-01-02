import random
print(random.randrange(1, 9))


# strings are arrays

j = "Happy new year 2023"
print(j[6])

# looping through strings

for x in "2023":
    print(x)


# Check string len
b = 'New Year'
print(len(b))


#Locate a given word in a string

year = 'The best offer of the year with free addons'
print('uth' in year)


if "free" in year:
    print("Yes, 'mk' offers available.")
else:
    print('No free offers')
    
# if not

y = 'Annual presidential scholarship is awarded to excellent students.'
print('Excellent' not in y)


if 'Exellent' not in y:
    print('No, exellent NOT present')
else:
    print('Yes, Exellent present')
