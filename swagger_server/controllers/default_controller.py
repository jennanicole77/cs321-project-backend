import connexion
import six
import requests
import base64
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

gpuToUpdate = ""

def get_eth_price(price=None): 
    currPrice = Price(float(User.efficient_get_eth(newUser)))
    return currPrice

def get_profitability(profitability=None): 
    currProfitability = Profitability(float(User.efficient_get_mhs(newUser)))
    return currProfitability

def get_user(user=None):  
    global gpuToUpdate
    gpuToUpdate = ""
    global newUser
    all_gpus = dict()
    load_gpus(all_gpus)
    newUser = User(all_gpus)
    User.user_constructor(newUser, 0, 0, dict(), 0, 0)
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

def get_save(object=None):  
    gpus = [] 
    gpus_dict = User.get_user_gpu(newUser)  
    for keys in gpus_dict:
        currName = gpus_dict[keys].name
        currHash = gpus_dict[keys].hash
        currPower = gpus_dict[keys].power
        currQuantity = gpus_dict[keys].quantity
        currGpuList = ["name: ", currName, "hash: ", currHash, 
            "power: ", currPower, "quantity: ", currQuantity]
        gpus.append(currGpuList)

    response = {
        "ethereum" : User.get_ethereum_mined(newUser),
        "power_rate" : User.get_power_rate(newUser),
        "tax_rate" : User.get_tax_rate(newUser),
        "total_cost" : User.get_total_cost(newUser)  ,
        "user_gpu" : gpus
    }
    return json.dumps(response)

def put_load(load=input):
    User.load(newUser, base64.b64decode(load))
    return json.dumps(User.get_ethereum_mined(newUser))

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

def put_gpu_update(name=input):
    global gpuToUpdate
    gpuToUpdate = name
    return json.dumps(gpuToUpdate)

def put_add_gpu(quantity=input):
    User.add_gpus(newUser, gpuToUpdate, quantity)
    gpus = []
    user_gpus = User.get_user_gpu(newUser)
    for keys in user_gpus:
        currName = user_gpus[keys].name
        currHash = user_gpus[keys].hash
        currPower = user_gpus[keys].power
        currQuantity = user_gpus[keys].quantity
        currGpuList = ["name: ", currName, "hash: ", currHash, 
            "power: ", currPower, "quantity: ", currQuantity]
        gpus.append(currGpuList)
    return json.dumps(gpus)

def put_remove_gpu(quantity=input):
    User.remove_gpus(newUser, gpuToUpdate, quantity)
    gpus = []
    user_gpus = User.get_user_gpu(newUser)
    for keys in user_gpus:
        currName = user_gpus[keys].name
        currHash = user_gpus[keys].hash
        currPower = user_gpus[keys].power
        currQuantity = user_gpus[keys].quantity
        currGpuList = ["name: ", currName, "hash: ", currHash, 
            "power: ", currPower, "quantity: ", currQuantity]
        gpus.append(currGpuList)
    return json.dumps(gpus)

