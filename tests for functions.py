import unittest
import dict_func
import one_value
import classes
from classes import Driver
from classes import Vehicle
from classes import Time

drivers_1 = [classes.Driver('Daughter', 17, classes.Time(1,0), 1, 2),
             classes.Driver('Father', 45, classes.Time(1,15), 2, 1),
             classes.Driver('Mother', 47, classes.Time(1,15), 2, 0)]

vehicles_1 = [classes.Vehicle('Tesla', 'Electric', 0.0, 30, 200 ),
              classes.Vehicle('Truck', 'Gas', 20.0, 15, 110),
              classes.Vehicle('Minivan', 'Gas', 28.0, 35, 105)]



class TestCase(unittest.TestCase):
    def test_dictionary_drive_time_persons1(self):
        expected = {('Daughter', '(Daily drive time)'): 'Hours: 1, Minutes: 0', ('Father', '(Daily drive time)'): 'Hours: 1, Minutes: 15', ('Mother', '(Daily drive time)'): 'Hours: 1, Minutes: 15'}
        actual = dict_func.dictionary_drive_time_persons(drivers_1)
        self.assertEqual(actual, expected)

    def test_dictionary_drive_time_persons2(self):
        expected = {}
        actual = dict_func.dictionary_drive_time_persons([])
        self.assertEqual(actual, expected)

    def test_dictionary_drive_miles_vehicles1(self):
        expected = {}
        actual = dict_func.dictionary_drive_miles_vehicles([])
        self.assertEqual(actual, expected)

    def test_dictionary_drive_miles_vehicles2(self):
        expected = {('Tesla', '(daily miles)'): 30, ('Truck', '(daily miles)'): 15, ('Minivan', '(daily miles)'): 35}
        actual = dict_func.dictionary_drive_miles_vehicles(vehicles_1)
        self.assertEqual(actual, expected)

    def test_dictionary_mpg1(self):
        expected = {}
        actual = dict_func.dictionary_mpg([])
        self.assertEqual(actual, expected)

    def test_dictionary_mpg2(self):
        expected = {('Tesla', '(miles per gallon)'): '0.0', ('Truck', '(miles per gallon)'): '20.0', ('Minivan', '(miles per gallon)'): '28.0'}
        actual = dict_func.dictionary_mpg(vehicles_1)
        self.assertEqual(actual, expected)

    def test_gas_dictionary1(self):
        expected = {}
        actual = dict_func.gas_dictionary([], 0,0)
        self.assertEqual(actual, expected)

    def test_gas_dictionary2(self):
        expected = {'Tesla': ('Cost of gas per month in dollars', 0.0, 'Great job you are under budget for this vehicle! Amount under monthly budget in dollars', 140.0), 'Truck': ('Cost of gas per month in dollars', 90.0, 'Great job you are under budget for this vehicle! Amount under monthly budget in dollars', 50.0), 'Minivan': ('Cost of gas per month in dollars', 150.0, 'Amount over monthly budget in dollars', 10.0)}
        actual = dict_func.gas_dictionary(vehicles_1, 4.0,140.0)
        self.assertEqual(actual, expected)

    def test_safety_rating1(self):
        expected = -18
        actual = one_value.safety_rating(Driver('Matt',12, Time(2,0), 2,3))
        self.assertEqual(actual, expected)

    def test_safety_rating2(self):
        expected = 0
        actual = one_value.safety_rating(Driver('Matt',20, Time(2,0), 2,2))
        self.assertEqual(actual, expected)






