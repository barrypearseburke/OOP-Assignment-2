__author__ = 'Barry'
import random # Random locations start
import string
import winsound # used to play Elevator music
import time  # use for sleep command
import pygame

""" OOP -Assignement2
    Autor = Barry Burke
    Student No = C13427078
    Date Started = 26/2/15
    Name of Assignment = Elevator Simulator
     """
#################################################################################################
#     PLEASE ENSURE THAT FILE "Elevator Music.wav" is in the same directory as this file.       #
#################################################################################################

# todo play elevator music when lift opens
# Right so 3 classes
# building  Elevator  and customer
# todo no:1 make 3 classes called building , a customer and elevator and init

# todo if time; have a assign a weight to each person. and set a max weight to the lift. refuse customers...
# todo  if there are too many people in the lift

# todo do 4th class to make lift in pygame

class Building:
    # class recives the amount of floors in the building and the amount of customers
    def __init__(self, floors, no_of_customers):
        self.floors = floors
        self.no_of_customers = no_of_customers
        self.customers_waiting = []
        self.customers_served = []
        for person in range(0, self.no_of_customers):
            aCustomer = Customer(self.floors)
            self.customers_waiting.append(aCustomer)
        # create an elevator
        self.AElevator = Elevator(self.floors, self.customers_waiting, self.customers_served)
        self.AElevator.Elevatormainloop()


class Elevator:
    def __init__(self, floors, customers_waiting, customers_served,Max_mass =500): # allows a max mass to be sent, but if nothing, set a standard size of 500kg
        self.location = 0
        self.direction = "up"
        self.floors = floors
        self.customers_inside_elevators = []
        self.customers_waiting = customers_waiting
        self.customers_served = customers_served
        self.Max_Mass = Max_mass # Set a maximum mass to 500Kg
        self.Mass =0

    def __repr__(self):
        self.__str__()

    def Elevatormainloop(self):
        # check to see are their people in the list
        self.working = 0

        while self.working == 0:
            time.sleep(2)
            print(self)

            if len(self.customers_inside_elevators) == 0:  # There is nobody in the lift
                # pass for now. will go to check customers list
                # move on to see are the customers waiting to get on at this floor.

                # check end
                self.checkend()

                # if nobody in lift , call to check are their people wanting to get in



            elif len(self.customers_inside_elevators) > 0:
                # call fxn to search through the list and see does anybody want to get out at this floor.
                self.checkElevator()
                # once everybody is asked do they want to get out
                # ask does anybody want to get in
            self.checkCustometers()
    # todo ,BUG: when a customer is leaving the lift or entering lift what is happening is they are removed from where they were. if they were item
    # todo, 3 for example , the list then searches element 4 but becuase an entry has been removed. the  orginal number 4 is now item 3
    # todo and the list is now searching new element 4 and orginal numnber 5. so orginal number 4 is not being asked does he want to enter
    def checkElevator(self):

        for customer in self.customers_inside_elevators[:]: # for every customer in the lift.  # [:] makes it go through a copy so fixes to-do above
            if customer.destination == self.location:  # ask them do they want to get out.
                # move customer in customers served.
                self.customers_served.append(customer)
                self.customers_inside_elevators.remove(customer)
                self.Mass = self.Mass - customer.Mass

    def checkCustometers(self):

        for customer in self.customers_waiting[:]:  # [:]make it go through a copy so fixes to-do above
            if self.Mass + customer.Mass > self.Max_Mass:
                continue # If by adding the customer to the it would cause the lift to exceed max mass , skip them
            elif customer.Source == self.location:  # if the customer  wants to get on at this floor,
                self.customers_inside_elevators.append(customer)  # place customer into elevator
                self.customers_waiting.remove(customer)  # The customer isent waiting anymore
                self.Mass = self.Mass +customer.Mass


        # go up or down a floor
        if len(self.customers_waiting) == 0 and len(self.customers_inside_elevators) == 0:
            self.checkend() # if nobody left , end program
        elif self.direction == "up" and self.location < self.floors:  # if we are going up and were not on the top floor
            self.location += 1  # go up

        elif self.direction == "up" and self.location == self.floors:  # if we are going up but were on the top floor
            self.direction = "down"  # we decide to go back down
            self.location += -1  # we go down by 1 floor.

        elif self.direction == "down" and self.location > 0:  # if we are going down and we are not on the ground floor
            self.location += -1  # go down
        elif self.direction == "down" and self.location == 0:  # if we are going down , but were on floor 0
            self.direction = "up"  # we go up
            self.location += 1  # we  go up by 1 floor.
    def __str__(self):

        self.updatetoscreen = """
        The Elevators is on floor {}
        The Elevators Max_Mass is {}
        The Elevators Mass is {}
        There are {} people in the lift
        There are {} people waiting
        There are  {} people already served
        Elevator doors are now opening
        """.format(self.location,self.Max_Mass ,self.Mass,len(self.customers_inside_elevators),len(self.customers_waiting), len(self.customers_served))
        return self.updatetoscreen

    def checkend(self):
        # todo make an end call.
        # this fxn will check to see is the program over. This happens when there is nobody left in the elevator.

        if len(self.customers_waiting) == 0:
            # end program
            self.working = 1  # end elevator main loop
            print("All Customers have been Served. Lift Status:")
            self.end = """
            The Lift is on floor {}
            The Elevators Max_Mass is {}
            The Elevators Mass is {}
            There are {} people in the lift
            There are {} people waiting
            There are  {} people served
            """.format(self.location, self.Max_Mass, self.Mass , len(self.customers_inside_elevators),len(self.customers_waiting), len(self.customers_served))
            print(self.end)

class Customer:
    def __init__(self, floor):
        self.Source = random.randint(0, floor)
        self.destination = random.randint(0, floor)
        self.Mass = random.randint(50,80)  # selects a random weight for the customer between 50 and 100kg
        while self.Source == self.destination:
            self.Source = random.randint(0, floor)
            self.destination = random.randint(0, floor)


def main():
    print("Out of order, Travel at ones own risk")

    # main will be used to pass vars to classes
    No_of_floors = int(input("How many floors are in the building"))
    No_of_Customers = int(input("How many Customers are in the building"))
    Elevatormusic(1)  # 1 turns music on

    Building(No_of_floors, No_of_Customers)  # creates a building


# defines a fxn that will turn on or off the music
def Elevatormusic(onoff):  # pass 1 for turn music on , 0 for off
    # this code plays elevator music in the background of the project
    if onoff == 1:
        try:
            winsound.PlaySound("Elevator Music.wav", winsound.SND_ASYNC)  # turns music on
        except Error as e:
            print(e)

    elif onoff == 0:  # turns off music
        winsound.PlaySound("", winsound.SND_ASYNC)


if __name__ == "__main__":
    main()
