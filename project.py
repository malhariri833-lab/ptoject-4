# Step 1: Ask for Member Details
name = input("Enter your name: ")
club_name = input("Enter your school club name: ")

# Step 2: Store Details Using Different Data Types
member_number = 101
points = 25.5
event_count = 4
meeting_hours = 2.5
active = True

# Step 3: Print Values and Their Data Types
print(member_number, type(member_number))
print(points, type(points))
print(event_count, type(event_count))
print(meeting_hours, type(meeting_hours))
print(active, type(active))

# Step 4: Typecast Values into Text
member_number_text = str(member_number)
event_count_text = str(event_count)
points_text = str(points)
active_text = str(active)

# Step 5: Use String Indexing and Slicing
first_three = name[0:3]
last_letter = name[-1]

print(first_three)
print(last_letter)

# Step 6: Reverse the Club Name
secret_code = club_name[::-1]

# Step 7: Concatenate the Badge Lines
line1 = "Name: " + name
line2 = "Club: " + club_name
line3 = "Member Number: " + member_number_text
line4 = "Points: " + points_text
line5 = "Events: " + event_count_text
line6 = "Active: " + active_text
line7 = "Badge Code: " + first_three + last_letter
line8 = "Secret Club Code: " + secret_code

# Step 8: Run and Explore
print(line1)
print(line2)
print(line3)
print(line4)
print(line5)
print(line6)
print(line7)
print(line8)