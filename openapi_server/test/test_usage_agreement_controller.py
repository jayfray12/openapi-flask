# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.usage_agreement import UsageAgreement  # noqa: E501
from openapi_server.test import BaseTestCase


class TestUsageAgreementController(BaseTestCase):
    """UsageAgreementController integration test stubs"""

    def test_get_usage_agreement(self):
        """Test case for get_usage_agreement

        
        """
        headers = { 
        }
        response = self.client.open(
            '/usageagreement',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
