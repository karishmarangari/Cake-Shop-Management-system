from customer import Customer
from usermag import UserMag

def User():
    choice = 0
    cakeuser = UserMag()
    while(choice != 6):
        print("\t\t1.Show all cake")
        print("\t\t2.Search cake")
        print("\t\t3.Add to cart")
        print("\t\t4 remove from cart")
        print("\t\t5.buy cake")
        print("\t\t6.Exit")
    
        choice = int(input("enter your choice"))
        if(choice == 1):
            cakeuser.Showallcale()

        elif(choice == 2):
            print("\ta search by id")
            print("\tb search by name")
            ans = input("enter your choice")
            if(ans.lower() == "a"):
                id = int(input("enter id to be search"))
                cakeuser.Searchbyid(id)
            elif(ans.lower() == "b"):
                name = input("enter cake name to be search")
                cakeuser.Searchbyname(name)
            else:
                print("invalid search")

        elif(choice == 3):
            name = input("enter cake name")
            cakeuser.Addtocart(name)

        elif(choice == 4):
            id = int(input("enter cake id to be remove from cart"))
            cakeuser.Removecart(id)       

        elif(choice == 5):
            cakeuser.Buycake()

        elif(choice == 6):
            print("-----Thank you for visiting-----")
            exit()