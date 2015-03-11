__author__ = 'Barry'
import random
import string

""" OOP -Assignement2
    Autor = Barry Burke
    Student No = C13427078
    Date Started = 26/2/15
    Name of Assignment = Elevator Simulator

 """
#Right so 3 classes
#building  Elevator  and customer
#todo no:1 make 3 classes called building , a customer and elevator and init

class Building:
    def __init__(self,floors,no_of_customers):
        self.floors = floors
        self.no_of_customers = no_of_customers
        self.customers_waiting=[]
        self.customers_served=[]
        for person in range(0,self.no_of_customers):
            aCustomer =Customer(self.floors)
            self.customers_waiting.append(aCustomer)

    # def __repr__(self):
    #     #this will print out building with elevator
    #     pass


class Customer:
    def __init__(self,floor):
        #todo set customer source and destination
        #todo errorcheck so source !=source
        self.Source = random.randint(0,floor)
        self.destination =random.randint(0,floor)
        #this checks to see if source == destination.
        ##  if is, places customer the floor up, unless the next floor is a higher number than there are floors
        #then places a floor below source.
        if self.Source == self.destination:
            self.destination +=1
        if self.destination > floor:
            self.destination -=2

        #todo , better error check as this wont work for small buildings
class Elevator:
    def __init__(self):
        self.location =0
        self.customers_inside_elevators=[]



def main():
    print("Out of order, Travel at ones own risk")
    #main will be used to pass vars to classes
    No_of_floors =int(input("How many floors are in the building"))
    No_of_Customers =int(input("How many Customers are in the building"))

    x=Building(No_of_floors,No_of_Customers)





if __name__ =="__main__":
    main()
