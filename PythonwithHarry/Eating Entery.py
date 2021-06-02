#Here we are making function to getdate and time
def getdate():
    import datetime
    return datetime.datetime.now()
# Here WE are making function to |Add| or |see| log of data entry
def eatingEn():
    in1 = input("\n\n\n|||You Want to add or see log or del all Entry ||\n")
    if in1 == "add":
        inn1 = input("Enter Thing to add \n")
        op = open("Entry.txt", "a")
        op.write(str([str(getdate())]) + "  :  " + inn1 + " \n ")
        print("!!Succesfully Added!!\n\n")
    elif in1 == "see":
        op = open("Entry.txt", "r")
        see = op.readlines()
        for items in see:
            print(items)
    elif in1 == "del all Entry":
        with open("Entry.txt","w") as op:
            op.write("")
            print("!!Succesfully deleated!!")
    else:
        print("Invalid argument")
# We are running the fuction we have already made
eatingEn()
in2 = input("Y to run again and N to exit\n")
Up = in2.upper()
#Here We are making Saying that we have made if y so run it again of n to Exit
if Up=="Y":
    eatingEn()
elif Up=="N":
    print("See you later")
else :
    print("Invalid")