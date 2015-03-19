__author__ = 'Barry'
import random # Random locations start
import string
import winsound # used to play Elevator music
import time  # use for sleep command
import platform # so music only plays on windows
""" OOP -Assignement2
    Autor = Barry Burke
    Student No = C13427078
    Date Started = 26/2/15
    Date Finished =19/3/15
    Name of Assignment = Elevator Simulator

    This Elevator Simulator features Elevator Music , however this will only work on a windows PC.
     """
#################################################################################################
#     PLEASE ENSURE THAT FILE "Elevator Music.wav" is in the same directory as this file.       #
#################################################################################################

# todo play elevator music when lift opens ☑
# Right so 3 classes
# Building  Elevator  and customer ☑
# todo no:1 make 3 classes called building , a customer and elevator and init☑

# todo if time; have a assign a weight to each person. and set a max weight to the lift. refuse customers...
# todo  if there are too many people in the lift☑

#todo , error check on user ☑

#todo Do doc string documenation on each class ☑
class Building:
    """
    This Class Building Takes in the number of floors and the number of customers.
    It makes 2 list called Customers waiting to use the lift and customers already served.
    The class also makes a all the customers and places them in the waiting list
    The elevator is also created here
    """
    # class recives the amount of floors in the building and the amount of customers
    def __init__(self, floors, no_of_customers):
        """
            Initialise value ,creates lists
        """
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
    """ This is where most of the code for the elevator simulator is. The Elevator starts on level 0 and goes up.
        each floor it checks to see are their customers who want to get off and then check to see if anybody is waiting .
        if there is nobody in the elevator , the program may be ready to end so it check to see if there is people waiting
        in the customer waiting class.
    """
    def __init__(self, floors, customers_waiting, customers_served,Max_mass =500,sleeptime=2):
    # allows a max mass to be sent, but if nothing, set a standard size of 500kg
    # sleep time allows the user to read output ,2 seconds by default , can be increase or decrease if chosen if class is manually called
        """
        inits values and makes a customers inside elevator list
        """
        self.location = 0
        self.sleeptime = sleeptime
        self.direction = "up"
        self.floors = floors
        self.customers_inside_elevators = []
        self.customers_waiting = customers_waiting
        self.customers_served = customers_served
        self.Max_Mass = Max_mass # Set a maximum mass to 500Kg
        self.Mass = 0
        self.efficiency = 0   # after each floor is visited , one is added to a counter

    def __repr__(self):
        """
        calls __str__() so to be able to print to the screen
        """
        self.__str__()

    def Elevatormainloop(self):
        """
        main elevator loop
        """
        # check to see are their people in the list
        self.working = 0

        while self.working == 0:
            time.sleep(self.sleeptime)
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

    def checkElevator(self):
        """
        check to see if there are people in the elevator who want to get out at this floor
        """
        for customer in self.customers_inside_elevators[:]: # for every customer in the lift.  # [:] makes it go through a copy so fixes to-do above
            if customer.destination == self.location:  # ask them do they want to get out.
                # move customer in customers served.
                self.customers_served.append(customer)
                self.customers_inside_elevators.remove(customer)
                self.Mass = self.Mass - customer.Mass

    def checkCustometers(self):
        """
        checks to see who wants to get in on this floor and then goes up or down .
        """

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
            self.efficiency += 1 # add one to counter


        elif self.direction == "up" and self.location == self.floors:  # if we are going up but were on the top floor
            self.direction = "down"  # we decide to go back down
            self.location += -1  # we go down by 1 floor.
            self.efficiency +=1 # add one to counter


        elif self.direction == "down" and self.location > 0:  # if we are going down and we are not on the ground floor
            self.location += -1  # go down
            self.efficiency +=1 # add one to counter


        elif self.direction == "down" and self.location == 0:  # if we are going down , but were on floor 0
            self.direction = "up"  # we go up
            self.location += 1  # we  go up by 1 floor.
            self.efficiency +=1 # add one to counter

    def __str__(self):

        """
        :return:  prints to screen the info of the list
        """
        self.updatetoscreen = """
        The Elevators is on floor {}
        The Elevators Max_Mass is {} Kg
        The Elevators Mass is {} Kg
        There are {} people in the lift
        There are {} people waiting
        There are  {} people already served
        Elevator doors are now opening
        """.format(self.location,self.Max_Mass ,self.Mass,len(self.customers_inside_elevators),len(self.customers_waiting), len(self.customers_served))
        return self.updatetoscreen

    def checkend(self):
        """
        check to see can we end the program and gives final print statment to summarise.
        """
        # this fxn will check to see is the program over. This happens when there is nobody left in the elevator.

        if len(self.customers_waiting) == 0:
            # end program
            self.working = 1  # end elevator main loop
            print("All Customers have been Served. Lift Status:")
            self.end = """
            The Lift is on floor {}
            The Elevators Max_Mass is {} Kg
            The Elevators Mass is {} Kg
            There are {} people in the lift
            There are {} people waiting
            There are  {} people served

            The Elevator Visited {} floors
            """.format(self.location, self.Max_Mass, self.Mass , len(self.customers_inside_elevators),len(self.customers_waiting), len(self.customers_served), self.efficiency)
            print(self.end)

class Customer:
    """customer class - Assigns each customer a random dest floor and start floor . Also sets a mass
        between 50 and 80 Kgs"""
    def __init__(self, floor):
        """
        assigns each value to vars
        """
        self.Source = random.randint(0, floor)
        self.destination = random.randint(0, floor)
        self.Mass = random.randint(50,80)  # selects a random weight for the customer between 50 and 100kg
        while self.Source == self.destination:
            self.Source = random.randint(0, floor)
            self.destination = random.randint(0, floor)


def main():
    """
    asks the user to enter the number of floors and customers wanted for the sim. error checks their answers . Calles
    to put on elevator music which runs in the background and calls to creates a building .
    """
    print("Out of order, Travel at ones own risk")
    breakvalue =1
    while  breakvalue ==1: ## makes sure user enters real numbers and not letters
        # main will be used to pass vars to classes
        try:
            No_of_floors = int(input("How many floors are in the building"))
        except ValueError:
            print("This is not a number. Please Enter another Value")
            continue

        try:
            No_of_Customers = int(input("How many Customers are in the building"))
        except ValueError:
            print("This is not a number. Please Enter another Value")
            continue
        break


    Elevatormusic()  # 1 turns music on

    Building(No_of_floors, No_of_Customers)  # creates a building


# defines a fxn that will turn on or off the music
def Elevatormusic(onoff =1 ):  # pass 1 for turn music on , 0 for off
    """ This method checks to see if you are running windows os If you are it attempts to play elevator music
    so to fully simulate an elevator. This only runs for windows os and if this detects any other os , it simple wont
    play.
    """
    # this code plays elevator music in the background of the project
    #detech os
    if (platform.system()) == "Windows":
        if onoff == 1:
            try:
                winsound.PlaySound("Elevator Music.wav", winsound.SND_ASYNC)  # turns music on
            except ValueError as e:
                print(e)


# if the program is run as one then main is run.
if __name__ == "__main__":
    main()
