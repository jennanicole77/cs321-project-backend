from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import warnings
import datetime
import time
import json
import math

warnings.filterwarnings("ignore", category=DeprecationWarning) 

# Selenium Driver is different for the OS you are using, choose one of the following
#PATH = "dependencies/windowschromedriver"
PATH = "dependencies/m1chromedriver"
# PATH = "dependencies/macchromedriver"
# PATH = "dependencies/linuxchromedriver"

# A class that defines the attributes of a GPU
class GPU:
    def __init__(self, name, hash, power):
        self.name = name
        self.hash = hash
        self.power = power
        self.quantity = 0
    def __str__(self):
        return "name: {0}, hash: {1}, power: {2}, quantity: {3}".format(self.name, self.hash, self.power, self.quantity)

# Class that stores the User's parameters
class User:
    def __init__(self, All_Gpu_Dict):
        self.ethereum = 0           #Stores the total amount of ethereum the user has
        self.power_rate = 0         #Stores the power rate of the user in ppw
        self.user_gpu = dict()      #Stores a map that contains all the GPUS the user has
        self.tax_rate = 0           #Stores the percent rate of tax_ratees ex: 0.25
        self.total_cost = 0         #Stores the money spent with the RIG
        self.eth_price = 0
        self.cash_per_100 = 0
        self.total_hashrate = 0
        self.All_Gpu_Dict = All_Gpu_Dict
        
    def __str__(self):
        return "amount of ethereum: {0}, price per wattage: {1}, total hashrate: {2}, tax_rate: {3}, total_cost: {4}".format(self.ethereum, self.power_rate, self.get_total_hashrate(), self.tax_rate, self.total_cost)
    
    # A constructor used to initialize an user at once when all values are given. 
    def user_constructor(self, ethereum, power_rate, user_gpu, tax_rate, total_cost):
        self.ethereum = ethereum
        self.power_rate = power_rate
        self.user_gpu = user_gpu
        self.tax_rate = tax_rate
        self.total_cost = total_cost

    # Sets the total ammount of ethereum mined, default is 0
    def set_ethereum_mined(self, ethereum):
        self.ethereum = float(ethereum)
    
    # Gets the total amount of ethereum mined
    def get_ethereum_mined(self):
        return self.ethereum

    def get_all_gpu_dict(self):
        return self.All_Gpu_Dict
    
    # Sets the total  cost of the system, default is 0
    def set_total_cost(self, total_cost):
        self.total_cost = float(total_cost)
    
    # Gets the total cost of the system
    def get_total_cost(self):
        return self.total_cost
    
     # Sets the total  cost of the system, default is 0
    
    # Sets the tax rate
    def set_tax_rate(self, tax_rate):
        self.tax_rate = float(tax_rate)
    
    # Gets the total cost of the system
    def get_tax_rate(self):
        return self.tax_rate
    
     # Sets the total  cost of the system, default is 0
    def get_user_gpu(self):
        return self.user_gpu
    # Sets the power rate
    def set_power_rate(self, power_rate):
        self.power_rate = float(power_rate)
    
    # Gets the total cost of the system
    def get_power_rate(self):
        return self.power_rate
    
    # Grabs the price of eth without wasting selenium calls if value already exists
    def efficient_get_eth(self):
        if self.eth_price == 0:
            self.eth_price = self.grab_eth_price()
            time.sleep(3)
        return self.eth_price

    def efficient_get_mhs(self):
        if self.cash_per_100 == 0:
            self.cash_per_100 = self.grab_profitability()
        return self.cash_per_100

    # Returns the value needed to be mined in dollars.
    def need_to_mine(self):
        time.sleep(3)
        tot = self.get_total_cost()
        eth = self.get_ethereum_mined() * (1 - self.tax_rate)
        ret =  tot - eth
        if ret < 0:
            ret = 0
        return ret


    # Loops through the gpus stored in the user_gpu map adding upthe hashrates of all GPUs
    # Returns the total hash rate of the user's GPUs
    def get_total_hashrate(self):
        return self.total_hashrate

    # Loops through the gpus stored in the user_gpu map adding up the power consumption of the Gpus
    # Returns the total cost of power consumption in a 24 hour period
    def  power_usage(self):
        power_usage = 0
        total_gpu_power = 0
        for keys in self.user_gpu:
            total_gpu_power += float(self.user_gpu[keys].power) * float(self.user_gpu[keys].quantity)
        power_usage = (total_gpu_power/1000) * self.power_rate * 24
        return power_usage

    # Returns expected daily revenue before power costs
    # (total_hashrate/100) * (profitabiity per 100Mhs of eth)
    def daily_revenue(self):
        daily_revenue = (self.get_total_hashrate()/100) * self.efficient_get_mhs()
        return daily_revenue

    # Returns the daily profit adjusted for power and tax_ratees
    def daily_profit(self):
        tax_rate = self.daily_revenue() * self.tax_rate
        daily_profit = self.daily_revenue() -  self.power_usage() - tax_rate
        return daily_profit

    # Saves session's data into a json file
    def save(self):
        gpus = dict()
        for keys in self.user_gpu:
            gpus[keys] = {"name" : self.user_gpu[keys].name, "quantity" : self.user_gpu[keys].quantity}

        data = {"ethereum" : self.ethereum, "power_rate" : self.power_rate, "tax_rate" : self.tax_rate, "total_cost" : self.total_cost, "user gpus" : gpus}

        with open("sessions\saved_session.json", "w") as f:
            json.dump(data, f)
        return data
    
    # Loads a saved user session
    def load(self, file):
        data = json.loads(file)

        all_gpus = dict()
        self.user_gpu = dict()
        load_gpus(all_gpus)

        for i in range(len(data["user_gpu"])):
            self.add_gpus(data["user_gpu"][i][1], data["user_gpu"][i][7])

        
        self.user_constructor(data["ethereum"], data["power_rate"], self.user_gpu, data["tax_rate"], data["total_cost"])
    
    # This function adds a gpu to the user dictionary
    def add_gpus(self, name, quantity):
        
        if quantity > 0:
            self.user_gpu[self.All_Gpu_Dict[name].name] = self.All_Gpu_Dict[name]
            self.user_gpu[name].quantity = self.user_gpu[name].quantity + quantity
            self.total_hashrate = self.total_hashrate + (float(self.user_gpu[name].hash) * quantity)

    # This function removes a gpu from the user dictionary
    def remove_gpus(self, name, quantity):
        
        if name in self.user_gpu.keys():
            self.user_gpu[name].quantity = self.user_gpu[name].quantity - quantity
            self.total_hashrate = self.total_hashrate - (float(self.user_gpu[name].hash) * quantity)
            if self.user_gpu[name].quantity <= 0:
                self.user_gpu[name].quantity = 0
                self.user_gpu.pop(name)
            if self.total_hashrate <= 0:
                self.total_hashrate = 0
                

    # Calculates the return on total_cost
    def calculate_remaining_days_for_ROI(self):

        daily_profit = self.daily_profit()
        if daily_profit == 0:
            return "???"
        ROI = self.need_to_mine()/daily_profit
        day = math.ceil(ROI)
    

        start_date = datetime.datetime.now()
        start_date_string = start_date.strftime("%m/%d/%y")
        date_1 = datetime.datetime.strptime(start_date_string, "%m/%d/%y")
        end_date = date_1 + datetime.timedelta(days=day)


        return str(day) + " days on " + end_date.strftime("%B %d, %Y")

        # This function uses selenium to grab the profitablility per 100Mhs of ethereum
    
    #Uses Selenium to grab profitability per 100 Mhs
    def grab_profitability(self):

        # Url where profitability will be pulled from
        hiveon_url = "https://hiveon.net/"

        #Forces selenium to run on headless mode
        op = webdriver.ChromeOptions()
        op.add_argument('headless')

        # Loads up the webdriver and page
        driver = webdriver.Chrome(PATH, options=op)
        #driver = webdriver.Chrome(PATH)
        driver.get(hiveon_url)
        


        #Finds the required value on the website and pulls the information 
        location = "/html/body/div[1]/div[1]/div/section[3]/div/div/div[1]/div[2]"
        try:
            main = WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element((By.XPATH, location), ".")
        )
        finally:
            price_string = driver.find_element_by_xpath(location).text
            driver.quit()
        
        # Parses the return string

        price_string = price_string.replace('$', ' ')
        split_string = price_string.split()

        float_price = float(split_string[0])

        return float_price

    # This function grabs the Price of a single ETH Coin
    def grab_eth_price(self):
        # Url where profitability will be pulled from
        url = "https://www.google.com/search?q=Ethereum+Price&oq=Ethereum+Price&aqs=chrome..69i57j69i60.1759j0j4&sourceid=chrome&ie=UTF-8"

        

        #Forces selenium to run on headless mode
        op = webdriver.ChromeOptions()
        op.add_argument('headless')

        # Loads up the webdriver and page
        driver = webdriver.Chrome(PATH, options=op)
        driver.get(url)
        
        #Finds the required value on the website and pulls the information 
        location = "/html/body/div[7]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div[1]/div/div[1]/div[1]/div[2]/span[1]"
        #ocation = "[data-precision]"
        price_string = driver.find_element_by_xpath(location).text
        price_string = price_string.replace(',', '')  
        
        float_price = float(price_string)

        return float_price

    
