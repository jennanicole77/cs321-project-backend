# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.price import Price  # noqa: E501
from swagger_server.models.profitability import Profitability  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

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


if __name__ == '__main__':
    import unittest
    unittest.main()
