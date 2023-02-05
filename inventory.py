
#========The beginning of the class==========
class Shoe:
    # creator to initialise different class attributes in Shoe
    def __init__(self, country, code, product, cost, quantity): 
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # method to get cost of a Shoe object
    def get_cost(self):
        return int(self.cost)

    # method to get quantity of a Shoe object
    def get_quantity(self):
        return int(self.quantity)

    # method to return a srting representation of Shoe object
    def __str__(self):
        return f'''
                Product: {self.product}
                Country: {self.country}
                Code: {self.code}
                Cost: {self.cost}
                Quantity: {self.quantity}
                '''

#==========Functions outside the class==============
def read_shoes_data(shoe_list): # function to read shoe data from txt file and return a list of Shoe objects
    file = None
    try: # check if 'inventorty.txt' exists
        file = open('inventory.txt','r')
        lines = file.readlines()[1:] # skip first line of txt file
        for line in lines: # read each line, split line into different shoe attributes and call function to create shoe object
            line = line.strip("\n")
            shoe_data = line.split(",")
            shoe_list.append(capture_shoes(shoe_data[0],shoe_data[1],shoe_data[2],shoe_data[3],shoe_data[4]))
    except: # print message if txt file does not exist
        print("The file that you are trying to open does not exist")
    finally:
        if file is not None:
            file.close()
    return shoe_list

def capture_shoes(country, code, product, cost, quantity): # function to create and return shoe object
    shoes = Shoe(country, code, product, cost, quantity)
    return shoes

def view_all(shoe_list): # function to print string repesentation of each shoe object
    for i in range(0,len(shoe_list)):
        print(shoe_list[i].__str__())

def re_stock(shoe_list): # function to find shoe object with lowest quantity and add the user entered amount to that object
    shoe_quantity_list = get_quantity_list(shoe_list)
    min_quantity = min(shoe_quantity_list)
    min_index = shoe_quantity_list.index(min_quantity)
    print(f"{shoe_list[min_index].product} is with the lowest quantity, i.e. {shoe_list[min_index].quantity} pairs")
    select = input("Do you want to restock this item?(Please y for yes and n for no): ").lower()
    if select == "y":
        restock_quantity = int(input("Please enter how many pairs you want to add: "))
        shoe_list[min_index].quantity = str(shoe_list[min_index].get_quantity() + restock_quantity)
        update_shoes_data(shoe_list) # call function to update txt file

def search_shoe(shoe_list): # function to ask user to enter a shoe code and print string representation of corresponding shoe object
    shoe_code_list = []
    for i in range(0,len(shoe_list)):
        shoe_code_list.append(shoe_list[i].code)
    while True:
        search_code = input("Please enter the code of the shoe you want to search: ")
        if search_code in shoe_code_list:
            search_index = shoe_code_list.index(search_code)
            print(shoe_list[search_index].__str__())
            break
        else:
            print("The entered code is invalid, please try again!")

def value_per_item(shoe_list,index): # function to find value of shoe object i.e. cost times quantity
    value = shoe_list[index].get_cost() * shoe_list[index].get_quantity()
    return value

def highest_qty(shoe_list): # function to find shoe object with highest quantity and print 'as being for sale'
    shoe_quantity_list = get_quantity_list(shoe_list)
    max_quantity = max(shoe_quantity_list)
    max_index = shoe_quantity_list.index(max_quantity)
    print(f"{shoe_list[max_index].product} is with the highest quantity and being for sale")

def get_quantity_list(shoe_list): # function to create a list of quantity of corresponding shoe object with respect to its index
    shoe_quantity_list = []
    for i in range(0,len(shoe_list)):
        shoe_quantity_list.append(shoe_list[i].get_quantity())
    return shoe_quantity_list

def update_shoes_data(shoe_list): # function to open and write 'inventory.txt' file
    update_file_line_list = ["Country,Code,Product,Cost,Quantity"]
    for i in range(0,len(shoe_list)):
        string = shoe_list[i].country+","+shoe_list[i].code+","+shoe_list[i].product+","+shoe_list[i].cost+","+shoe_list[i].quantity
        update_file_line_list.append(string)
    file = None
    try:
        file = open('inventory.txt','w')
        for i in range(0,len(update_file_line_list)):
            file.write(update_file_line_list[i]+"\n")
    except:
        print("The file that you are trying to open does not exist")
    finally:
        if file is not None:
            file.close()
#==========Main Menu=============
action = ""

while action != "e":
    shoe_list = [] # define a empty shoe_list
    shoe_list = read_shoes_data(shoe_list) # call fucntion to read shoes data from txt file
    
    # ask user to enter the action he/she wants to perform, lower() to prevent case sensitive
    action = input('''Select one of the following Options below:
    va - View all shoes
    as - add a new shoe
    rs - Restock shoe with lowest quantity
    ss - Search a shoe by shoe code
    hq - Find shoe with highest quantity and mark as being for sale
    v - Find value of each shoe
    e - Exit
    : ''').lower()

    if action == "va":
        view_all(shoe_list) # call fucntion to view all shoes
    
    elif action == "as": # ask user to enter new shoe attributes and create a new Shoe object and update 'inventory.txt'
        new_shoe_country = input("Please enter country of the new shoe: ")
        new_shoe_code = input("Please enter code of the new shoe: ")
        new_shoe_product = input("Please enter product of the new shoe: ")
        new_shoe_cost = input("Please enter cost of the new shoe: ")
        new_shoe_quantity = input("Please enter quantity of the new shoe: ")
        new_shoe = capture_shoes(new_shoe_country,new_shoe_code,new_shoe_product,new_shoe_cost,new_shoe_quantity)
        shoe_list.append(new_shoe)
        update_shoes_data(shoe_list)

    elif action == "rs":
        re_stock(shoe_list) # call function to restock shoe
    
    elif action == "ss":
        search_shoe(shoe_list) # call function to search by shoe code
    
    elif action == "hq":
        highest_qty(shoe_list) # call function to find shoe with highest quantity
    
    elif action == "v": # print value of each shoe object one by one
        for i in range(0,len(shoe_list)):
            value = str(value_per_item(shoe_list,i)) # call function to determine value of current shoe object
            print(f"The value of {shoe_list[i].product} is {value}")
    
    elif action == "e":
        print("Thanks and goodbye!")
    
    else:
        print("You have entered an invalid action, please try again!")