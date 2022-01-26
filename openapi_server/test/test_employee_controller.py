# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.employee import Employee  # noqa: E501
from openapi_server.models.employee_assignment_with_survey_group import EmployeeAssignmentWithSurveyGroup  # noqa: E501
from openapi_server.test import BaseTestCase


class TestEmployeeController(BaseTestCase):
    """EmployeeController integration test stubs"""

    def test_get_employee_by_id(self):
        """Test case for get_employee_by_id

        Find an Employee resource by ID
        """
        headers = { 
        }
        response = self.client.open(
            '/employee/{employee_id}'.format(employee_id='ajones'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_employees(self):
        """Test case for get_employees

        List all employees available in the Feedback 360 Survey API.
        """
        query_string = [('filterBy', 'name'),
                        ('filter', 'Frank'),
                        ('sortBy', 'sort_by_example'),
                        ('sortOrder', 'sort_order_example'),
                        ('offset', 56),
                        ('maxResults', 20)]
        headers = { 
        }
        response = self.client.open(
            '/employee',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_survey_group_by_employee_id(self):
        """Test case for get_survey_group_by_employee_id

        Find an all Survey Groups an employee is part of resource by ID
        """
        headers = { 
        }
        response = self.client.open(
            '/employee/{employee_id}/surveyGroups'.format(employee_id='ajones'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_employee_by_id(self):
        """Test case for update_employee_by_id

        Update an Employee resource by ID 
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
            '/employee/{employee_id}'.format(employee_id='ajones'),
            method='PUT',
            headers=headers,
            data=json.dumps(employee),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
