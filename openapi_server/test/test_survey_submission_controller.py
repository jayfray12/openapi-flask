# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.employee import Employee  # noqa: E501
from openapi_server.models.survey_submission import SurveySubmission  # noqa: E501
from openapi_server.models.survey_submission_entity import SurveySubmissionEntity  # noqa: E501
from openapi_server.models.survey_submission_with_skill_rating import SurveySubmissionWithSkillRating  # noqa: E501
from openapi_server.test import BaseTestCase


class TestSurveySubmissionController(BaseTestCase):
    """SurveySubmissionController integration test stubs"""

    def test_create_survey_submissions(self):
        """Test case for create_survey_submissions

        Create a batch of SurveySubmissions for a survey group in the Feedback 360 Survey API.
        """
        headers = { 
        }
        response = self.client.open(
            '/surveygroups/{survey_group_id}/createSurveySubmissions'.format(survey_group_id='f9238beb-9649-4983-9059-4f0ee372d56e'),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_disable_survey_submission(self):
        """Test case for disable_survey_submission

        Disable a surveySubmission from Feedback 360 Survey API.
        """
        headers = { 
        }
        response = self.client.open(
            '/surveySubmission/{survey_submission_id}'.format(survey_submission_id='f9238beb-9649-4983-9059-4f0ee372d56e'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_reviewed_by_by_employee_id(self):
        """Test case for get_reviewed_by_by_employee_id

        Fetch the survey submissions reviewed by the given employee Id.
        """
        headers = { 
        }
        response = self.client.open(
            '/surveySubmission/reviewedBy/{employee_id}'.format(employee_id='ajones'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_reviewed_on_by_employee_id(self):
        """Test case for get_reviewed_on_by_employee_id

        Fetch the survey submissions that the given employee Id was reviewed on.
        """
        headers = { 
        }
        response = self.client.open(
            '/surveySubmission/reviewedOn/{employee_id}'.format(employee_id='ajones'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_survey_submission_by_id(self):
        """Test case for get_survey_submission_by_id

        Fetch the survey submission associated with the survey submission resource ID
        """
        headers = { 
        }
        response = self.client.open(
            '/surveySubmission/{survey_submission_id}'.format(survey_submission_id='f9238beb-9649-4983-9059-4f0ee372d56e'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_survey_submissions_by_survey_group_id(self):
        """Test case for get_survey_submissions_by_survey_group_id

        Fetch the survey submissions associated with the Survey Group.
        """
        headers = { 
        }
        response = self.client.open(
            '/surveySubmission/surveyGroup/{survey_group_id}'.format(survey_group_id='f9238beb-9649-4983-9059-4f0ee372d56e'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_survey_submission_by_id(self):
        """Test case for update_survey_submission_by_id

        Update a survey Submission in Feedback 360 Survey API. 
        """
        survey_submission_with_skill_rating = {
  "ratings" : [ {
    "skill" : "{}",
    "rating" : 0,
    "id" : "f1ad7649-eb70-4499-9c82-a63fe2c6dc71"
  }, {
    "skill" : "{}",
    "rating" : 0,
    "id" : "f1ad7649-eb70-4499-9c82-a63fe2c6dc71"
  } ],
  "surveyGroup" : "{}"
}
        headers = { 
        }
        response = self.client.open(
            '/surveySubmission/{survey_submission_id}'.format(survey_submission_id='f9238beb-9649-4983-9059-4f0ee372d56e'),
            method='PUT',
            headers=headers,
            data=json.dumps(survey_submission_with_skill_rating),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
