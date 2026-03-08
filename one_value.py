from classes import Vehicle
from classes import Driver
from classes import Time
import dict_func
from dict_func import gas_dictionary

vehicles_1 = [Vehicle('Tesla', 'Electric', 0.0, 30, 200 ),
              Vehicle('Truck', 'Gas', 20.0, 15, 110),
              Vehicle('Minivan', 'Gas', 28.0, 35, 105)]
drivers_1 = [Driver('Daughter', 17, Time(1,0), 1, 2),
             Driver('Father', 45, Time(1,15), 2, 1),
             Driver('Mother', 47, Time(1,15), 2, 0)]
monthly_gas_budget = 140.0

estimated_cost_per_gallon = 4.0
#Supporting functions
def safety_rating(Driver) -> int:
    return Driver.driver_age-Driver.accident_count*10

#time_week_cars: Returns the total weekly drive time for all the drivers together. Thomas James.
def time_week_drivers(list1:list[Driver])->Time:
    total_time_minutes = 0
    for driver in list1:
        total_time_minutes += driver.time_driving_per_day.hours*60 + driver.time_driving_per_day.minutes
    return Time(total_time_minutes//60, total_time_minutes%60)

print("Total weekly drive time is -", time_week_drivers([Driver('Daughter', 17, Time(1,0), 1, 2),
             Driver('Father', 45, Time(1,15), 2, 1),
             Driver('Mother', 47, Time(1,15), 2, 0)]))

#compare_average: Tells the drivers whether they are over the national average of driving based on their number of drivers. Thomas James.

def compare_average(list1:list[Driver]) -> None:
    your_time = time_week_drivers(list1)
    your_minutes = your_time.hours*60+your_time.minutes
    try:
        if your_minutes/len(list1)>60.7:
            print("You are above the national average driving time by:", int((your_minutes/len(list1)-60.7)//1),"minutes.")
        else:
            print("You are below the national average driving time by:", abs(your_minutes/len(list1)-60.7)//1,"minutes. Great job!")
    except ZeroDivisionError:
        print ("")

compare_average(drivers_1)


#driver_to_car_pairs: Gives suggestions on what cars should be driven by which people. Thomas James.

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

#Determines whether to give rush hour suggestions. Thomas James.

def rush_hour_suggestions(list1:list[Driver])->None:
    for driver in list1:
        if driver.stuck_in_traffic_count >= 2:
            print(driver.name_of_driver, "- Try to avoid driving during the hours of 7am-9am and 4pm-6:30pm as much as possible.")
        else:
            continue

rush_hour_suggestions(drivers_1)


#Determines whether you are under or over budget on gas. Thomas James.
def gas_budget(list1:list[Vehicle], gas_money:float, cost_of_gas:float)->bool:
    if list1 == []:
        return True
    for driver in list1:
        if gas_cost(list1,cost_of_gas) > gas_money:
            x = abs(gas_cost(list1,cost_of_gas) - gas_money)
            print("You are over budget by: $",x)
            return False
        else:
            x = abs(gas_cost(list1, cost_of_gas) - gas_money)
            print("You are under budget by: $",x)
            return True

def exceed_average(list1:list[Vehicle], gas_money:float, cost_of_gas)->None:
    for car in list1:
        if gas_cost(list1,cost_of_gas) > (gas_money/len(list1)):
            print(car.name_of_car, "is over budget on gas")
        else:
            print(car.name_of_car, "is under budget on gas")
































