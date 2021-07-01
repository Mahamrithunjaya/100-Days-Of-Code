def logging_decorator(function):
    def wrapping_function(*args):
        print(f"You called {function.__name__}{args}")
        result = function(args[0], args[1], args[2])
        print(f"It returned: {result}")
    return wrapping_function


@logging_decorator
def a_function(n1, n2, n3):
    return n1 + n2 + n3


a_function(1, 2, 3)
