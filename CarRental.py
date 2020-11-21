class cars:    
    def __init__(self,car_name="",number_plate = "",cost = ""):
        self.car_name=car_name
        self.number_plate = number_plate 
        self.cost = cost

    def print_cars(self):
        print("Name:" + self.car_name,"No. Plate:" + self.number_plate, "Cost:" + self.cost)

def create_car(car_list):
    print("Enter Car Details :- ")
    car_name = input("\tCar Name : ")
    number_plate = input("\tNumber Plate : ")
    cost = input("\tCost : ")
    car_obj = cars(car_name,number_plate,cost)
    car_list.append(car_obj)
    return car_list

def printCar(car_list):
    i=0
    if len(car_list) > 0:
        for car_o9bj in car_list:
            print("Car " , str(i) , " : ")
            cars.print_cars()
            i+=1        

# --------------------MAIN------------------------------
car_list = list()
while True:
    x="0"
    print("-----Welcome-----")
    x =input("1. Add Car\n2. View The List")
    if x =="1":
        car_list = create_car(car_list)
    elif x=="2":
        printCar(car_list)
    else:
        print("---END---")