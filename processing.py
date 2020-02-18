""" Module to process the data of Pico y Placa """
from datetime import date, time, datetime
from car_module import *

# Global Variables
aux = datetime.now() # aux value to set time
morning_in = aux.replace(hour=7, minute=0) # 7:00 
morning_end = aux.replace(hour=9, minute=30) # 9:30 
afternoon_in = aux.replace(hour=16, minute=0) # 16:00 
afternoon_end = aux.replace(hour=19, minute=30) # 19:30

def line_treatment(line):
    """ Function that treat the raw data obtained in 
        in a string form """
    aux_list = line.split(" ")  # Separate the line by spaces
    plate_num = aux_list[0]     # Get the number of the plate
    date = datetime.strptime(aux_list[1], "%Y-%m-%d")
    # Transfor the string of the date into date type
    aux_time = aux_list[2].split(":")
    # Separate the hours and minutes
    aux_hour = int(aux_time[0]) # Assing the hours 
    aux_min = int(aux_time[1]) # assing the minutes 
    date = date.replace(minute=aux_min, hour=aux_hour) 
    # Encode the hour and minutes in a datetime class
    
    return [plate_num, date]

def check_availability(car):
    """ Function that take a car class and 
        modify the availability of the car 
        according to the pico y placa rules"""
    plate_num = int(car.plate[-1]) # Get the last number of the plate
    date = car.date # Get the date  
    weekday = (date.weekday() + 1)*2 # Get the number of the week day
    time = date.time() # Get the time 
    restricted = [(weekday-1) , weekday % 10] # Create an interval of restrictions
    check_time = (time <= morning_end.time() and time >= morning_in.time()) or \
                (time <= afternoon_end.time() and time >= afternoon_in.time())
    # Boolean that verify the time 
    if  check_time and plate_num in restricted:
        car.availability = False
    else:
        car.availability = True

def data_treatment(file_name):
    """ Function to treat a file with car information and date
        -- plate number date(Y-m-d) time(h:m) --
        it return a list of cars and print a file with the 
        information of the cars that are allowed to be on the road """
    input_f = open(file_name, "r") # Read the file
    out_f = open(file_name[:-4]+".out","w") # Create the output file
    cars = [] # Create a list where the car class will be stored
    for line in input_f:
        param = line_treatment(line) # Read the parameters per line
        car = Car(param[0], param[1]) # Create a class Car with the parameters
        check_availability(car) 
        cars.append(car) # Append the car to the list of cars
        print (car, file=out_f) # Print in the output file
    input_f.close() # Close input file
    out_f.close() # Close output file
    return cars

