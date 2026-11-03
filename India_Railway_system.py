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
# print(" --- Indian Railway Booking System --- ")
# Passenger_name = input("Enter passenger name : ")
# Age = int(input("Enter Age : "))
# Destination = input("Enter Destination : ")

# # Display booking Confirmation
# print("\n --- Booking Details --- ")
# print(f"passenger : {Passenger_name}")
# print(f"Age : {Age}")
# print(f"Destination : {Destination}")
# print("Booking confirmed!!!")

#Arthimetic Operators

# Base_price = 1500
# Service_charge = 100
# Total_price = Base_price + Service_charge

# print(f"Base Price : ₹{Base_price}")
# print(f"Service Charge : ₹{Service_charge}")
# print(f"Total Price : ₹{Total_price}")

# Comparison Operators
# passengers_age = 25
# senior_citizen_age = 60
# is_senior = passengers_age >= senior_citizen_age

# print(f"\nIs passenger senior citizen? {is_senior}")



#Logical operators
# has_ticket = True
# has_id_proof = True
# can_board = has_ticket and has_id_proof

# print(f"Can Board Train? {can_board}")


#Control Flow - If Statements

#Age based Pricings

# Age = int(input("Enter passenger Age : "))

# if Age < 5:
#     price = 0
#     category = "Infant (FREE)"
# elif Age < 12:
#     price = 750
#     Category = "Child (50% DISCOUNT)"
# elif Age >= 60:
#     price = 1200 
#     category = "Senior Citizen (20% DISCOUNT)"
# else:
#     price = 1500
#     category = "Adult"

# print(f"Category : {category}")
# print(f"Ticket Price : ₹{price}")

# For Loop - Display available trains 

Trains = [
    {"name": "Rajdhani Express",
     "number": 12303,
     "destination":"New Delhi"},
     {"name": "Shatabdi Express",
          "number": 11306,
          "destination":"Chennai"},
    {"name": "Duronto Express",
         "number": 23231,
         "destination":"Mumbai"},
]

print("Available Trains: ")
for Train in Trains : 
    print(f"{Train['number']} - {Train['name']} to {Train['destination']}")


#While loop - Booking  System Menu

print("\n --- Booking Menu --- ")
choice = 0

while choice != 3:
    print("1. Book Ticket")
    print("2. Check Status")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Booking ticket ...")
    elif choice ==2:
        print("Checking Status")
    elif choice == 3:
        print("Thank you for using Indian Railways🙏")
    else:
        print("Invalid Choice😵‍💫")