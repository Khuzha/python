# ------------ My first function --------------

def print_the_text_n_times(text, quantity):
    """
    This function prints recieved text quantity-times
    """
    i = 0
    while (i < quantity):
        print(text)
        i += 1

print_the_text_n_times('lol', 10)

# ---------------------------------------------



# --------------- Arguements ------------------

def test(a, b, c = 3, d = 4):
    """
    This function prints all recieved arguements
    """
    print('a = ', a)
    print('b = ', b)
    print('c = ', c)
    print('d = ', d)
    print('-------')

# test() - TypeError
test(1, 2) # a = 1, b = 2, c = 3, d = 4
test(b = 6, c = 10, a = 5) # a = 5, b = 6, c = 10, d = 4
# test(1, d = 5) - TypeError
test(10, 15, 20, 25) # a = 10, b = 15, c = 20, d = 25

# ---------------------------------------------



# ------------ Without return -----------------

# If function hasn`t return, it`s value will be "None"
def return_nothing(arg):
    print(arg)

a = return_nothing('lol')
print(a) # None

# ---------------------------------------------



# -------------- Unpacking --------------------

def check(name, profession, university = 'TashIIT'):
    if university == 'TashIIT':
        return (True, 'Ok') # this is tuple
    else:
        return (False, 'Kein Zutritt') # also tuple

okay, message = check('Sardor', 'developer', university = 'TashIIT') 
# This was unpacking one tuple into some variables
print (okay, ',', message)

okay, message = check('Sardor', 'weiss nicht', 'MIT')
print(okay, ',', message)

# ---------------------------------------------



# ------------ *args and *kwargs --------------
# Arguement with one * (e.g. *args) will be tuple
# Arguement with two * (e.g. **kwargs) will be dictionary

def second_function(a, b, *args):
    print('a =', a, ', b =', b)
    print('other arguements:', args) # ('lol', 'kek', 5, [10, 15, 20])
    return 'okay'

print(second_function(1, 2, 'lol', 'kek', 5, [10, 15, 20]))

def third_function(a, b, **kwargs):
    print('a =', a, ', b =', b)
    print('other arguements:', kwargs) # {'name': 'Sardor', 'age': 18, 'height': 177, 'langs': ['Uzbek', 'German', 'English', 'Russian']}
    return 'super'

print(third_function(1, 2, name = 'Sardor', age = 18, height = 177, langs = ['Uzbek', 'German', 'English', 'Russian']))
# ---------------------------------------------



# ------- Don`t use editable arguements -------

def print_list(a = []):
    a.append(1)
    print(a)

print_list() # [1]
print_list() # [1, 1]
print_list() # [1, 1, 1]

# ---------------------------------------------



# ----------------- Lambdas -------------------
# Don`t do so! Don`t assign lambdas to variable. 
# Don`t give them name, they`re as anonymus functions
double = lambda x: x*2
print(double(5)) # 10
map(double, [1, 2, 3]) # [2, 4, 6]
print(list(map(double, [1, 2, 3])))

# ---------------------------------------------



# ------------------- Lol ---------------------

a = map(int, [1, 2, 3])
print(list(a)) # [1, 2, 3]
print(list(a)) # []

# ---------------------------------------------
