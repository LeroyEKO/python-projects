import re

def register():
    fn = input("Enter your first name: ")
    ln = input("Enter your last name: ")

    uname = (fn[:3])+(ln[3:])

    def pword():
        password = input("Create a password: ")

        if len(password) < 6:
            print("Password too weak. Create a longer password (longer than 6 characters). ")
            pword()

        elif not re.search('[!"£$%_^&*()@?~><]', password):
            print("Password too weak. Add special characters (symbols) to password. ")
            pword()

        elif not re.search('[1234567890]', password):
            print("Password too weak. Add numbers too your password.")
            pword()

        elif not re.search('[ABCDEFGHIJKLMNOPQRSTUVWXYZX]', password):
            print("Password too week. Add upper case letters to your password")
            pword()

        else:
            print("Password successfully created!")
            f = open("U_D.txt", "a")
            f.write("\n" + str(uname) + "," + password)
            f.close()

            print("You have been registered! ")
            print("Your username is: ", uname)
            print("Your password is: ", password)

    pword()


def login():
    uname = input("Enter your username: ")
    password = input("Enter Your password: ")
    file = open("U_D.txt","r")

    for s in file:
        a,b = s.split(",")
        b =b.strip()
        if (a == uname and b != password):
            while password != b:

                print("password is incorrect ")
                password = input("Try again : ")

                if password == b:
                   print("Logged in successfully")

        elif (uname == a and password == b):
           print("Logged in successfully")

def option():
    op = input("Do you want to log in or register:  (log/reg): ")
    if(op != "log" and op != "reg"):
        option()
    elif op.lower() == "log":
        login()
    elif op.lower() == "reg":
        register()

option()