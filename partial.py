# Pre defined operation function
def compute(operation, *args):
    if operation == 'max':
        return max(args)
    elif operation == 'add':
        return sum(args)
    elif operation == 'min':
        return min(args)


# Solution:
    
full_args = [] # creating a variable for storing all arguments iteratively
full_kwargs = {} # creating a variable for storing keyword arguments iteratively

def partial(func, *args, **kwargs):
    
    # declare the placeholder variables for *args and **kwargs as global variables
    global full_args
    global full_kwargs
    
    # This try/except block helps create a running list of all arguments/keyword arguments
    try:
        if args:
            full_args.extend(args) # extend the existing list of arguments as and when new arguments are provided
        if kwargs:
            full_kwargs.update(kwargs) # uopdate the existing keyword arguments when provided
    except:
        pass
    
    # A wrapper function to use the existing info on args/kwargs
    def func_wrapper(fkw = full_kwargs['operation'], fa = full_args):
        # edge case when no args are provided
        if fa == []:
            fa = [0]

        # inner function that finally uses the defined operation function
        def wrap_func(*args):
            if args and isinstance(args, int):
                # print("case 1")
                return compute(fkw, *list(fa+[args]))
            elif args and isinstance(args, list):
                # print("case 2")
                return compute(fkw, *list(fa+args))
            else:
                # print("case 3")
                return compute(fkw, *fa)
            
        return wrap_func
    
    return func_wrapper()


""" 
Write a function "partial" that takes the following inputs:
1. A callable function already defined
2. optional key word arguments
3. optional arguments
and outputs a new callable function.

The function should partially execute with any *args or **kwargs provided historically up until the point that function is called

For eg:
Say a function called "compute" already exists which is defined below

def compute(operation, *args):
    if operation == 'max':
        return max(args)
    elif operation == 'add':
        return sum(args)
    elif operation == 'min':
        return min(args)

this function has a keyword argument called 'operation' and some optional arguments to compute the operation over.
We want to design the partial function like so:

result = partial(compute, operation = 'add')
result = partial(result, 2, 4, 6)
print(result()) # It should print 2+4+6 = 12

result = partial(result, 3, 2)
print(result()) # It should print 2+4+6+3+2 = 17

print(result(11)) # It should print 2+4+6+3+2+11 = 28
"""
result = partial(compute, operation = 'max')
result = partial(result, 3, 6, 2, 5)
print(result())
result = partial(result, 4, 8, 11, 12)
print(result())
result = partial(result, 10, 3, 12, 15)
print(result())