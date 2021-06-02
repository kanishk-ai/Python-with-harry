# First we will see about Args
# def function_name_print(a,b,c,d):
#     print(a,b,c,d)
# function_name_print("harry","kanishk","sudi","harry")
# But if we want to add some more argumentes it show error
# To solve this problem devloper introduce *args
# def function1(*args):
#     print(args)
#
# list1 = ["harry","kanishk"]
# function1(*list1)
# if we want to add as dictonary so it create some problem
# to solve introduction to **kargs
# This is a order[normal,*args,**kargs]
def function1(normal,*args,**kwargs):
    print(kwargs)
    print(type(kwargs))

# list1 = {"harry":"coder","kanishk":"learner"}
# function1(0000,**list1)
#
# list4 = ("harry","kanishk")
# function1(**list4)
# Error : rgument after ** must be a mapping, not list