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


class Customer:
    def __init__(self,customers):
        # self.customers=customers
        # self.cust_waiting =customers
        # self.cust_served =0


class Elevator:
    def __init__(self):
        self.location =0



def main():
    #main will be used to pass vars to classes
    No_of floors =int(input("How many floors are in the building"))
    No_of_Customers =int(input("How many Customers are in the building"))


if __name__ =="__main__"
    main()
