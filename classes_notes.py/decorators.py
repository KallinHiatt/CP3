def cough(func):
    def func_wrapper():
    #stuff that happens before the function
        print("*cough*")
        func()
    #stuff that happens after the function
    return func_wrapper


@cough
def akward():
    print("Can I get a discount?")

akward()

@cough
def answer():
    print("This is a dollar tree...")

akward()
answer()