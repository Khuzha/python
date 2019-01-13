import keyword

keyword.kwlist # ['False', 'None', 'True', 'and', 'as'...]

a = 5
float(a) # 5.0

list(range(0, 1000, 5)) # [0, 5, 10, 15, 20, 25, 30, 35... 995]

any([False, False, None, 'some text']) # True - one of elements is True
any([]) # False - list ist empty
all(['some text', 5, True]) # True - all elements are True
all([]) # True - no element in the list


print(bin(2000))