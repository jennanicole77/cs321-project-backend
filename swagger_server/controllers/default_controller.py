import connexion
import six
import requests
import logging
import json
from swagger_server.models.price import Price 
from swagger_server.models.profitability import Profitability  
from swagger_server.models.current_user import CurrentUser
from swagger_server.ethereum_calculator.ethereum import User, load_gpus
from swagger_server import util

all_gpus = dict()
load_gpus(all_gpus)
newUser = User(all_gpus)

def get_eth_price(price=None): 
    currPrice = Price(float(User.grab_eth_price(newUser)))
    return currPrice

def get_profitability(profitability=None): 
    currProfitability = Profitability(float(User.grab_profitability(newUser)))
    return currProfitability

def get_user(user=None):  
    gpus = []   
    for gpu in newUser.All_Gpu_Dict:
        gpus.append(gpu)

    response = {
        "ethereum" : newUser.ethereum,
        "power_rate" : newUser.power_rate,
        "user_gpu" : newUser.user_gpu,
        "tax_rate" : newUser.tax_rate,
        "total_cost" : newUser.total_cost  ,
        "All_Gpu_Dict" : gpus
    }
    return  json.dumps(response)

def get_days(): 
    return json.dumps(User.calculate_remaining_days_for_ROI(newUser))

def get_hashrate(): 
    return json.dumps(User.get_total_hashrate(newUser))

def get_mine():  
    return json.dumps(User.need_to_mine(newUser))

def get_profit(): 
    return json.dumps(User.daily_profit(newUser))

def get_revenue():
    return json.dumps(User.daily_revenue(newUser))

def put_amount_mined(mined=input):  
    User.set_ethereum_mined(newUser, mined)
    return json.dumps(User.get_ethereum_mined(newUser))

def put_power(power=input): 
    User.set_power_rate(newUser, power)
    return json.dumps(User.get_power_rate(newUser))

def put_rig(rig=input): 
    User.set_total_cost(newUser, rig)
    return json.dumps(User.get_total_cost(newUser))

def put_tax(tax=input): 
    User.set_tax_rate(newUser, tax)
    return json.dumps(User.get_tax_rate(newUser))

def put_add_gpu(gpu_name=input, gpu_quantity=input):
    User.add_gpus(newUser, gpu_name, gpu_quantity)

