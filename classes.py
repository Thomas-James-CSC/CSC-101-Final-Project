#Thomas James created the classes
class Time:
    def __init__(self, hours:int, minutes:int):
        self.hours = hours
        self.minutes = minutes

    def __repr__(self):
        return "Hours: {}, Minutes: {}".format(self.hours,self.minutes)

    def __eq__(self, other):
        return ((self is other) or
        (type(self) is type(other)) and
        self.hours == other.hours and
        self.minutes == other.minutes)



class Vehicle:
    def __init__(self, name_of_car:str, powertrain:str, mpg:float, miles_used_per_day:int, top_speed:float):
        self.name_of_car = name_of_car
        self.powertrain = powertrain
        self.mpg = mpg
        self.miles_used_per_day = miles_used_per_day
        self.top_speed = top_speed

    def __repr__(self):
        return "Name of Car: {}, Powertrain: {}, Miles Per Gallon: {}, Miles Driven Per Day: {}, Top Speed: {}".format(self.name_of_car,self.powertrain,self.mpg,self.miles_used_per_day,self.top_speed)

    def __eq__(self, other):
        return ((self is other) or
        (type(self) is type(other)) and
        self.name_of_car == other.name_of_car and
        self.powertrain == other.powertrain and
        self.mpg == other.mpg and
        self.miles_used_per_day == other.miles_used_per_day and
        self.top_speed == other.top_speed)


class Driver:
    def __init__(self, name_of_driver:str, driver_age:int, time_driving_per_day:Time, stuck_in_traffic_count:int, accident_count:int):
        self.name_of_driver = name_of_driver
        self.driver_age = driver_age
        self.time_driving_per_day = time_driving_per_day
        self.stuck_in_traffic_count = stuck_in_traffic_count
        self.accident_count = accident_count

    def __repr__(self):
        return "Name: {}, Age: {}, Time driving per day: {}, Traffic encounters: {}, Accident Count: {}".format(self.name_of_driver,self.driver_age, self.time_driving_per_day,self.stuck_in_traffic_count,self.accident_count)

    def __eq__(self, other):
        return ((self is other) or
        (type(self) is type(other)) and
        self.name_of_driver == other.name_of_driver and
        self.driver_age == other.driver_age and
        self.time_driving_per_day == other.time_driving_per_day and
        self.stuck_in_traffic_count == other.stuck_in_traffic_count and
        self.accident_count == other.accident_count)

#Data Entry Example:
#Family 1:
vehicles_1 = [Vehicle('Tesla', 'Electric', 0.0, 30, 200 ),
              Vehicle('Truck', 'Gas', 20.0, 15, 110),
              Vehicle('Minivan', 'Gas', 28.0, 35, 105)]

drivers_1 = [Driver('Daughter', 17, Time(1,0), 1, 2),
             Driver('Father', 45, Time(1,15), 2, 1),
             Driver('Mother', 47, Time(1,15), 2, 0)]

monthly_gas_budget = 140.0

estimated_cost_per_gallon = 4.0




