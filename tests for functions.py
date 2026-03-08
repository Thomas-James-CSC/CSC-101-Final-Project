import unittest
import dict_func
import one_value
import classes
from classes import Driver
from classes import Time

drivers_1 = [classes.Driver('Daughter', 17, classes.Time(1, 0), 1, 2),
             classes.Driver('Father', 45, classes.Time(1, 15), 2, 1),
             classes.Driver('Mother', 47, classes.Time(1, 15), 2, 0)]

vehicles_1 = [classes.Vehicle('Tesla', 'Electric', 0.0, 30, 200),
              classes.Vehicle('Truck', 'Gas', 20.0, 15, 110),
              classes.Vehicle('Minivan', 'Gas', 28.0, 35, 105)]


#Thomas James wrote these test functions:
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
        actual = dict_func.gas_dictionary([], 0, 0)
        self.assertEqual(actual, expected)

    def test_gas_dictionary2(self):
        expected = {'Tesla': ('Cost of gas per month in dollars', 0.0, 'Great job you are under budget for this vehicle! Amount under monthly budget in dollars', 46.666666666666664), 'Truck': ('Cost of gas per month in dollars', 90.0, 'Amount over monthly budget in dollars', 43.333333333333336), 'Minivan': ('Cost of gas per month in dollars', 150.0, 'Amount over monthly budget in dollars', 103.33333333333334)}
        actual = dict_func.gas_dictionary(vehicles_1, 4.0, 140.0)
        self.assertEqual(actual, expected)

    def test_safety_rating1(self):
        expected = -18
        actual = one_value.safety_rating(Driver('Matt', 12, Time(2, 0), 2, 3))
        self.assertEqual(actual, expected)

    def test_safety_rating2(self):
        expected = 0
        actual = one_value.safety_rating(Driver('Matt', 20, Time(2, 0), 2, 2))
        self.assertEqual(actual, expected)

    def test_time_week_drivers(self):
        expected = Time(3,30)
        actual = one_value.time_week_drivers(drivers_1)
        self.assertEqual(actual, expected)

    def test_time_week_drivers2(self):
        expected = Time(0,0)
        actual = one_value.time_week_drivers([])
        self.assertEqual(actual, expected)

#Connor Nowak wrote these test functions:

    def test_compare_average1(self):
        expected = None
        actual = one_value.compare_average(drivers_1)
        self.assertEqual(actual, expected)

    def test_compare_average2(self):
        expected = None
        actual = one_value.compare_average([])
        self.assertEqual(actual, expected)

    def test_driver_to_car(self):
        expected = None
        actual = one_value.driver_to_car(drivers_1, vehicles_1)
        self.assertEqual(actual, expected)

    def test_driver_to_car2(self):
        expected = None
        actual = one_value.driver_to_car([], [])
        self.assertEqual(actual, expected)

    def test_rush_hour_suggestions(self):
        expected = None
        actual = one_value.rush_hour_suggestions(drivers_1)
        self.assertEqual(actual, expected)

    def test_rush_hour_suggestions2(self):
        expected = None
        actual = one_value.rush_hour_suggestions([])
        self.assertEqual(actual, expected)

    def test_gas_cost1(self):
        expected = 240.0
        actual = one_value.gas_cost(vehicles_1, 4.0)
        self.assertEqual(actual, expected)

    def test_gas_cost2(self):
        expected = 0.0
        actual = one_value.gas_cost([], 4.0)
        self.assertEqual(actual, expected)

    def test_gas_budget1(self):
        expected = False
        actual = one_value.gas_budget(vehicles_1, 140.0, 4.0)
        self.assertEqual(actual, expected)

    def test_gas_budget2(self):
        expected = True
        actual = one_value.gas_budget([], 140.0, 4.0)
        self.assertEqual(actual, expected)

    def test_exceed_average1(self):
        expected = None
        actual = one_value.exceed_average(vehicles_1, 140.0, 4.0)
        self.assertEqual(actual, expected)

    def test_exceed_average2(self):
        expected = None
        actual = one_value.exceed_average([], 140.0, 4.0)
        self.assertEqual(actual, expected)




