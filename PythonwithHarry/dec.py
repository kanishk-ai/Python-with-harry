# In File we will learn about Decorater's
def dec1(func1):
    def executer():
        print("Execution now")
        func1
        print("Executed")
        return executer
@dec1
def who_is_harry():
    print("harry is a good boy")

# who_is_harry = dec1(who_is_harry) # By replace of this line we use @(function name)
who_is_harry()
