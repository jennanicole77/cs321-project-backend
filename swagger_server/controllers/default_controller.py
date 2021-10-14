import connexion
import six
import requests
from swagger_server.models.gpu import GPU  # noqa: E501
from swagger_server.models.price import Price  # noqa: E501
from swagger_server.scrapers.ethereum import grab_eth_price
from swagger_server import util


def get_eth_price(price=None):  # noqa: E501
    """Your GET endpoint

     # noqa: E501

    :param price: current Ethereum price
    :type price: float

    :rtype: Price
    """
    
    response = requests.get("https://api.coincap.io/v2/rates/ethereum")
    rawPrice = response.json()['data']['rateUsd']
    priceResp = Price(float(rawPrice))
    return priceResp


def get_gpu(make=None, model=None, hash=None, power=None):  # noqa: E501
    """Get available GPUs

    Get list of matching GPUs based on query parameters # noqa: E501

    :param make: Make
    :type make: str
    :param model: Model
    :type model: str
    :param hash: Hash rate
    :type hash: str
    :param power: Power consumption
    :type power: str

    :rtype: List[GPU]
    """
    return 'do some magic!'


def post_gpu(body=None):  # noqa: E501
    """Add new GPU

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: GPU
    """
    if connexion.request.is_json:
        body = GPU.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
