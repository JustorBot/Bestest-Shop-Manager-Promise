import json
from ctuClass import ctuStock

#All thes shops save file names  
#Items          
shop1Items = "shop1_items.txt"
shop2Items = "shop2_items.txt"
shop3Items = "shop3_items.txt"
shop4Items = "shop4_items.txt"

#Shop Names
shop1Name = "shop1_name.txt"
shop2Name = "shop2_name.txt"
shop3Name = "shop3_name.txt"
shop4Name = "shop4_name.txt"

#Shop Locations
shop1Location = "shop1_location.txt"
shop2Location = "shop2_location.txt"
shop3Location = "shop3_location.txt"
shop4Location = "shop4_location.txt"

#Shop Custormers
shop1Custormers = "shop1_customers.txt"
shop2Custormers = "shop2_customers.txt"
shop3Custormers = "shop3_customers.txt"
shop4Custormers = "shop4_customers.txt"

#Shop Sales
shop1Sales = "shop1_sales.txt"
shop2Sales = "shop2_sales.txt"
shop3Sales = "shop3_sales.txt"
shop4Sales = "shop4_sales.txt"

#All shop objects information storage
#Uses the save files to store variables
shop1 = ctuStock(shop1Name, shop1Location, shop1Custormers, shop1Sales, 0, shop1Items)
shop2 = ctuStock(shop2Name, shop2Location, shop2Custormers, shop2Sales, 0, shop2Items)
shop3 = ctuStock(shop3Name, shop3Location, shop3Custormers, shop3Sales, 0, shop3Items)
shop4 = ctuStock(shop4Name, shop4Location, shop4Custormers, shop4Sales, 0, shop4Items)

#Heading
print("Welcome to CTU Technologies\n")

#List of the shops available
shops = [shop1, shop2, shop3, shop4]

#Menu Picker
#Works for all menus with them numbers
options = [0, 1, 2, 3, 4, 99]

#Shop Name Checker
optionsName = ['']

#Location Picker
#Forces these Locations with the Default location being Default
optionsLocation = ['KZN', "Free State", "Gauteng", "Limpopo", "Default"]

