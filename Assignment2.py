__author__ = 'Barry'
import random
import string
import winsound

""" OOP -Assignement2
    Autor = Barry Burke
    Student No = C13427078
    Date Started = 26/2/15
    Name of Assignment = Elevator Simulator
     """
##############################################################################################
#       PLEASE ENSURE THAT FILE "Elevator Music.wav" is in the same directory as this file.  #
##############################################################################################

#todo play elevator music when lift opens
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
        #create an elevator
            AElevator = Elevator(self.floors,self.customers_waiting,self.customers_served)
    # def __repr__(self):
    #     #this will print out building with elevator..
    #     pass


class Customer:
    def __init__(self,floor):

        while self.Source == self.destination:
            self.Source = random.randint(0,floor)
            self.destination =random.randint(0,floor)


class Elevator:
    def __init__(self,floors):
        self.location =0
        self.customers_inside_elevators=[]

    def Elevatormainloop(self):
        #check to see are their people in the list

        if len(self.customers_inside_elevators) == 0:
            pass
            #move on to see are the customers waiting to get on at this floor.
        if len(self.customers_inside_elevators) > 0:
            #call fxn to search through the list and see does anybody want to get out at this floor.
            pass

    def checkElevator(self):
        for customer in self.customers_inside_elevators:
            if customer.destination == self.location:
                #move customer in customers served.
                self.customers_served



def main():
    print("Out of order, Travel at ones own risk")

    #main will be used to pass vars to classes
    No_of_floors =int(input("How many floors are in the building"))
    No_of_Customers =int(input("How many Customers are in the building"))

    #this code plays elevator music in the background of the project
    winsound.PlaySound("Elevator Music.wav",winsound.SND_ASYNC)
    x=Building(No_of_floors,No_of_Customers)





if __name__ =="__main__":
    main()
