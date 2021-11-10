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

def get_days():  # noqa: E501
    """Your GET endpoint

     # noqa: E501


    :rtype: Object
    """
    return 'do some magic!'

def get_hashrate():  # noqa: E501
    """Your GET endpoint

     # noqa: E501


    :rtype: Object
    """
    return 'do some magic!'

def get_mine():  
    return json.dumps(newUser.need_to_mine())

def get_profit():  # noqa: E501
    """Your GET endpoint

     # noqa: E501


    :rtype: Object
    """
    return 'do some magic!'

def get_revenue():  # noqa: E501
    """Your GET endpoint

     # noqa: E501


    :rtype: Object
    """
    return 'do some magic!'

def put_amount_mined(mined=input):  
    newUser.set_ethereum_mined(mined)
    return json.dumps(newUser.get_ethereum_mined())

def put_power(power=input): 
    newUser.set_power_rate(power)
    return json.dumps(newUser.get_power_rate())

def put_rig(rig=input): 
    newUser.set_total_cost(rig)
    return json.dumps(newUser.get_total_cost())

def put_tax(tax=input): 
    newUser.set_tax_rate(tax)
    return json.dumps(newUser.get_tax_rate())

