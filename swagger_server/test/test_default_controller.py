# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.gpu import GPU  # noqa: E501
from swagger_server.models.price import Price  # noqa: E501
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

    def test_get_gpu(self):
        """Test case for get_gpu

        Get available GPUs
        """
        query_string = [('make', 'make_example'),
                        ('model', 'model_example'),
                        ('hash', 'hash_example'),
                        ('power', 'power_example')]
        response = self.client.open(
            '/gpu',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_gpu(self):
        """Test case for post_gpu

        Add new GPU
        """
        body = GPU()
        response = self.client.open(
            '/gpu',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
