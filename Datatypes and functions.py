# # list

# states = ["Maharastra","Kerela","Goa","Punjab","Haryana","Gujrat"]

# print("Original list : ",states)

# states.append("karnataka")
# states.insert(2,"Rajasthan")
# print("After Append & Insert: ",states)

# states.extend(["Sikkim","Bihar"])
# print("After extend: ",states)

# states.remove("Bihar")
# popped = states.pop()
# print("Removed Elements: ",popped)
# print("After Remove & Pop: ",popped)

# # Sorting and Reverse

# states.sort()
# print("Sorted list: ",states)
# states.reverse()
# print("Reversed List: ",states)

# print("Index of Punjab: ",states.index("Punjab"))
# print("count of Punjab: ",states.count("Punjab"))

# copy_states = states.copy()
# print("Copied list : ",copy_states)
# states.clear()
# print("Cleared list: ",states)



# # Tuple
# cities = ("Mumbai","Delhi","Banglore","Chennai","Kolkata","Mumbai")
# print("Tuple : ",cities)

# # Count
# print("Count of Mumbai: ",cities.count("Mumbai"))

# #Index
# print("Index of kolkata: ",cities.index("Kolkata"))

# # Length
# print("Length: ",len(cities))

# # Members
# print("Delhi in tuple?","Delhi" in cities)

# #Min & Max (Alphabetically)
# print("Min: ",min(cities))
# print("Max: ",max(cities))

# Dictionaries
capitals = {
    "Maharastra" : "Mumbai",
    "Goa" : "Panji",
    "Tamil Nadu" : "Chennai",
    "Gujrat" : "Gandhinagar"
}

print("dictionary : ",capitals)

#Get & Access
print("Capital of Goa : ",capitals.get("Goa"))


# # Key, Values , Items

# print("states: ",capitals.keys())
# print("Capitals: ",capitals.values())
# print("Pairs: ",capitals.items())

# # Update & Add
# capitals.update({"Karnataka": "Banglore"})
# capitals["Punjab"] = "Chandigarh"
# print("After Update: ",capitals)

# # Remove
# capitals.pop("Tamil Nadu")
# capitals.popitem()
# print("After pop & popitem: ",capitals)

# # Copy & Clear
# copy_caps = capitals.copy()
# capitals.clear()
# print("Copies : ",copy_caps)
# print("Cleared: ",capitals)


# Set
languages = {"Hindi","English","Marathi","Tamil","Telugu"}
print("Original Set: ",languages)

#Add & Remove

languages.add("Haryanvi")
languages.discard("English")
print("After Add & Discard: ",languages)

languages.remove("Tamil")

# Set Operations
south = ("Tamil","Telugu","Kannada")
print("Union: ",languages.union(south))
print("Intersection: ",languages.intersection(south))
print("Difference: ",languages.difference(south))
print("symmetric Difference: ",languages.symmetric_difference(south))

#String
movie = "Ranjhana is a Classic Movie"
print("Original: ",movie)

#Case
print(movie.upper())
print(movie.lower())
print(movie.title())
print(movie.capitalize())
print(movie.swapcase())

#Check
print(movie.startswith("Samyak"))
print(movie.endswith("Movie"))
print("Is Alpha: ",movie.isalpha())
print("Is Digital: ",movie.isdigit())

# Find & Replace
print("Find 'Classic': ",movie.find("Classic"))
print(movie.replace("Classic","Legendary"))

#split & Join
words = movie.split()
print("Split: ",words)
joined = "-".join(words)
print("joined: ",joined)


#Strip
line = "    Jai Hind    "
print("Stripped: ",line.strip())
print("Left Strip: ",line.lstrip())
print("Right Strip: ",line.rstrip())

# Date & time

import datetime
now = datetime.datetime.now()
print("Now: ",now)

today = datetime.date.today()
print("today : ",today)

Birthdate = datetime.date(2004,3,20)
print("Birth Date: ",Birthdate.strftime("%d-%B-%y"))

# time Difference
diff = today - Birthdate
print("Days After Birth: ",diff.days)

# Current Components
print("Year: ",now.year)
print("Month: ",now.month)
print("day: ",now.day)
print("Hour: ",now.hour)
print("Minutes: ",now.minute)
print("Second: ",now.second)

#Create a time object
t = datetime.time(10,30,15)
print("Custom Time: ",t)

# Combine Date & Time
dt = datetime.datetime.combine(today,t)
print("Combined Datetime: ",dt)

#formating
print("Formatted: ",now.strftime("%A,%d %B %Y %I:%M %p"))
