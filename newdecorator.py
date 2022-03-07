def new_decorator(original_func):
    def wrap_func():
        print('some extra code, before the original function')
        original_func()
        print('some extra code, after the oroginal fun')
    return wrap_func()

def func_needs_decorator():
    print("i want to be decorated")
print(func_needs_decorator())

decorated_func= new_decorator(func_needs_decorator)
print(decorated_func)


