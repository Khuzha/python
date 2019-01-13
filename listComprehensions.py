import itertools

# -------------------- Generators -------------------- 
gen = (x for x in [1, 2, 3])
# Man schreibt das im (), aber das ist kein 'set'! Das ist 'generator'.
print(gen) # <generator object <genexpr> at 0x7fb09bdfa3b8>
# print(gen[0]) - TypeError: 'generator' object is not subscriptable
# len(gen) - TypeError: object of type 'generator' has no len()
listFromGen = list(gen)
print(listFromGen) # [1, 2, 3]

for x in gen:
    print(x)
    # This prints nothing because upper you`ve already iterated this generater
    # and generaters are cleaned after iteration


print(range(100))

# ----------------------------------------------------

print(combinations('ab', 3))

# --------------- List comprehensions ----------------

# ----------------------- Lists ---------------------- 
result = [x*x for x in range(10) if x>3]


[x for x in [1, 2, 3]] # [1, 2, 3]
[x*x for x in [1, 2, 3]] # [1, 4, 9]
[x for x in [1, 2, 3, 4, 5] if x%2 == 0] # [2, 4]
[x + y for x, y in ((1, 2), (2, 3), (3, 4))] # [3, 5, 7]
[x.upper() for x in ['lol', 'kek', 'haha'] if len(x) < 4] # ['LOL', 'KEK']

users = [
    {'name': 'Sardor', 'age': 18},
    {'name': 'Jakhongir', 'age': 30}
]
oldMans = [usersDict['name'] for usersDict in users if usersDict['age'] > 20] # Jakhongir

newDict = {
    'lol': 'kek',
    'count': 6
}
bust = [k for (k, v) in newDict.items() if v is not None] # ['lol', 'count']
bust2 = [key for key in newDict if newDict[key] != None] # ['lol', 'count']

# ----------------------- Sets ----------------------- 
{x for x in [1, 2, 3]} # {1, 2, 3}
{x for x in [1, 1, 2, 1, 3, 2, 3, 3, 2]} # {1, 2, 3}
list({x for x in [1, 1, 2, 1, 3, 2, 3, 3, 2]}) # [1, 2, 3]

users = [{'age': 20}, {'age': 30}]
# {user for user in users if user['age'] > 20} - TypeError: unhashable type: 'dict'. You can`t keep dicts in set



# ----------------------- Dicts ---------------------- 
{key: value for (key, value) in [('name', 'Sardor'), ('age', 20)]} # {'name': 'Sardor', 'age': 20}

mydict = {'1': 'value1', '2': 'value2'}

# string keys to int:
{int(key): mydict[key] for key in mydict} # {1: 'value1', 2: 'value2'}

# revers a dict.: key to value, value to key:
{value: key for (key, value) in mydict.items()} # {'value1': '1', 'value2': '2'}
{value: key for (key, value) in mydict.items()} # {'1': 'value1', '2': 'value2'}

# remove all keys with value == None
mydict.update({'value3': None}) # {'1': 'value1', '2': 'value2', 'value3': None}
{key: value for (key, value) in mydict.items() if value != None} # {'1': 'value1', '2': 'value2'}