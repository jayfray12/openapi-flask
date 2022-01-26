# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.employee_assignment import EmployeeAssignment  # noqa: E501
from openapi_server.models.employee_assignment_with_employee import EmployeeAssignmentWithEmployee  # noqa: E501
from openapi_server.models.generic_error import GenericError  # noqa: E501
from openapi_server.models.survey_group import SurveyGroup  # noqa: E501
from openapi_server.models.survey_group_entity import SurveyGroupEntity  # noqa: E501
from openapi_server.models.survey_submission import SurveySubmission  # noqa: E501
from openapi_server.test import BaseTestCase


class TestSurveyGroupController(BaseTestCase):
    """SurveyGroupController integration test stubs"""

    def test_add_default_skill(self):
        """Test case for add_default_skill

        Add a default skill to a survey group.
        """
        request_body = ['request_body_example']
        headers = { 
        }
        response = self.client.open(
            '/surveygroups/{survey_group_id}/defaultSkill'.format(survey_group_id='f9238beb-9649-4983-9059-4f0ee372d56e'),
            method='POST',
            headers=headers,
            data=json.dumps(request_body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


    def test_create_survey_group(self):
        """Test case for create_survey_group

        Create a new survey group in the Feedback 360 Survey API.
        """
        survey_group = {
  "tsmId" : "timmytsm@redhat.com",
  "opportunityId" : "3456NAS",
  "createdDate" : "2000-01-23T04:56:07.000+00:00",
  "defaultSkills" : [ {
    "skillsBaseId" : 1234,
    "skill" : "Crucial Conversations",
    "description" : "The ability to have crucial conversations with clients.",
    "active" : true,
    "id" : "d567521f-13a6-4237-936c-40bbbf388bc5",
    "category" : "leadership"
  }, {
    "skillsBaseId" : 1234,
    "skill" : "Crucial Conversations",
    "description" : "The ability to have crucial conversations with clients.",
    "active" : true,
    "id" : "d567521f-13a6-4237-936c-40bbbf388bc5",
    "category" : "leadership"
  } ],
  "createdBy" : "janedoe",
  "modifiedDate" : "2000-01-23T04:56:07.000+00:00",
  "modifiedBy" : "janedoe",
  "id" : "f1ad7649-eb70-4499-9c82-a63fe2c6dc71",
  "projectName" : "NASA App Modernization",
  "projectCreatorId" : "janedoe@redhat.com"
}
        headers = { 
        }
        response = self.client.open(
            '/surveygroups',
            method='POST',
            headers=headers,
            data=json.dumps(survey_group),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_default_skill(self):
        """Test case for delete_default_skill

        Delete default skills for a Survey Group.
        """
        headers = { 
        }
        response = self.client.open(
            '/surveygroups/{survey_group_id}/defaultSkill/{default_skill_id}'.format(survey_group_id='f9238beb-9649-4983-9059-4f0ee372d56e', default_skill_id='f9238bea-9649-4983-9059-4f0ee372d56e'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_survey_group_by_id(self):
        """Test case for delete_survey_group_by_id

        Disable a survey group from Feedback 360 Survey API.
        """
        headers = { 
        }
        response = self.client.open(
            '/surveygroups/{survey_group_id}'.format(survey_group_id='f9238beb-9649-4983-9059-4f0ee372d56e'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_survey_groups(self):
        """Test case for get_all_survey_groups

        Get all survey groups from Feedback 360 Survey API.
        """
        headers = { 
        }
        response = self.client.open(
            '/surveygroups',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_employees_by_survey_group(self):
        """Test case for get_employees_by_survey_group

        Get list of assigned employees for a given survey group
        """
        headers = { 
        }
        response = self.client.open(
            '/surveygroups/{survey_group_id}/assignment'.format(survey_group_id='survey_group_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_survey_group_by_id(self):
        """Test case for get_survey_group_by_id

        Find a survey group resource by ID
        """
        headers = { 
        }
        response = self.client.open(
            '/surveygroups/{survey_group_id}'.format(survey_group_id='\"08bb3e66-8562-11ea-9325-b78f2fb687bf\"'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_survey_group_submissions(self):
        """Test case for get_survey_group_submissions

        Find all submissions associated to a survey group.
        """
        headers = { 
        }
        response = self.client.open(
            '/surveygroups/{survey_group_id}/submissions'.format(survey_group_id='f9238beb-9649-4983-9059-4f0ee372d56e'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_remove_employee_assignment(self):
        """Test case for remove_employee_assignment

        Remove an employee association with a survey group
        """
        headers = { 
        }
        response = self.client.open(
            '/surveygroups/{survey_group_id}/assignment/{employee_id}'.format(survey_group_id='\"1bea1106-8562-11ea-aee6-7721eaea325b\"', employee_id='\"1bea1106-8562-11ea-aee6-7721eaea325b\"'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_default_skills(self):
        """Test case for update_default_skills

        Update the default skills for a survey group. 
        """
        request_body = ['request_body_example']
        headers = { 
        }
        response = self.client.open(
            '/surveygroups/{survey_group_id}/defaultSkill'.format(survey_group_id='f9238beb-9649-4983-9059-4f0ee372d56e'),
            method='PUT',
            headers=headers,
            data=json.dumps(request_body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_employee_assignment(self):
        """Test case for update_employee_assignment

        Allows for updating start/end date and perhaps role for an existing assignment
        """
        employee_assignment = {
  "endDate" : "2000-01-23T04:56:07.000+00:00",
  "billableRole" : "Consultant",
  "id" : "f9238beb-9649-4983-9059-4f0ee372d56e",
  "surveyGroup" : "{}",
  "employee" : "{}",
  "startDate" : "2000-01-23T04:56:07.000+00:00"
}
        headers = { 
        }
        response = self.client.open(
            '/surveygroups/{survey_group_id}/assignment/{employee_id}'.format(survey_group_id='\"1bea1106-8562-11ea-aee6-7721eaea325b\"', employee_id='ajones'),
            method='PUT',
            headers=headers,
            data=json.dumps(employee_assignment),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_survey_group_by_id(self):
        """Test case for update_survey_group_by_id

        Update a Survey Group in Feedback 360 Survey API. 
        """
        survey_group = {
  "tsmId" : "timmytsm@redhat.com",
  "opportunityId" : "3456NAS",
  "createdDate" : "2000-01-23T04:56:07.000+00:00",
  "defaultSkills" : [ {
    "skillsBaseId" : 1234,
    "skill" : "Crucial Conversations",
    "description" : "The ability to have crucial conversations with clients.",
    "active" : true,
    "id" : "d567521f-13a6-4237-936c-40bbbf388bc5",
    "category" : "leadership"
  }, {
    "skillsBaseId" : 1234,
    "skill" : "Crucial Conversations",
    "description" : "The ability to have crucial conversations with clients.",
    "active" : true,
    "id" : "d567521f-13a6-4237-936c-40bbbf388bc5",
    "category" : "leadership"
  } ],
  "createdBy" : "janedoe",
  "modifiedDate" : "2000-01-23T04:56:07.000+00:00",
  "modifiedBy" : "janedoe",
  "id" : "f1ad7649-eb70-4499-9c82-a63fe2c6dc71",
  "projectName" : "NASA App Modernization",
  "projectCreatorId" : "janedoe@redhat.com"
}
        headers = { 
        }
        response = self.client.open(
            '/surveygroups/{survey_group_id}'.format(survey_group_id='f9238beb-9649-4983-9059-4f0ee372d56e'),
            method='PUT',
            headers=headers,
            data=json.dumps(survey_group),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
