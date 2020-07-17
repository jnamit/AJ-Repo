import inspect

# useful to print all params passed to a function
# And the function call stack
def foo(a, b, c, d):
    print("Inside function " + inspect.stack()[0][3] + ". Input params are:"+ str(locals()))
    print(locals()['b'])
    my_var = "my_var_value"
    # Basically locals() is a dict of all variables locally available. Any new ones you create will get added to it
    # Useful to print state of all vars in a function
    print("locals() ver 2 = ", locals())

    print("Current function name is " + inspect.currentframe().f_code.co_name)

    # print the entire function call stack
    print("inspect.stack() = " + str(inspect.stack()))

    print("Current function name AGAIN is " + inspect.stack()[0][3] + ", and was called by " + inspect.stack()[1][3])

def bar():
    foo(10, "Amit", 20, "Jain")

bar()