""" Module baseCar
 Module that contain the class car and it corresponding
 methods"""

#Global Variables [Week Days]
week_days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

class Car():
    """ Class Car with the following parameters:
        plate (Int)
        date (date)
        time (time)
        availability (bool)
        Functions:
        __str__
        print_ava [transform bool to string]"""


    def __init__(self, *parameters):
        """ Constructor of class car
            parameters[0].- Plate number (Int)
            parameters[1].- date with time (date)
            availability will be assing later (Bool)"""
        self.plate = parameters[0]
        self.date = parameters[1]
        self.availability = -1 
        # Before the assignment of the real value it will be
        # assign the value of -1 as default

    def print_ava(self):
        """ Function that said in words if a car is
            or not available."""
        if self.availability == -1:
            return "The Values has not been assigned yet"
        elif self.availability:
            return "This Car can drive around"
        else:
            return "This Car cannot drive around"

    def print_weekday(self):
        idx = self.date.weekday()
        return week_days[idx]

    def __str__(self):
        separator = "-----------------------------------------------------------------"
        return "Car plate: {} \n Date: {} \t Week day: {}  \n {} \n {} \n".format(self.plate, self.date, self.print_weekday(), self.print_ava(), separator)
