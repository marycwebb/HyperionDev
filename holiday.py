"""
Create a program that will calculate a user's entire holiday cost
First create 3 variables that will ask the user to input data about their holiday
Create a function that calculates the user's hotel cost 
Create a function that calculates the user's plane cost 
Create a function that calculates the user's car rental cost
Create variables for each of those functions with the user input as the argument
Create a fourth function that calculates the total cost of the holiday by adding the 3 previous functions together
Create a fourth variable of the function that calculates the total cost of the holiday
Print all of the information in a readable way for the user
"""
num_nights = int(input("Pleae enter how many nights you will be staying in a hotel: "))
city_flight = input("Please enter the city you are flying to: ")
rental_days = int(input("Please enter how many days you will be hiring a car: "))

def hotel_cost(num_nights):
   result = int(num_nights) * 100
   return result

def plane_cost(city_flight):
    
    if city_flight == "London":
        result = 200
    elif city_flight == "Manchester":
        result = 300
    elif city_flight == "Liverpool":
        result = 400
    else: result = 500
    return result

def car_rental(rental_days):
    result = int(rental_days) * 40
    return result

hotel_total = hotel_cost(num_nights)
plane_total = plane_cost(city_flight)
car_total = car_rental(rental_days)


def holiday_cost(hotel_cost, plane_cost, car_rental):
    result = hotel_cost + plane_cost + car_rental
    return result

print(holiday_cost(hotel_total, plane_total, car_total))

holiday_total = holiday_cost(hotel_total, plane_total, car_total)

print(f"""Your holiday breakday will be as follows:
      The total cost of your hotel stay will be: £{hotel_total}
      The total cost of your plane journey will be: £{plane_total}
      The total cost of your car rental will be: £{car_total}
      So the total cost of your entire holiday will be: £{holiday_total}
      Have a great trip!""")