#Shops application runner
while True:
    #Main Menu options
    print("1. Shop Management")
    print("2. Sales")
    print("3. Returns")
    print("4. Stock")
    print("99. Exit\n")
    
    #The option picker for main menu
    try:
        optionChoosen = int(input("Select an option or 99 to exit: "))
    except ValueError:
        print("Invalid input. Please enter a valid option number or 99 to exit.")
        continue

    if optionChoosen not in options:
        print("Invalid option. Please enter a valid option number or 99 to exit.")
        continue
    
    #Logic behind the Shop Management option on main menu
    #Shop management menu
    if optionChoosen == 1:
        print("Shop Management")
        print("1. Change shop Name")
        print("2. Change shop location")
        print("3. Display current shops")
        print("4. Display all shops information")
        print("0. Back\n")

        #The option picker for Shop management menu
        try:
            shopMangaeChoice = int(input("Select an option: "))
        except ValueError:
            print("Invalid input. Please enter a valid option number or 99 to exit.")
            continue

        if shopMangaeChoice not in options:
            print("Invalid option. Please enter a valid option number or 99 to exit.")
            continue
    
        #Displays each shop object
        if shopMangaeChoice == 1:
            print("Change Shop name\n")
            print("Select Shop")

            # Loop over the shops and print the names
            for i, shop in enumerate(shops):
                shop_names = shop.show_shopName()
                print(f"{i+1}. {' '.join(shop_names)}")
        
            #The option picker for changing the name of a shop
            try:
                shopNameChoice = int(input("Select an option: "))
            except ValueError:
                print("Invalid input. Please enter a valid option number or 99 to exit.")
                continue

            if shopNameChoice not in options:
                print("Invalid option. Please enter a valid option number or 99 to exit.")
                continue
            
            #Logic for the name changing of shops
            if shopNameChoice == 1:
                #The option picker for changing a shops Name
                try:
                    newShopName = input("Type Shop Name: ")
                except ValueError:
                    print("Invalid input. Please enter a valid Name")
                    continue

                if newShopName in optionsName:
                    print("Invalid option. Please enter a valid Name.")
                    continue
                
                shop1Name = newShopName
                shop1.add_shopName(shop1Name)
                
                shop1.show_shopName()
                print("")
                print("Shop Name successfully changed to {}".format(shop1Name))
                print("")
            elif shopNameChoice == 2:
                #The option picker for changing a shops Name
                try:
                    newShopName = input("Type Shop Name: ")
                except ValueError:
                    print("Invalid input. Please enter a valid Name")
                    continue

                if newShopName in optionsName:
                    print("Invalid option. Please enter a valid Name.")
                    continue
                
                shop2Name = newShopName
                shop2.add_shopName(shop2Name)
                
                shop2.show_shopName()
                print("")
                print("Shop Name successfully changed to {}".format(shop2Name))
                print("")
            elif shopNameChoice == 3:
                #The option picker for changing a shops Name
                try:
                    newShopName = input("Type Shop Name: ")
                except ValueError:
                    print("Invalid input. Please enter a valid Name")
                    continue

                if newShopName in optionsName:
                    print("Invalid option. Please enter a valid Name.")
                    continue
                
                shop3Name = newShopName
                shop3.add_shopName(shop3Name)
                
                shop3.show_shopName()
                print("")
                print("Shop Name successfully changed to {}".format(shop3Name))
                print("")
            elif shopNameChoice == 4:
                #The option picker for changing a shops Name
                try:
                    newShopName = input("Type Shop Name: ")
                except ValueError:
                    print("Invalid input. Please enter a valid Name")
                    continue

                if newShopName in optionsName:
                    print("Invalid option. Please enter a valid Name.")
                    continue
                
                shop4Name = newShopName
                shop4.add_shopName(shop4Name)
                
                shop4.show_shopName()
                print("")
                print("Shop Name successfully changed to {}".format(shop4Name))
                print("")
         
        #Logic for the location changing of a shop       
        elif shopMangaeChoice == 2:
            print("Change Shop Location\n")
            print("Select Shop")
            for i, shop in enumerate(shops):
                shop_names = shop.show_shopName()
                shop_locations = shop.show_shopLocation()
                print(f"{i+1}. {' '.join(shop_names)}, {''.join(shop_locations)}")
            
            #The option picker for changing a shops location
            try:
                shopLocationChoice = int(input("Select an option: "))
            except ValueError:
                print("Invalid input. Please enter a valid option number or 99 to exit.")
                continue

            if shopLocationChoice not in options:
                print("Invalid option. Please enter a valid option number or 99 to exit.")
                continue
            
            #Logic for changging the shops location
            if shopLocationChoice == 1:
                #Location Option Picker
                try:
                    newShop1Location = input("Enter a location Free State, Gauteng, KZN, Limpopo: ")
                except ValueError:
                    print("Invalid input. Please enter a valid option number or 99 to exit.")
                    continue

                if newShop1Location not in optionsLocation:
                    print("Invalid option. Please enter a valid option")
                    continue
                shop1Location = newShop1Location
                shop1.add_shopLocation(shop1Location)
                shop1.show_shopLocation()
                print("")
                print("Shop Location successfully changed to {}".format(shop1Location))
                print("")
            elif shopLocationChoice == 2:
                #Location Option Picker
                try:
                    newShop2Location = input("Enter a location Free State, Gauteng, KZN, Limpopo: ")
                except ValueError:
                    print("Invalid input. Please enter a valid option number or 99 to exit.")
                    continue

                if newShop2Location not in optionsLocation:
                    print("Invalid option. Please enter a valid option")
                    continue
                shop2Location = newShop2Location
                shop2.add_shopLocation(shop2Location) 
                newShop2Location.show_shopLocation()
                print("")
                print("Shop Location successfully changed to {}".format(shop2Location))
                print("")
            elif shopLocationChoice == 3:
                #Location Option Picker
                try:
                    newShop3Location = input("Enter a location Free State, Gauteng, KZN, Limpopo: ")
                except ValueError:
                    print("Invalid input. Please enter a valid option number or 99 to exit.")
                    continue

                if newShop3Location not in optionsLocation:
                    print("Invalid option. Please enter a valid option")
                    continue
                shop3Location = newShop3Location
                shop3.add_shopLocation(shop3Location)
                shop3.show_shopLocation()
                print("")
                print("Shop Location successfully changed to {}".format(shop3Location))
                print("")
            elif shopLocationChoice == 4:
                #Location Option Picker
                try:
                    newShop4Location = input("Enter a location Free State, Gauteng, KZN, Limpopo: ")
                except ValueError:
                    print("Invalid input. Please enter a valid option number or 99 to exit.")
                    continue
                if newShop4Location not in optionsLocation:
                    print("Invalid option. Please enter a valid option")
                    continue
                shop4Location = newShop4Location
                shop4.add_shopLocation(shop4Location)
                shop4.show_shopLocation()
                print("")
                print("Shop Location successfully changed to {}".format(shop4Location))
                print("")
        
        #Logic for displaying Current Shops  
        elif shopMangaeChoice == 3:
            for i, shop in enumerate(shops):
                shop_names = shop.show_shopName()
                shop_locations = shop.show_shopLocation()
                print(f"{i+1}. {' '.join(shop_names)}, {''.join(shop_locations)}")
            print("")
        
        #Logic for displaying all information about a shop   
        elif shopMangaeChoice == 4:
            for i, shop in enumerate(shops):
                shop_names = shop.show_shopName()
                shop_locations = shop.show_shopLocation()
                shop_custormers = shop.show_shop_customers()
                shop_sales = shop.show_shop_sales()
                print(f"---------------- \n\nShop Name: {' '.join(shop_names)} \nShop Location: {' '.join(shop_locations)} \nNumber of Custormers: {' '.join(shop_custormers)} \nSales: {' '.join(shop_sales)} \nReturns: {shop.returns} \n\n---------------- \n\n")
            print("")
            
    #Logic behind the Sales Menu option on main menu  <---------------------------------------------------------------------
    elif optionChoosen == 2:
        #Shop  selection
        print("Select a shop:")
        for i, shop in enumerate(shops):
            shop_names = shop.show_shopName()
            shop_locations = shop.show_shopLocation()
            print(f"{i+1}. {' '.join(shop_names)}")
        choice = input("Enter a number: ")
        if not choice.isdigit() or int(choice) < 1 or int(choice) > len(shops):
            print("Invalid choice.")
            continue
        shop = shops[int(choice)-1]

        #Shows the shop items available
        print("")
        shop.show_items()
        print("")

        #Main logic
        while True:
            #Menu of options
            print("Select an option:")
            print("1. Add items to stock (admin only)")
            print("2. Buy items")
            print("3. Go back")
            choice = input("Enter a number: ")
            if not choice.isdigit() or int(choice) < 1 or int(choice) > 3:
                print("Invalid choice.")
                continue
            
            #ADMIN panel
            if choice == "1":
                #Password
                password = input("Enter the admin password: ")
                if password != "ADMIN":
                    print("Incorrect password.")
                    continue
                #Adding Items
                #Item
                try:
                    item = input("Enter the item to add: ")
                except ValueError:
                    print("Invalid input. Please enter a valid Item")
                    continue

                if item in optionsName:
                    print("Invalid option. Please enter a valid Item.")
                    continue
                #Price
                while True:
                    try:
                        price = float(input("Enter the price: "))
                        if price < 0:
                            print("Invalid input. Please enter a non-negative integer.")
                            continue  
                        break  
                    except ValueError:
                        print("Invalid input. Please enter a valid integer.")

                if price in optionsName:
                    print("Invalid option. Please enter a valid Price.")
                    continue
                #Quantity
                while True:
                    try:
                        quantity = int(input("Enter the quantity to add: "))
                        if quantity < 0:
                            print("Invalid input. Please enter a non-negative integer.")
                            continue  
                        break  
                    except ValueError:
                        print("Invalid input. Please enter a valid integer.")

                if quantity in optionsName:
                    print("Invalid option. Please enter a valid Quantity.")
                    continue
                shop.add_stock(item, price, quantity)
                print(f"{quantity} {item} added to stock.")

            #Buying of stuff 
            elif choice == "2":
                cart = {}
                #Main buying loop to buy multiple items
                while True:
                    #Gets Item
                    item = input("Select an item to buy or 'done' to finish: ")
                    if item == "done":
                        break
                    if item not in shop.inventory:
                        print("Invalid item.")
                        continue
                    #Gets the Amount wanted
                    while True:
                        try:
                            quantity = int(input("Enter the quantity to buy: "))
                            if quantity < 0:
                                print("Invalid input. Please enter a non-negative integer.")
                                continue  
                            break  
                        except ValueError:
                            print("Invalid input. Please enter a valid integer.")

                    if quantity > shop.inventory[item]['stock']:
                        print(f"Not enough {item} in stock.")
                        continue
                    cart[item] = quantity

                #The cart items
                shop.sell_items(cart)

            #Ends the loop
            else:
                break
        
    #Logic behind the Returns Menu option on main menu  <---------------------------------------------------------------------
    elif optionChoosen == 3:
        #Shop  selection
        print("Select a shop:")
        for i, shop in enumerate(shops):
            shop_names = shop.show_shopName()
            shop_locations = shop.show_shopLocation()
            print(f"{i+1}. {' '.join(shop_names)}")
        choice = input("Enter a number: ")
        if not choice.isdigit() or int(choice) < 1 or int(choice) > len(shops):
            print("Invalid choice.")
            continue
        shop = shops[int(choice)-1]

        #Shows the shop items available
        print("")
        shop.show_items()
        print("")

        #Main logic
        cart = {}

        #Logic Behind Return loop
        while True:
            #Gets Item
            item = input("Select an item to return or 'done' to finish: ")
            if item == "done":
                break
            if item not in shop.inventory:
                print("Invalid item.")
                continue
            #Quantity
            while True:
                try:
                    quantity = int(input("Enter the quantity to return: "))
                    if quantity < 0:
                        print("Invalid input. Please enter a non-negative integer.")
                        continue  
                    break  
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")

                if quantity in optionsName:
                    print("Invalid option. Please enter a valid Quantity.")
                    continue
            #Checks Quantity of Return
            if quantity > shop.inventory[item]['stock']:
                print(f"Sorry, pls return less {shop.inventory[item]['stock']} of {item} in stock.")
                continue
            cart[item] = quantity
            print(f"{quantity} {item}(s) returned")
            shop.inventory[item]['stock'] += quantity

        #Display cart and total cost
        print("Your shopping cart:")
        for item, quantity in cart.items():
            print(f"{quantity} {item}(s)")
        shop.save_inventory()
        total_cost = sum([quantity * shop.inventory[item]['price'] for item, quantity in cart.items()])
        print(f"Total return price: {total_cost}")

    
    #Logic behind the Stock on main menu  
    elif optionChoosen == 4:
        #Shop  selection
        print("Select a shop:")
        for i, shop in enumerate(shops):
            shop_names = shop.show_shopName()
            shop_locations = shop.show_shopLocation()
            print(f"{i+1}. {' '.join(shop_names)}")
        choice = input("Enter a number: ")
        if not choice.isdigit() or int(choice) < 1 or int(choice) > len(shops):
            print("Invalid choice.")
            continue
        shop = shops[int(choice)-1]

        #Shows the shop items available
        print("")
        shop.show_items()
        print("")

        #Main logic
        while True:
            #Menu of options
            print("Select an option:")
            print("1. Add items to stock (admin only)")
            print("3. Go back")
            choice = input("Enter a number: ")
            if not choice.isdigit() or int(choice) < 1 or int(choice) > 3:
                print("Invalid choice.")
                continue
            
            #ADMIN panel
            if choice == "1":
                #Password
                password = input("Enter the admin password: ")
                if password != "ADMIN":
                    print("Incorrect password.")
                    continue
                #Items Adding
                #Item
                try:
                    item = input("Enter the item to add: ")
                except ValueError:
                    print("Invalid input. Please enter a valid Item")
                    continue

                if item in optionsName:
                    print("Invalid option. Please enter a valid Item.")
                    continue
                #Price
                while True:
                    try:
                        price = float(input("Enter the price: "))
                        if price < 0:
                            print("Invalid input. Please enter a non-negative integer.")
                            continue  
                        break  
                    except ValueError:
                        print("Invalid input. Please enter a valid integer.")

                if price in optionsName:
                    print("Invalid option. Please enter a valid Price.")
                    continue
                #Quantity
                while True:
                    try:
                        quantity = int(input("Enter the quantity to add: "))
                        if quantity < 0:
                            print("Invalid input. Please enter a non-negative integer.")
                            continue  
                        break  
                    except ValueError:
                        print("Invalid input. Please enter a valid integer.")

                if quantity in optionsName:
                    print("Invalid option. Please enter a valid Quantity.")
                    continue
                shop.add_stock(item, price, quantity)
                print(f"{quantity} {item} added to stock.")
            
            #Ends the loopy   
            else:
                print("")
                break
           
    #Ends the application
    elif optionChoosen == 99:
        print("Exiting...")
        break