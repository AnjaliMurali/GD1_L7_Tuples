def get_group_details():
    groupname = input("Enter the group name: ")
    Sizeofthegroup = int(input("Enter the size of the group: "))
    dateofthecompetition = input("Enter the date of the competition (YYYY-MM-DD): ")
    venue = input("Enter the venue of the competition: ")
    typeofthemedal = input("Enter the type of the medal: ")
    
    # Creating a tuple with the group details
    group_details = (groupname, Sizeofthegroup, dateofthecompetition, venue, typeofthemedal)
    return group_details

# List to store details of all five groups
groups = []

# Loop to get details for 5 groups
for i in range(5):
    print(f"\nEnter details for group {i+1}:")
    group = get_group_details()
    groups.append(group)

# Displaying all groups' details
print("\nAll groups' details:")
for group in groups:
    print(group)
