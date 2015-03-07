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
    def __init__(self,floors):
        self.floors =floors

    def __repr__(self):
        #this will print out building with elevator
        pass


class Customer:
    def __init__(self,floor):
        #todo set customer source and destination
        Source = random.randint(0,floor)
        destination =random.randint(0,floor)


class Elevator:
    def __init__(self):
        self.location =0



def main():
    print("Out of order, Travel at ones own risk")
    #main will be used to pass vars to classes
    No_of_floors =int(input("How many floors are in the building"))
    No_of_Customers =int(input("How many Customers are in the building"))

    #todo make a for loop to makes a load of inistinats of the customers.
    Cust =[]
    for items in No_of_Customers:
        ACustomer = Customer(No_of_floors)
        cust.append(ACustomer)


if __name__ =="__main__":
    main()
