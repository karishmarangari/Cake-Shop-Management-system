from customer import Customer
import os


class UserMag:
    def Showallcale(self):
        try:
            with open("cdata.txt", "r") as fp:
                print("***************************")
                print('''        All Cakes      ''')
                print("***************************")
                print(fp.read())
        except:
            print("file does not exists")

    def Searchbyid(self, id):
        try:
            with open("cdata.txt", "r") as fp:
                print("***************************")
                print('''      Searches Cake    ''')
                print("***************************")
                for cake in fp:
                    try:
                        cake.index(str(id), 0, 4)
                        print(cake)
                    except:
                        pass
                    else:
                        print("record found")
        except:
            print("file does not exists")

    def Searchbyname(self, name):
        try:
            with open("cdata.txt", "r") as fp:
                print("***************************")
                print('''      Searches Cake    ''')
                print("***************************")
                for cake in fp:
                    try:
                        cake.lower().index(name.lower())
                        print(cake)
                    except:
                        pass
                    else:
                        print("record found")
        except:
            print("file does not exists")

    def Addtocart(self, name):
        Allcake = []
        found = False
        try:
            with open("cdata.txt", "r") as fp:
                for cake in fp:
                    try:
                        cake.lower().index(name.lower())
                        found = True
                        cake = cake.split(",")
                        if(int(cake[3]) == 0):
                            print("cake is not available")
                            return
                        else:
                            print("available")       
                    except:
                        pass
                    else:
                        print(cake)
                        qt = cake[-1]
                        ipqt = int(input("enter quantity"))
                        qt = int(qt) - ipqt
                        #print(qt)
                        total = int(cake[-2]) * ipqt
                        cake[3] = str(qt)
                        cake[3] += "\n"
                        
                        with open("cart.txt", "a") as fpp:
                            fpp.write(str(cake[0]) + ",")
                            fpp.write(str(cake[1]) + ",")
                            fpp.write(str(total) + ",")
                            fpp.write(str(ipqt) + "\n")
                            #fpp.write(str(Total) + "\n")
                        cake = ",".join(cake)
                    Allcake.append(cake)
                #print(Allcake)
            if(found):
                with open("cdata.txt", "w") as fp:
                    for cdata in Allcake:
                        fp.write(cdata)  
            else:
                print("not available")
            with open("cart.txt","r") as data:
                costadd = 0
                print("********************************")
                print('''            Cart            ''')
                print("********************************")
                for line in data:
                    try:
                        line = line.split(",")
                        print("\t" + "id:" + line[0] + "\t\t" + "ot:" + line[3])
                        print("\t" + line[1] + "\t" + line[2] + "rs")
                        costadd += int(line[2]) + 50
                        print(" " + "----------------------------")
                    except:
                        pass
                print("\t GSt: \t\t 50rs")
                print("---------------------------")
                print("\tTotal Bill:", costadd)
        except:
            print("file does not exists")
        

    def Buycake(self):
        Allist = []
        try:
            add = 0
            with open("cart.txt", "r") as fp:
                for i in fp:    
                    i = i.replace(',',' ')
                    #print(i)
                    i = i.split()
                    #multi = (int(i[-1]) * int(i[-2]))
                    add += int(i[-2])
                    #print(add)
                    i += "\n"
                    i = ",".join(i)
                    Allist.append(i)
                #print(Allist)
                with open("cart.txt", "w") as fpp:
                    for j in Allist:
                        fpp.write(j)

                with open("cart.txt","r") as data:
                    costadd = 0
                    print("*******************************")
                    print('''           Cart            ''')
                    print("*******************************")
                    for line in data:
                        try:
                            line = line.split(",")
                            print("\t" + "id:" + line[0] + "\t\t" + "ot:" + line[3])
                            print("\t" + line[1] + "\t" + line[2] + "rs")
                            print(" " + "---------------------------")
                        except:
                            pass
                    print("\t GSt: \t\t 50rs")
                    print("---------------------------------")
                    costadd = add + 50
                    print("\tTotal Bill:", costadd)
        except:
            print("file does not exists")
        open("cart.txt", "w").close()
    
    def Removecart(self, id):
        Allcart = []
        Allcdata = []
        try:
            with open("cdata.txt", "r") as fpp:
                for main in fpp:
                    try:
                        main.index(str(id), 0, 4)

                        #remove cart item
                        main = main.split(",")   
                        with open("cart.txt", "r") as fp:
                            for data in fp:
                                try:
                                    data.index(str(id), 0, 10)
                                    data = data.split(",")
                                    #print(data[-1])
                                    data[3] += "\n"

                                    #restore quantity
                                    add = int(main[3]) + int(data[-1])
                                    #print(add)
                                except:
                                    Allcart.append(data)
                        #update cart after removing cart item
                        Allcart = ",".join(Allcart)
                        #print(Allcart) 
                        with open("cart.txt", "w") as fpp:
                            for new in Allcart:
                                fpp.write(new)
                            print("----------------------------------------")
                            print("\tremove cart item sucessfully")
                            print("----------------------------------------")
                    except:
                        Allcdata.append(main)         
                    else:
                        #update remove item quantity in cdata
                        main[3] = str(add)
                        main[3] += "\n"
                        #print(main[3])
                        #print(main)
                        main = ",".join(main)
                        #print(main)
                        Allcdata.extend(main)

            #updata cake quantity back in cdata
            with open("cdata.txt", "w") as update:
                for pdata in Allcdata:
                    update.write(pdata)            
        except:
            print("file does not exists")

    def Exit(self):
        pass 
