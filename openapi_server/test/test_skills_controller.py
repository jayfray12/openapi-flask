# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.skill import Skill  # noqa: E501
from openapi_server.test import BaseTestCase


class TestSkillsController(BaseTestCase):
    """SkillsController integration test stubs"""

    def test_get_all_skills(self):
        """Test case for get_all_skills

        Fetch all the skills available to be added on a survey submission.
        """
        query_string = [('filterBy', 'skill'),
                        ('filterString', 'Openshift'),
                        ('sortBy', 'sort_by_example'),
                        ('sortOrder', 'sort_order_example'),
                        ('offset', 56),
                        ('maxResults', 20)]
        headers = { 
        }
        response = self.client.open(
            '/skills',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
