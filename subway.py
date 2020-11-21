class subway:
    bread=str()
    veggies=str()
    meat=str()
    sauces=str()
    def __init__(self,bread="", veggies ="",meat = "",sauces = ""):
        self.bread = bread
        self.veggies = veggies
        self.meat = meat
        self.sauces = sauces

    def print_subway_items(self):
        print("Your Sub:")
        print("\tBread: ",self.bread)
        print("\tVeggies: ",self.veggies)
        print("\tMeat: ",self.meat)
        print("\tSauces: ",self.sauces)

# ------------------FUNCTIONS----------------------------
def your_input(x):
    n = input("Add Your Ingredient: ")
    x.append(n)

def remove_from_list(i):
    n = int(input("Enter the Index Value of the Ingredient:\n"))-1
    i.pop(n)
    

def print_items(x):
    print(x)

def print_whole_menu(a,b,c,d):
    print("")
    print("Bread: ", a)
    print("")
    print("Veggies: ",b)
    print("")
    print("Meat: ", c)
    print("")
    print("Sauces: ",d)
    print("")

def making_order(my_order,a,b,c,d):
    print("Make Your Sub!!!")
    print("ENTER THE INDEX VALUE:")
    
    print_items(a)
    bread_int=int(input("\tBread:"))-1
    bread=a[bread_int]
    
    print_items(b)    
    veggies_int=int(input("\tVeggies:"))-1
    veggies=b[veggies_int]
    
    print_items(c)
    meat_int=int(input("\tMeat:"))-1
    meat=c[meat_int]
    
    print_items(d)
    sauces_int=int(input("\tSauce:"))-1
    sauces=d[sauces_int]

    Subway=subway(bread,veggies,meat,sauces)
    my_order.append(Subway)
    return my_order

def print_order(my_order):
    i=1
    name=input("Enter Your Name: ")
    if len(my_order) > 0:
        for subway in my_order:
            print(name , str(i) , " : ")
            subway.print_subway_items()
            i+=1
    else:
        print("No Sub There!")

#---------------------MAIN--------------------------------
list_bread=["Multigrain","Oats","Regular"]
list_veggies=["Lettus","Onion","Tomato"]
list_meat=["Hot & Sweet Chicken","Beef","Grilled Chicken"]
list_sauces=["Hot Sauce","Mayo","Honey Mustard"]
ingredient=None
my_order=[]
while True:
    n=0
    print("")
    print("~~~ Welcome To Subway ~~~")
    n= int(input("1. Customer\n2. Staff\n3.Exit\n"))
    if n==1:
#-----------------------CUSTOMER-----------------------------------------     
        while True:
            a=0
            print("Customer Menu")
            a=int(input("\t1. View Full Menu\n\t2. Make an Order\n\t3. Back to Main Menu"))
            if a==1:
                print_whole_menu(list_bread,list_veggies,list_meat,list_sauces)
            elif a==2:
                my_order= making_order(my_order,list_bread,list_veggies,list_meat,list_sauces)
                print("")
                print_order(my_order)
            elif a==3:
                break
            else:
                print("You have entered the Wrong Value!!!")

    elif n==2:
#----------------------------STAFF----------------------------------------        
        while True:
            x=0
            print("Staff Menu:")
            x= int(input("\t1. Add Ingredient\n\t2. Remove Ingredient\n\t3. Back To Main Menu\n"))
            if x==1:
#-------------------ADD ITEMS-----------------------------------                
                while True:
                    z=0
                    print("Add Item From:")
                    z=int(input("\t1. Bread\n\t2. Veggies\n\t3. Meat\n\t4. Sauces\n\t5. Back To Staff Menu\n"))
                    if z==1:
                        your_input(list_bread)
                    elif z==2:
                        your_input(list_veggies)
                    elif z==3:
                        your_input(list_meat)
                    elif z==4:
                        your_input(list_sauces)
                    elif z==5:
                        break
                    else:
                        print("You have entered the Wrong Value!!!")
                    print("")
                    print("Your Ingredient is Added!!!")    
            elif x==2:
#------------------DELETE ITEMS----------------------------------                
                while True:
                    z=0
                    print("Delete Item From:")
                    z=int(input("\t1. Bread\n\t2. Veggies\n\t3. Meat\n\t4. Sauces\n\t5. Back To Staff Menu"))
                    if z==1:
                        print_items(list_bread)
                        print("")
                        remove_from_list(list_bread)
                    elif z==2:
                        print_items(list_veggies)
                        print("")
                        remove_from_list(list_veggies)    
                    elif z==3:
                        print_items(list_meat)
                        print("")
                        remove_from_list(list_meat)
                    elif z==4:
                        print_items(list_sauces)
                        print("")
                        remove_from_list(list_sauces)
                    elif z==5:
                        break
                    else:
                        print("You have entered the Wrong Value!!!")
                    print("Your Ingredient is Removed!!!")
            elif x==3:
                break
            else:
                print("You have entered the Wrong Value!!!")              
    elif n==3:
        break
    else:
        print("You have entered the Wrong Value!!!")
    print("Thank You!, Have a Nice Day :)")


        
        