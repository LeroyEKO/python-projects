def register():

    fn = input("Enter your first name: ")
    ln = input("Enter your last name: ")

    uname = (fn[:3])+(ln[3:])
    password = input("Create a password: ")

    while len(password) < 6:
        print("Password is too short, must be more than 6 characters")
        password = input("Create a password: ")

        if len(password) >= 6:
            pc = input("confirm password: ")

            while pc != password:

                print("password not confirmed")
                pc = input("confirm password: ")


    f = open("UD.txt","a")
    f.write("\n" + str(uname) + "," + password )
    f.close()

    print("You have been registered! ")
    print("Your username is: ",uname)
    print("Your password is: ",password)

def login():
    uname = input("Enter your username: ")
    password = input("Enter Your password: ")
    file = open("UD.txt","r")

    for x in file:
        a,b = x.split(",")
        b = b.strip()

        if (a == uname and b != password):
            while password != b:

                print("password is incorrect ")
                password = input("Try again : ")

                if password == b:
                    print("Logged in successfully")
                    break

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