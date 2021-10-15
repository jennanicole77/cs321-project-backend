import connexion
import six
import requests
from swagger_server.models.gpu import GPU  # noqa: E501
from swagger_server.models.price import Price  # noqa: E501
from swagger_server.models.profitability import Profitability  # noqa: E501
from swagger_server.scrapers.ethereum import grab_eth_price, grab_profitability
from swagger_server import util


def get_eth_price(price=None):  # noqa: E501
    """Your GET endpoint

     # noqa: E501

    :param price: current Ethereum price
    :type price: float

    :rtype: Price
    """
    
    currPrice = Price(float(grab_eth_price()))
    return currPrice

def get_profitability(profitability=None):  # noqa: E501
    """Your GET endpoint

     # noqa: E501

    :param profitability: profitability
    :type profitability: float

    :rtype: Profitability
    """
    currProfitability = Profitability(float(grab_profitability()))
    return currProfitability
