# pico-placa

Software that verify if a car can be or not in the street acording to the rules of Pico & Placa in Quito.
The rules are the following:
If the last digit of the plate of a car correspond to the day listed in the table bellow,
  Day     Last Digit Plate
  Monday        1, 2
  Tuesday       3, 4
  Wednesday     5, 6
  Thursday      7, 8
  Friday        9, 0
between these intervals of time (7:00 - 9:30) and (16:00 - 19:30), then the car cannot be on the road.
Otherwise it is free to be on the road. 

### Prerequisites

You will need to install pytest in order to run the tests 

```
pip install -U pytest
```
Also, you will need python 3.7.4 to run the program.

### Sample Generator

The software has a sample generator that create a file with random data of plates and dates in a given interval, 
you can run the script in this way

```
python random_data.py
```

if you wan to modify the date range you can modify the line 29 of random_data.py

```
line = str(plate)+" "+random_date("2000-1-1 00:00", "2020-02-17 23:59", random.random())
```

### Run

To run the script given a sample you only need to run 

```
python pico_placa.py
```
you can change the sample file name in the line 9 of pico_placa.py 


```
    data_treatment("sample.dat")
```

or you can uncomment line 7 and 8 of pico_placa.py and enter by console the name of the sample

```
    #file_n = eval(input("Please enter the name of the file: "))
    #data_treatment(file_n)
```

### Tests

To run the test you will need to run the following code in the folder of the program

```
pytest -q test.py
```
### Authors

* **Anthony Ramos**
