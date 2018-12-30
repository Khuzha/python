# ------------------ Example -------------------
employees = [
    {
        'name': 'Sardor',
        'age': 18,
        'languages': ('Uzbek', 'English', 'German', 'Russian') 
    },
    {
        # ...
    }
]
# ----------------------------------------------



# ------------------- Notes --------------------
value = 1, # it`s a tuple
# better to write tuples so:
value = (1)
value = {} # it`s an empty dictionary
value = set() # it`s an empty set 
print(value) # set()
# ----------------------------------------------



# In (includes?)
2 in [1, 2, 3] # True
2 in (1, 2, 3) # True
'weight' in {'name': 'Sardor', 'age': 18} # False
True in {True, None, 42} # True



# Slices:
myList = [1, 2, 3, 4, 5]
myList[0:2] # [1, 2] - new list from first to second arguement. Second arguement is excluded
myList[:3] # [1, 2, 3] - new list from first (0) element to element with number of second arguement. Second arguement is also excluded
myList[1:-1] # [2, 3, 4] - (-1 is the last element, but it`s excluded, first arguement is included) second arguement begins from the end (here - penultimate element) 
myList[0::2] # [1, 3, 5] - every second element. Second arguement indicates interval
myList[::-2] # [5, 3, 1] - every second element beginning from the end
myList[::-1] # [5, 4, 3, 2, 1] - all elements beginning from the end
# ----------------------------------------------



# ------------ Iteration: for...in -------------
# for key in [1, 2, 3] # 1, 2, 3
# for key in {'name', 10, True} # 'name', 10, True
# for key in {'name': 'Sardor', 'age': 18} # 'name', 'age'
# for key in ('lol', 10, True) # 'lol', 10, True

# newList = (1, 2, 3, 4, 5)
# for key in newList[::-2] # 5, 3, 1
# ----------------------------------------------


# --------- Unpacking Lists and Tuples ---------
a, b = [1, 2] # a = 1, b = 2
age, weight, _, _, city = (35, 75, None, None, 'Munich') # age = 35, weight = 75, _ isn`t any value
a, b = b, a + b
# a, b = (1, 2, 3) # ValueError: too many values to unpack
# a, b, c, d = (1, 2, 3) # ValueError: not enough values to unpack
# ----------------------------------------------


# ------------------- Lists --------------------
# like arrays in java & js
firstList = [1, 10, 15]

print('First element (0) = ', firstList[0])
firstList[0] = 5
print('First element (0) = ', firstList[0])

print('full list:', firstList)
firstList.append(20)
print('full list after .append():', firstList)

firstList.extend([25, 30, 35]) # adds new list to the end of old list
print('full list after .extend():', firstList)

firstList.insert(0, 40) #first arguement - position, second - value
print('full list after .insert():', firstList)

firstList.sort()
print('full list after .sort():', firstList)

# list.pop() returns last value of list and removes this value from list
print('last value:', firstList.pop())
print('full list after .pop():', firstList)

print('adding one list to other:', firstList + [40, 45, 50])
# ----------------------------------------------



# ------------------- Tuples -------------------
# like lists, but non-editable
firstTuple = (5, 10, 15) # standard declaration
print(firstTuple)
print('first element of tuple =', firstTuple[0])

secondTuple = firstTuple + (20, 25, 30)
print(secondTuple)

# firstTuple[0] = 5 - Exeprion, because tuples aren`t editable
# ----------------------------------------------



# ----------------- Dictionaries -----------------
firstDictionary = {
    'name': 'Sardor',
    'age': 18,
    'height': 177,
    }

print(firstDictionary['age'])

firstDictionary['weight'] = 75
print('full dictionary:', firstDictionary)
firstDictionary.update({'weight': 74})
print('full dictionary after .update():',firstDictionary)

# print(firstDictionary[lolkek]) - KeyError. Use instad this:
print(firstDictionary.get('lolkek')) # 'None', without exceptions

print('keys of dictionary:', firstDictionary.keys()) # returns list of keys
print('values of dictionary:', firstDictionary.values()) # returns list of values
# list of values and list of keys aren`t synchronized. They can be in diffedent order

print('items of dictionary:', firstDictionary.items())
print('.pop(\'age\') result:', firstDictionary.pop('age')) # returns values of this key and removes key and values from dictionary
print('whole dictionary after .pop():', firstDictionary)
# ------------------------------------------------


# --------------------- Sets ---------------------
# keeps only non-repeating values. Also they should be non-editable
firstSet = {5, 10, 15}
print('whole set:', firstSet)

print({10, 15, 20, 20, 15, 10, 5}) # {10, 20, 5, 15}
firstSet.add(20) # {5, 10, 15, 20}

print(firstSet & {15, 20, 25, 30}) # {20, 15} - intersections of some sets. Only same values

# '|' adds one set to other
print(firstSet | {15, 20, 25})
# '-' subtracts one set from other
print(firstSet - {15, 20, 25, 30}) # nonexistent values are ignored
# -----------------------------------------------