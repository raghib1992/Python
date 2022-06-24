def new_decorator(original_func):

    def wrap_func():
        print("Some code before a function to decorate it..")
        original_func()
        print("Some code after a function to decorate it..")
    
    return wrap_func
@new_decorator
def func_need_decorator():
    print( "I am the function, kindly decorate me")

# my_func = new_decorator(func_need_decorator)
# my_func()

func_need_decorator()