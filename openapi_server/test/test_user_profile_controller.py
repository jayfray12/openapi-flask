# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.employee import Employee  # noqa: E501
from openapi_server.test import BaseTestCase


class TestUserProfileController(BaseTestCase):
    """UserProfileController integration test stubs"""

    def test_get_user_profile(self):
        """Test case for get_user_profile

        
        """
        headers = { 
        }
        response = self.client.open(
            '/userprofile',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_user_profile(self):
        """Test case for update_user_profile

        Update the user profile resource 
        """
        employee = {
  "role" : "Consultant",
  "dateTermsAccepted" : "2021-02-09T00:00:00.000+0000",
  "name" : "John Smith",
  "termsVersionNumber" : 1.0,
  "id" : "jsmith@redhat.com",
  "hasAcceptedTerms" : false,
  "email" : "jsmith@redhat.com"
}
        headers = { 
        }
        response = self.client.open(
            '/userprofile',
            method='PUT',
            headers=headers,
            data=json.dumps(employee),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
