from customer import Customer
from cakemag import CakeMag

def Admin():

    choice = 0
    cakeshop = CakeMag()
    while(choice != 6):
        print("\t\t1.Add an cake")
        print("\t\t2.Delete an cake")
        print("\t\t3.Edit an cake")
        print("\t\t4.Search an cake")
        print("\t\t5.Display all cake")
        print("\t\t6.Exit")
    
        choice = int(input("enter your choice"))

        if(choice == 1):
            id = int(input("enter id of cake"))
            name = input("enter name of cake")
            price = int(input("enter price of cake"))
            qnt = int(input("enter quantity of cake"))

            C = Customer(id, name, price, qnt)
            cakeshop.Addcake(C)

        elif(choice == 2):
            id = int(input("enter id to be deleted"))
            cakeshop.Deletecake(id)

        elif(choice == 3):
            cid = int(input("enter the id u want to edit"))
            cakeshop.Editcake(cid)

        elif(choice == 4):
            print("\ta serch by name")
            print("\tb search by id")
            ans = input("enter your choice")
            if(ans.lower() == "a"):
                name = input("enter name to be search")
                cakeshop.Searchcakename(name)
            elif(ans.lower() == "b"):
                id = int(input("enter id to be search"))
                cakeshop.Searchcakeid(id)
            else:
                print("invalid input")

        elif(choice == 5):
            cakeshop.ShowAllcake()

        elif(choice == 6):
            print("----thank you----")
