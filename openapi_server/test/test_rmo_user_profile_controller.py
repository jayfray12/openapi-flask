# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.employee_aggregate_skill_ratings import EmployeeAggregateSkillRatings  # noqa: E501
from openapi_server.models.employee_skill_history import EmployeeSkillHistory  # noqa: E501
from openapi_server.test import BaseTestCase


class TestRMOUserProfileController(BaseTestCase):
    """RMOUserProfileController integration test stubs"""

    def test_get_employee_aggregate_skill_ratings(self):
        """Test case for get_employee_aggregate_skill_ratings

        Find a list ggregate Skill Ratings for each skill that the employee has be rated on 3 or more times.
        """
        headers = { 
        }
        response = self.client.open(
            '/rmo/profile/{employee_id}/aggregateRatings'.format(employee_id='ajones'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_employee_skills_history(self):
        """Test case for get_employee_skills_history

        Find a list of all the project and corresponding skills associated with an employee.
        """
        headers = { 
        }
        response = self.client.open(
            '/rmo/profile/{employee_id}/skills'.format(employee_id='ajones'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
