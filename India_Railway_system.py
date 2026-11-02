# Defining Variables for Indian Railway System

train_name = "Rajdhani Express"
train_number = 12301
ticket_price = 2450.50
is_ac_available = True
seat_numbers = [1, 2, 3, 4, 5]

# Showing the Details using print Function

# print("train Name : ",train_name)
# print("train Number : ",train_number)
# print("ticket price : ",ticket_price)
# print("is AC available : ",is_ac_available)
# print("seat Numbers : ",seat_numbers)

# Show the data types of the variables using type function

# print("the data type of train_name : ",type(train_name))
# print("the data type of train_number : ",type(train_number))
# print("the data type of ticket_price : ",type(ticket_price))
# print("the data type of is_ac_available : ",type(is_ac_available))
# print("the data type of seat_numbers : ",type(seat_numbers))

# Getting passangers information
print(" --- Indian Railway Booking System --- ")
Passenger_name = input("Enter passenger name : ")
Age = int(input("Enter Age : "))
Destination = input("Enter Destination : ")

# Display booking Confirmation
print("\n --- Booking Details --- ")
print(f"passenger : {Passenger_name}")
print(f"Age : {Age}")
print(f"Destination : {Destination}")
print("Booking confirmed!!!")