# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.current_user import CurrentUser  # noqa: E501
from swagger_server.models.price import Price  # noqa: E501
from swagger_server.models.profitability import Profitability  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_get_days(self):
        """Test case for get_days

        Your GET endpoint
        """
        response = self.client.open(
            '/days',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_eth_price(self):
        """Test case for get_eth_price

        Your GET endpoint
        """
        query_string = [('price', 1.2)]
        response = self.client.open(
            '/eth-price',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_hashrate(self):
        """Test case for get_hashrate

        Your GET endpoint
        """
        response = self.client.open(
            '/hashrate',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_mine(self):
        """Test case for get_mine

        Your GET endpoint
        """
        response = self.client.open(
            '/mine',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_profit(self):
        """Test case for get_profit

        Your GET endpoint
        """
        response = self.client.open(
            '/profit',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_profitability(self):
        """Test case for get_profitability

        Your GET endpoint
        """
        query_string = [('profitability', 1.2)]
        response = self.client.open(
            '/profitability',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_save(self):
        """Test case for get_save

        Your GET endpoint
        """
        query_string = [('object', 'object_example')]
        response = self.client.open(
            '/save',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_revenue(self):
        """Test case for get_revenue

        Your GET endpoint
        """
        response = self.client.open(
            '/revenue',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user(self):
        """Test case for get_user

        Your GET endpoint
        """
        query_string = [('user', 'user_example')]
        response = self.client.open(
            '/user',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_add_gpu(self):
        """Test case for put_add_gpu

        
        """
        query_string = [('quantity', 1.2)]
        response = self.client.open(
            '/add-gpu',
            method='PUT',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_amount_mined(self):
        """Test case for put_amount_mined

        
        """
        query_string = [('mined', 1.2)]
        response = self.client.open(
            '/amount-mined',
            method='PUT',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_gpu_update(self):
        """Test case for put_gpu_update

        
        """
        query_string = [('name', 'name_example')]
        response = self.client.open(
            '/gpu-update',
            method='PUT',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_power(self):
        """Test case for put_power

        
        """
        query_string = [('power', 1.2)]
        response = self.client.open(
            '/power',
            method='PUT',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_remove_gpu(self):
        """Test case for put_remove_gpu

        
        """
        query_string = [('quantity', 1.2)]
        response = self.client.open(
            '/remove-gpu',
            method='PUT',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_rig(self):
        """Test case for put_rig

        
        """
        query_string = [('rig', 1.2)]
        response = self.client.open(
            '/rig',
            method='PUT',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_tax(self):
        """Test case for put_tax

        
        """
        query_string = [('tax', 1.2)]
        response = self.client.open(
            '/tax',
            method='PUT',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
