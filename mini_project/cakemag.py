from customer import Customer


class CakeMag:

    def Addcake(self, C):
        with open("cdata.txt", "a") as fp:
            fp.write(str(C) + "\n")
            

    def Deletecake(self, id):
        Alldata = []
        found = False
        try:
            with open("cdata.txt", "r") as fp:
                for data in fp:
                    try:
                        data.index(str(id), 0, 4)
                    except:
                        Alldata.append(data)
                    else:
                        found = True
                        #if record is present we need tp override the file
                if(found):
                    with open("cdata.txt", "w") as fp:
                        for cdata in Alldata:
                            fp.write(cdata)
                        print("deleted sucessfully")
                else:
                    print("record not found")
        except:
            print("file does not exists")

    def Editcake(self, cid):
        Allcake = []
        found = False
        try:
            with open("cdata.txt", "r") as fp:
                for data in fp:
                    try:
                        data.index(str(cid), 0, 4)
                    except:
                        pass
                    else:
                        found = True
                        #edit data
                        data = data.split(",")
                        print(data)
                        
                        an = input("do you want to change price (y/n)")
                        if(an.lower() == "y"):
                            data[2] = input("enter new price")
                        
                        a = input("do you want to change quantity (y/n)")
                        if(a.lower() == "y"):
                            data[3] = input("enter new quantity")
                            data[3] += "\n"
                        #print(data)   
                        data = ','.join(data)
                    Allcake.append(data)
                #print(Allcake)
            if(found):
                with open("cdata.txt", "w") as fp:
                    for data in Allcake:
                        fp.write(data)
                    print("edited sucessfully")
            else:
                print("record not edit")                            
        except:
            print("file does not exists")

    def Searchcakeid(self, id):
        try:
            with open("cdata.txt", "r") as fp:
                for cake in fp:
                    try:
                        cake.index(str(id), 0, 4)
                        print(cake)
                    except:
                        pass
                    else:
                        print("found")
        except:
            print("file does not exists")
    
    def Searchcakename(self, name):
        try:
            with open("cdata.txt", "r") as fp:
                for data in fp:
                    try:
                        data.lower().index(name.lower())
                        print("found:", data)
                    except:
                        pass
                    else:
                        print("record found")
        except:
            print("file does not exists")

    def ShowAllcake(self):
        try:
            with open("cdata.txt", "r") as fp:
                print(fp.read())
        except:
            print("file does not exists")
