from admin import Admin
from user import User

choice = 0
if(__name__ == "__main__"):
    print('''
    \t1 Admin section
    \t2 user section
    ''')

    choice = int(input("enter your choice"))
    if(choice == 1):
        login = input("enter your name")
        password = input("enter your password")
        if(login == "ABCD" and password == "123"):
            Admin()
        else:
            print("invalid")
    
    elif(choice == 2):
        User()
    