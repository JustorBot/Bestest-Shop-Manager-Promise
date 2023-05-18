import json

#Shop/Store Class
class ctuStock():
    #Main Objects
    def __init__(self,shopName,shopLocation,customers_file,sales_file,returns,inventory_file):
        self.shopName = shopName
        self.shopLocation = shopLocation
        self.customers_file = customers_file
        self.customers = {}
        self.sales_file = sales_file
        self.sales = {}
        self.returns = returns
        self.inventory_file = inventory_file
        self.load_inventory()
        self.load_shopName()
        self.load_shopLocation()
        self.load_customers()
        self.load_sales()

#-------------------------START Items-------------------------
    #Adding the stock    
    def add_stock(self, item, price, quantity):
        if item in self.inventory:
            self.inventory[item]['stock'] += quantity
        else:
            self.inventory[item] = {'price': price, 'stock': quantity}
            self.save_inventory()

    #Selling of the items
    def sell_items(self, cart):
        total = 0
        print("Receipt:")
        for item, quantity in cart.items():
            if item not in self.inventory or self.inventory[item]['stock'] < quantity:
                print(f"Not enough {item} in stock.")
                continue
            price = self.inventory[item]['price']
            subtotal = price * quantity
            self.inventory[item]['stock'] -= quantity
            total += subtotal
            print(f"{quantity} x {item} = {subtotal:.2f}")
            ctuStock.increase_customer_count(self, 1) 
            ctuStock.increase_sales_count(self, 1)
        print(f"Total: {total:.2f}")
        self.save_inventory()
        self.save_customers()
        self.save_sales()

    #Displaying the items in a shop
    def show_items(self):
        print(f"Available items at {ctuStock.show_shopName(self)}:")
        for item, values in self.inventory.items():
            print(f"{item}: R{values['price']:.2f} ({values['stock']} in stock)")
            
#-------------------------END Items-------------------------

#-------------------------START Shop Name-------------------------
            
    #Adding Shop name 
    def add_shopName(self, nameShop):
        if nameShop in self.nameOfShop:
            print("Shop name already exists.")
        else:
            self.nameOfShop = {nameShop: {'Shops Name': nameShop}}
            self.save_shopName()

    # Display the names of all shops 
    def show_shopName(self):
        shop_names = list(self.nameOfShop.keys())
        if shop_names:
            return shop_names
        else:
            return ["No shop names found."]
   
    #Loading shop name 
    def load_shopName(self):
        try:
            with open(self.shopName, 'r') as f:
                self.nameOfShop = json.load(f)
        except FileNotFoundError:
            self.nameOfShop = {}
    
    #Saving shops name 
    def save_shopName(self):
        with open(self.shopName, 'w') as f:
            json.dump(self.nameOfShop, f)

#-------------------------END Shop Names-------------------------

#-------------------------START Shop Location-------------------------           
    #Adding Shop location 
    def add_shopLocation(self, locationShop):
        self.locationOfShop = {locationShop: {'Shops Location': locationShop}}
        self.save_shopLocation()

    # Display the location names of all shops 
    def show_shopLocation(self):
        shop_locations = list(self.locationOfShop.keys())
        if shop_locations:
            return shop_locations
        else:
            return ["No shop locations found."]
   
    #Loading shop location 
    def load_shopLocation(self):
        try:
            with open(self.shopLocation, 'r') as f:
                self.locationOfShop = json.load(f)
        except FileNotFoundError:
            self.locationOfShop = {}
    
    #Saving shops location 
    def save_shopLocation(self):
        with open(self.shopLocation, 'w') as f:
            json.dump(self.locationOfShop, f)

#-------------------------END Shop Location-------------------------

#-------------------------Items SAVING START-------------------------
    #Loading of the shop items save file
    def load_inventory(self):
        try:
            with open(self.inventory_file, 'r') as f:
                self.inventory = json.load(f)
        except FileNotFoundError:
            self.inventory = {}

    #Saving the shop items file
    def save_inventory(self):
        with open(self.inventory_file, 'w') as f:
            json.dump(self.inventory, f)

#-------------------------Items SAVING END-------------------------

#-------------------------START Customer-------------------------              
    def increase_customer_count(self, shop_number):
        if shop_number not in self.customers:
            self.customers[shop_number] = {'Shop Location': str(shop_number), 'Customer Count': 0}

        self.customers[shop_number]['Customer Count'] += 1

    def show_shop_customers(self):
        shop_customers = [str(shop_data.get('Customer Count', 0)) for shop_data in self.customers.values()]
        if shop_customers:
            return shop_customers
        else:
            return ["0"]

    def load_customers(self):
        try:
            with open(self.customers_file, 'r') as f:
                self.customers = json.load(f)
        except FileNotFoundError:
            self.customers = {}

    def save_customers(self):
        if self.customers:
            with open(self.customers_file, 'w') as f:
                json.dump(self.customers, f)
                
#-------------------------Customer Count SAVING END-------------------------

#-------------------------START Sales-------------------------
    def increase_sales_count(self, shop_number):
        if shop_number not in self.sales:
            self.sales[shop_number] = {'Shop Location': str(shop_number), 'Sales Count': 0}
        
        self.sales[shop_number]['Sales Count'] += 1

    def show_shop_sales(self):
        shop_sales = [str(shop_data.get('Sales Count', 0)) for shop_data in self.sales.values()]
        if shop_sales:
            return shop_sales
        else:
            return ["0"]

    def load_sales(self):
        try:
            with open(self.sales_file, 'r') as f:
                self.sales = json.load(f)
        except FileNotFoundError:
            self.sales = {}

    def save_sales(self):
        if self.sales:
            with open(self.sales_file, 'w') as f:
                json.dump(self.sales, f)
                
#-------------------------Sales Count SAVING END-------------------------