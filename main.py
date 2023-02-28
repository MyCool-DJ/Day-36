# create an empty list to store names
name_list = []

# loop until the user wants to quit
while True:
    
    # get first name
    first_name = input("Enter first name: ").strip().capitalize()
    
    # get last name
    last_name = input("Enter last name: ").strip().capitalize()
    
    # construct the full name
    full_name = f"{first_name} {last_name}"
    
    # check and add the full name to the list if it does not already exist 
    if full_name not in name_list:
        name_list.append(full_name)
        # print the full list
        print(name_list)