# Loads up the GPU name, hashrate and power consumption into a dictionary
def load_gpus(all_gpus):

    f = open("data/gpuhashrate.dat", "r")
    for lines in f:
        temp_list = lines.split()
        all_gpus[temp_list[0]] = (GPU(temp_list[0], temp_list[1], temp_list[2]))

    f.close()







# Page Loads 
# GPUs are loaded into all_gpu dict

all_gpus = dict() #A Global variable that stores all the possible GPU Types inside a map
load_gpus(all_gpus)

# A new user instance is created

#caio = User(all_gpus)


#caio.set_ethereum_mined(1000)
#caio.set_total_cost(5000)
#caio.set_tax_rate(0.1)
#caio.set_power_rate(0.12)

# #print(caio)

#caio.add_gpus("3070Ti", 4)
#caio.add_gpus("3070Ti", 2) #This will give exacly 100Mh/s good for testing
#caio.remove_gpus("3070Ti", 4)
#caio.add_gpus("3080Ti", 5)
# print(caio)


#print(f"\n\nYou currently own {caio.get_ethereum_mined()}")
#print(f"Your total system price was {caio.get_total_cost()}$")
#print(f"You need to mine: {caio.need_to_mine()}$ to reach ROI")
#print(f"Your current hashrate is {caio.get_total_hashrate()} Mh/s") 
#print(f"Revenue per day is estimated at {caio.daily_revenue()}$")
#print(f"Profit per day is estimated at {caio.daily_profit()}$")  
#print(f"At current prices, your rig will be payed in {caio.calculate_remaining_days_for_ROI()} days on TODO\n\n")  

#this is how to display after adding gpus
#for keys in caio.user_gpu:
#    print(caio.user_gpu[keys])

#gpus = []
#user_gpus = caio.user_gpu
#for keys in user_gpus:
#    currName = user_gpus[keys].name
#    currHash = user_gpus[keys].hash
#    currPower = user_gpus[keys].power
#    currQuantity = user_gpus[keys].quantity
#    currGpuList = ["name: ", currName, "hash: ", currHash, 
#        "power: ", currPower, "quantity: ", currQuantity]
#    gpus.append(currGpuList)
#for gpu in gpus:
#    print(gpu)





# print(grab_profitability())
# print(grab_eth_price())

# user_gpu = dict()


# remove_gpus(user_gpu, all_gpus, "3080")
# remove_gpus(user_gpu, all_gpus, "1080")


# user = load("saved_session.json")

# print("Power usage: " + str(user.power_usage()))

# print("Daily revenue: " + str(user.daily_revenue()))

# print("Daily earnings: " + str(user.daily_profit()))

# print("ROI: " + str(user.calculateROI()))

# print(user)

# user.save()
