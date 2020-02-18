# File with tests 

from car_module import *
from processing import *

class TestClass:
    def test_one(self):
        data_line = "0987 2020-01-02 7:01"
        par = line_treatment(data_line)
        car = Car(par[0], par[1])
        check_availability(car)
        assert car.availability == False

    def test_two(self):
        data_line = "0988 2020-01-02 7:30"
        par = line_treatment(data_line)
        car = Car(par[0], par[1])
        check_availability(car)
        assert car.availability == False

    def test_three(self):
        data_line = "0981 2020-01-02 7:30"
        par = line_treatment(data_line)
        car = Car(par[0], par[1])
        check_availability(car)
        assert car.availability == True

    def test_four(self):
        data_line = "0987 2020-01-02 9:31"
        par = line_treatment(data_line)
        car = Car(par[0], par[1])
        check_availability(car)
        assert car.availability == True

    def test_five(self):
        data_line = "0980 2020-02-07 16:01"
        par = line_treatment(data_line)
        car = Car(par[0], par[1])
        check_availability(car)
        assert car.availability == False

    def test_six(self):
        data_line = "0980 2020-02-07 19:31"
        par = line_treatment(data_line)
        car = Car(par[0], par[1])
        check_availability(car)
        assert car.availability == True

    def test_seven(self):
        data_line = "0980 2020-02-07 16:30"
        par = line_treatment(data_line)
        car = Car(par[0], par[1])
        check_availability(car)
        assert car.availability == False

    def test_eight(self):
        data_line = "0989 2020-02-07 15:59"
        par = line_treatment(data_line)
        car = Car(par[0], par[1])
        check_availability(car)
        assert car.availability == True