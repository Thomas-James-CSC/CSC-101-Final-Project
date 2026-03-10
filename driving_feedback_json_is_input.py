#Thomas James created the json file input option.
import classes
from classes import Driver, Vehicle, Time
import json
import argparse
from pathlib import Path

def load_data(path: Path):
    with path.open("r", encoding="utf-8") as f:
        configurations = json.load(f)

    drivers = []
    for d in configurations.get("drivers_1", []):
        t = d["time_driving_per_day"]
        time_obj = Time(int(t["hours"]), int(t["minutes"]))
        drivers.append(
            Driver(
                d["name_of_driver"],
                int(d["driver_age"]),
                time_obj,
                int(d["stuck_in_traffic_count"]),
                int(d["accident_count"]),
            )
        )

    vehicles = []
    for v in configurations.get("vehicles_1", []):
        vehicles.append(
            Vehicle(
                v["name_of_car"],
                v["powertrain"],
                float(v["mpg"]),
                int(v["miles_used_per_day"]),
                float(v["top_speed"]),
            )
        )

    return drivers, vehicles


def run_program(drivers_1, vehicles_1):
#Input loop for cost of gas and monthly gas budget
    while True:
        try:
            cost_of_gas = float(input("Please enter the estimated cost of gas per gallon in your area: "))
            monthly_gas_budget = float(input("Please enter your estimated monthly gas budget: "))
        except ValueError:
            print("Please enter a numeric value")
            continue
        else:
            break

  #Json file is the input for these functions
    def safety_rating(driver) -> int:
        return driver.driver_age - driver.accident_count * 10

    # Connor Nowak created this function to calculate the total time that the family drives.
    def time_week_drivers(list1: list[Driver]) -> Time:
        total_time_minutes = 0
        for driver in list1:
            total_time_minutes += driver.time_driving_per_day.hours * 60 + driver.time_driving_per_day.minutes
        return Time(total_time_minutes // 60, total_time_minutes % 60)

    print("Total weekly drive time is -", time_week_drivers(drivers_1))

    # Thomas James created this function to check if the family is under or over the national average drive time of 60.7 minutes per day.
    def compare_average(list1: list[Driver]) -> None:
        your_time = time_week_drivers(list1)
        your_minutes = your_time.hours * 60 + your_time.minutes
        try:
            if your_minutes / len(list1) > 60.7:
                print(
                    "You are above the national average driving time by:",
                    int((your_minutes / len(list1) - 60.7) // 1),
                    "minutes.",
                )
                print("")
            else:
                print(
                    "You are below the national average driving time by:",
                    abs(your_minutes / len(list1) - 60.7) // 1,
                    "minutes. Great job!",
                )
                print("")
        except ZeroDivisionError:
            print("")

    compare_average(drivers_1)

    # Thomas James created this function to return the daily drive times of people in a dictionary.
    def dictionary_drive_time_persons(lst1: list[Driver]) -> dict | None:
        if lst1 is None:
            return None
        dict1 = {}
        for i in range(len(lst1)):
            dict1[(lst1[i].name_of_driver, "(Daily drive time)")] = repr(lst1[i].time_driving_per_day)
        return dict1

    print(dictionary_drive_time_persons(drivers_1))
    print("")

    # Connor Nowak created this function to give the miles used by the cars in a dictionary.
    def dictionary_drive_miles_vehicles(lst2: list[Vehicle]) -> dict | None:
        if lst2 is None:
            return None
        dict2 = {}
        for i in range(len(lst2)):
            dict2[(lst2[i].name_of_car, "(daily miles)")] = lst2[i].miles_used_per_day
        return dict2

    print(dictionary_drive_miles_vehicles(vehicles_1))
    print("")

    # Connor Nowak
    def gas_cost(list1: list[Vehicle], cost_of_gas: float) -> float:
        monthly_gas_cost = 0
        for car in list1:
            try:
                one_day_gas_cost = (car.miles_used_per_day / car.mpg) * cost_of_gas
            except ZeroDivisionError:
                one_day_gas_cost = 0
            monthly_gas_cost += one_day_gas_cost * 30
        return monthly_gas_cost

    print("Your monthly gas cost is:", gas_cost(vehicles_1, cost_of_gas))

    # Connor Nowak
    def gas_budget(list1: list[Vehicle], monthly_gas_budget: float, cost_of_gas: float) -> bool:
        if list1 == []:
            return True
        for _vehicle in list1:
            if gas_cost(list1, cost_of_gas) > monthly_gas_budget:
                x = abs(gas_cost(list1, cost_of_gas) - monthly_gas_budget)
                print("You are over budget by: $", x)
                return False
            else:
                x = abs(gas_cost(list1, cost_of_gas) - monthly_gas_budget)
                print("You are under budget by: $", x)
                return True

    gas_budget(vehicles_1, monthly_gas_budget, cost_of_gas)

    # Thomas James
    def exceed_average(list1: list[Vehicle], gas_money: float, cost_of_gas: float) -> None:
        for car in list1:
            try:
                if (car.miles_used_per_day / car.mpg * cost_of_gas) * 30 > (gas_money / len(list1)):
                    print(car.name_of_car, "is over budget on gas")
                else:
                    print(car.name_of_car, "is under budget on gas")
            except ZeroDivisionError:
                print(car.name_of_car, "is under budget on gas")

    exceed_average(vehicles_1, monthly_gas_budget, cost_of_gas)
    print("")

    # Connor Nowak created this function to put the MPG in a dictionary.
    def dictionary_mpg(lst2: list[Vehicle]) -> dict | None:
        if lst2 is None:
            return None
        dict2 = {}
        for i in range(len(lst2)):
            dict2[(lst2[i].name_of_car, "(miles per gallon)")] = repr(lst2[i].mpg)
        return dict2

    print(dictionary_mpg(vehicles_1))
    print("")

    # Thomas James created this function to print the dictionary for total gas money that each car is using and the amount each car goes over on gas budget.
    def gas_dictionary(lst2: list[Vehicle], cost_of_gas: float, budget: float) -> dict:
        if lst2 is None:
            return {}
        new_dict = {}
        for vehicle in lst2:
            try:
                one_day_gas_cost = (vehicle.miles_used_per_day / vehicle.mpg) * cost_of_gas
            except ZeroDivisionError:
                one_day_gas_cost = 0.0
            gas_per_month = one_day_gas_cost * 30
            amount_over = gas_per_month - (budget / len(lst2))
            if amount_over >= 0:
                new_dict[vehicle.name_of_car] = (
                    "Cost of gas per month in dollars",
                    gas_per_month,
                    "Amount over monthly budget in dollars",
                    amount_over,
                )
            else:
                amount_under = abs(amount_over)
                new_dict[vehicle.name_of_car] = (
                    "Cost of gas per month in dollars",
                    gas_per_month,
                    "Great job you are under budget for this vehicle! Amount under monthly budget in dollars",
                    amount_under,
                )
        return new_dict

    print(gas_dictionary(vehicles_1, cost_of_gas, monthly_gas_budget))
    print("")

    print("Other suggestions:")

    def driver_to_car(list1: list[Driver], list2: list[Vehicle]) -> None:
        for x in range(len(list1) - 1):
            small_idx = x
            for j in range(x + 1, len(list1)):
                if safety_rating(list1[j]) > safety_rating(list1[small_idx]):
                    small_idx = j
            if small_idx != x:
                temp = list1[x]
                list1[x] = list1[small_idx]
                list1[small_idx] = temp

        vehicle_order = []
        for vehicle in list2:
            x = vehicle.top_speed
            best_vehicle = vehicle
            for i in range(list2.index(vehicle) + 1, len(list2)):
                if list2[i].top_speed >= x:
                    best_vehicle = list2[i]
            vehicle_order.append(best_vehicle)

        if len(list1) == len(list2):
            pairs = [[list1[i].name_of_driver, vehicle_order[i].name_of_car] for i in range(len(list2))]
            print("The best driving pairs based off of driving history are:", pairs)
        else:
            print("Different amount of cars and drivers. Try pairing less experienced drivers with safer cars.")

    driver_to_car(drivers_1, vehicles_1)

    def rush_hour_suggestions(list1: list[Driver]) -> None:
        for driver in list1:
            if driver.stuck_in_traffic_count >= 2:
                print(
                    driver.name_of_driver,
                    "- Try to avoid driving during the hours of 7am-9am and 4pm-6:30pm as much as possible.",
                )

    rush_hour_suggestions(drivers_1)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--data",
        default="data.json",
        help="JSON file with drivers and vehicles (default: data.json next to this script)",
    )
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    data_path = Path(args.data)
    if not data_path.is_absolute():
        data_path = script_dir / data_path

    if not data_path.exists():
        raise FileNotFoundError(f"Couldn't find data file at: {data_path}")

    drivers_1, vehicles_1 = load_data(data_path)
    run_program(drivers_1, vehicles_1)

if __name__ == "__main__":
    main()

while True:
    try:
        cost_of_gas = float(input("Please enter the estimated cost of gas per gallon in your area: "))
        monthly_gas_budget = float(input("Please enter your estimated monthly gas budget: "))
    except ValueError:
        ("Please enter a numeric value")
        continue
    else:
        break

#Supporting function (Still works with them):
def safety_rating(Driver) -> int:
    return Driver.driver_age-Driver.accident_count*10

#Connor Nowak created this function to calculate the total time that the family drives.

def time_week_drivers(list1:list[Driver])->Time:
    total_time_minutes = 0
    for driver in list1:
        total_time_minutes += driver.time_driving_per_day.hours*60 + driver.time_driving_per_day.minutes
    return Time(total_time_minutes//60, total_time_minutes%60)

print("Total weekly drive time is -", time_week_drivers(drivers_1))

#Thomas James created this function to check if the family is under or over the national average drive time of 60.7 minutes per day.
def compare_average(list1:list[Driver]) -> None:
    your_time = time_week_drivers(list1)
    your_minutes = your_time.hours*60+your_time.minutes
    try:
        if your_minutes/len(list1)>60.7:
            print("You are above the national average driving time by:", int((your_minutes/len(list1)-60.7)//1),"minutes.")
            print("")
        else:
            print("You are below the national average driving time by:", abs(your_minutes/len(list1)-60.7)//1,"minutes. Great job!")
            print("")
    except ZeroDivisionError:
        print ("")

compare_average(drivers_1)

#Thomas James created this function to return the daily drive times of people in a dictionary.

def dictionary_drive_time_persons(lst1:list[Driver])->dict|None:
    if lst1 is None:
        return None
    dict1 = {}
    for i in range(len(lst1)):
        dict1[lst1[i].name_of_driver, "(Daily drive time)"] = repr(lst1[i].time_driving_per_day)
    return dict1

print(dictionary_drive_time_persons(drivers_1))
print("")

#Connor Nowak created this function to give the miles used by the cars in a dictionary.

def dictionary_drive_miles_vehicles(lst2:list[Vehicle])->dict|None:
    if lst2 is None:
        return None
    dict2 = {}
    for i in range(len(lst2)):
        dict2[lst2[i].name_of_car, "(daily miles)"] = (lst2[i].miles_used_per_day)
    return dict2

print(dictionary_drive_miles_vehicles(vehicles_1))
print("")
#Connor Nowak

def gas_cost(list1:list[Vehicle],cost_of_gas:float)->float:
    monthly_gas_cost = 0
    for car in list1:
        try:
            gas_cost = (car.miles_used_per_day/car.mpg)*cost_of_gas
        except ZeroDivisionError:
            gas_cost = 0
        monthly_gas_cost += (gas_cost*30)
    return monthly_gas_cost

print("Your monthly gas cost is:", gas_cost(vehicles_1,cost_of_gas))


#Connor Nowak

def gas_budget(list1:list[Vehicle], monthly_gas_budget:float, cost_of_gas:float)->bool:
    if list1 == []:
        return True
    for driver in list1:
        if gas_cost(list1,cost_of_gas) > monthly_gas_budget:
            x = abs(gas_cost(list1,cost_of_gas) - monthly_gas_budget)
            print("You are over budget by: $",x)
            return False
        else:
            x = abs(gas_cost(list1, cost_of_gas) - monthly_gas_budget)
            print("You are under budget by: $",x)
            return True
gas_budget(vehicles_1, monthly_gas_budget, cost_of_gas)

#Thomas James

def exceed_average(list1:list[Vehicle], gas_money:float, cost_of_gas)->None:
    for car in list1:
        try:
            if (car.miles_used_per_day/car.mpg*cost_of_gas)*30 > (gas_money/len(list1)):
                print(car.name_of_car, "is over budget on gas")
            else:
                print(car.name_of_car, "is under budget on gas")
        except ZeroDivisionError:
            print(car.name_of_car, "is under budget on gas")

exceed_average(vehicles_1, monthly_gas_budget, cost_of_gas)
print("")

#Connor Nowak created this function to put the MPG in a dictionary.

def dictionary_mpg(lst2:list[Vehicle])->dict|None:
    if lst2 is None:
        return None
    dict2 = {}
    for i in range(len(lst2)):
        dict2[lst2[i].name_of_car,"(miles per gallon)"] = repr(lst2[i].mpg)
    return dict2

print(dictionary_mpg(vehicles_1))
print("")

#Thomas James created this function to print the dictionary for total gas that money that each car is using and the amount each car goes over on gas budget.

def gas_dictionary(lst2:list[Vehicle], cost_of_gas:float, budget:float)->dict:
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
print('')



#Thomas James created this function to pair drivers to a vehicle that was entered based on a "safety rating", which is based on the age of the driver factored with the number of accidents the driver has been in, in the last 12 months.
#The vehicle with the lowest top speed was given to the driver with the lowest safety rating.

print("Other suggestions:")

def driver_to_car(list1:list[Driver], list2:list[Vehicle])->None:
    for x in range(len(list1)-1):
        small_idx = x
        for j in range(x+1,len(list1)):
            if safety_rating(list1[j]) > safety_rating(list1[small_idx]):
                small_idx = j
        if small_idx!=x:
            temp = list1[x]
            list1[x] = list1[small_idx]
            list1[small_idx] = temp
    vehicle_order = []
    for vehicle in list2:
        x = vehicle.top_speed
        best_vehicle = vehicle
        for i in range(list2.index(vehicle)+1,len(list2)):
            if list2[i].top_speed >= x:
                best_vehicle = list2[i]
        vehicle_order.append(best_vehicle)
    if len(list1)==len(list2):
        x = [[list1[i].name_of_driver, vehicle_order[i].name_of_car]for i in range(len(list2))]
        print("The best driving pairs based off of driving history are:", x)
    else:
        print("Different amount of cars and drivers. Try pairing less experienced drivers with safer cars.")

driver_to_car(drivers_1, vehicles_1)

#Connor Nowak

def rush_hour_suggestions(list1:list[Driver])->None:
    for driver in list1:
        if driver.stuck_in_traffic_count >= 2:
            print(driver.name_of_driver, "- Try to avoid driving during the hours of 7am-9am and 4pm-6:30pm as much as possible.")
        else:
            continue

rush_hour_suggestions(drivers_1)