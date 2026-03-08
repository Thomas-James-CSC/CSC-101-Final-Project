import classes

#dictionary_drive_time_persons/vehicles: Functions to print the dictionary that shows the time spent driving for each person and miles driven for each vehicle. Thomas James.

def dictionary_drive_time_persons(lst1:list[classes.Driver])->dict|None:
    if lst1 is None:
        return None
    dict1 = {}
    for i in range(len(lst1)):
        dict1[lst1[i].name_of_driver, "(Daily drive time)"] = repr(lst1[i].time_driving_per_day)
    return dict1

drivers_1 = [classes.Driver('Daughter', 17, classes.Time(1,0), 1, 2),
             classes.Driver('Father', 45, classes.Time(1,15), 2, 1),
             classes.Driver('Mother', 47, classes.Time(1,15), 2, 0)]

print(dictionary_drive_time_persons(drivers_1))

def dictionary_drive_miles_vehicles(lst2:list[classes.Vehicle])->dict|None:
    if lst2 is None:
        return None
    dict2 = {}
    for i in range(len(lst2)):
        dict2[lst2[i].name_of_car, "(daily miles)"] = (lst2[i].miles_used_per_day)
    return dict2

vehicles_1 = [classes.Vehicle('Tesla', 'Electric', 0.0, 30, 200 ),
              classes.Vehicle('Truck', 'Gas', 20.0, 15, 110),
              classes.Vehicle('Minivan', 'Gas', 28.0, 35, 105)]
cost_of_gas = 4.0

monthly_gas_budget = 140.0

print(dictionary_drive_miles_vehicles(vehicles_1))

#dictionary_mpg: Prints the dictionary for the miles per gallon that each car has. Thomas James.

def dictionary_mpg(lst2:list[classes.Vehicle])->dict|None:
    if lst2 is None:
        return None
    dict2 = {}
    for i in range(len(lst2)):
        dict2[lst2[i].name_of_car,"(miles per gallon)"] = repr(lst2[i].mpg)
    return dict2

print(dictionary_mpg(vehicles_1))
print("")

#gas_dictionary: Prints the dictionary for total gas that money that each car is using and the amount each car goes over on gas budget. Thomas James.
def gas_dictionary(lst2:list[classes.Vehicle], cost_of_gas:float, budget:float)->dict:
    if lst2 is None:
        return {}
    new_dict = {}
    for vehicle in lst2:
        try:
            gas_cost = (vehicle.miles_used_per_day/vehicle.mpg)*cost_of_gas
        except ZeroDivisionError:
            gas_cost = 0.0
        gas_per_month = gas_cost*30
        amount_over = gas_per_month-(monthly_gas_budget/len(lst2))
        if amount_over >= 0:
            new_dict[vehicle.name_of_car] = ("Cost of gas per month in dollars", gas_per_month, "Amount over monthly budget in dollars", amount_over)
        if amount_over < 0:
            amount_under = abs(amount_over)
            new_dict[vehicle.name_of_car] = ("Cost of gas per month in dollars",gas_per_month, "Great job you are under budget for this vehicle! Amount under monthly budget in dollars", amount_under)
    return new_dict

print(gas_dictionary(vehicles_1, cost_of_gas, monthly_gas_budget))











