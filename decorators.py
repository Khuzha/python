def wrap_the_function(function_to_decorate):
    def wrapper(*args):
        print('I`m before main function')
        function_to_decorate(*args)
        print('I`m after main function')
    return wrapper

@wrap_the_function
def print_text_x_times(text, x):
    for i in range(x):
        print(text)

print_text_x_times('kek', 3)

