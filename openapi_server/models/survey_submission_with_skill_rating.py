# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.employee import Employee
from openapi_server.models.skill_rating import SkillRating
from openapi_server.models.survey_group import SurveyGroup
from openapi_server.models.survey_submission import SurveySubmission
from openapi_server import util

from openapi_server.models.employee import Employee  # noqa: E501
from openapi_server.models.skill_rating import SkillRating  # noqa: E501
from openapi_server.models.survey_group import SurveyGroup  # noqa: E501
from openapi_server.models.survey_submission import SurveySubmission  # noqa: E501

class SurveySubmissionWithSkillRating(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, survey_group=None, ratings=None, id=None, survey_author=None, survey_subject=None, submission_date=None, submission_status=None, feedback=None):  # noqa: E501
        """SurveySubmissionWithSkillRating - a model defined in OpenAPI

        :param survey_group: The survey_group of this SurveySubmissionWithSkillRating.  # noqa: E501
        :type survey_group: SurveyGroup
        :param ratings: The ratings of this SurveySubmissionWithSkillRating.  # noqa: E501
        :type ratings: List[SkillRating]
        :param id: The id of this SurveySubmissionWithSkillRating.  # noqa: E501
        :type id: str
        :param survey_author: The survey_author of this SurveySubmissionWithSkillRating.  # noqa: E501
        :type survey_author: Employee
        :param survey_subject: The survey_subject of this SurveySubmissionWithSkillRating.  # noqa: E501
        :type survey_subject: EmployeeAssignment
        :param submission_date: The submission_date of this SurveySubmissionWithSkillRating.  # noqa: E501
        :type submission_date: datetime
        :param submission_status: The submission_status of this SurveySubmissionWithSkillRating.  # noqa: E501
        :type submission_status: str
        :param feedback: The feedback of this SurveySubmissionWithSkillRating.  # noqa: E501
        :type feedback: str
        """
        self.openapi_types = {
            'survey_group': SurveyGroup,
            'ratings': List[SkillRating],
            'id': str,
            'survey_author': Employee,
            'submission_date': datetime,
            'submission_status': str,
            'feedback': str
        }

        self.attribute_map = {
            'survey_group': 'surveyGroup',
            'ratings': 'ratings',
            'id': 'id',
            'survey_author': 'surveyAuthor',
            'survey_subject': 'surveySubject',
            'submission_date': 'submissionDate',
            'submission_status': 'submissionStatus',
            'feedback': 'feedback'
        }

        self._survey_group = survey_group
        self._ratings = ratings
        self._id = id
        self._survey_author = survey_author
        self._survey_subject = survey_subject
        self._submission_date = submission_date
        self._submission_status = submission_status
        self._feedback = feedback

    @classmethod
    def from_dict(cls, dikt) -> 'SurveySubmissionWithSkillRating':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SurveySubmissionWithSkillRating of this SurveySubmissionWithSkillRating.  # noqa: E501
        :rtype: SurveySubmissionWithSkillRating
        """
        return util.deserialize_model(dikt, cls)

    @property
    def survey_group(self):
        """Gets the survey_group of this SurveySubmissionWithSkillRating.

        A GUID that uniquely identifies the project.  # noqa: E501

        :return: The survey_group of this SurveySubmissionWithSkillRating.
        :rtype: SurveyGroup
        """
        return self._survey_group

    @survey_group.setter
    def survey_group(self, survey_group):
        """Sets the survey_group of this SurveySubmissionWithSkillRating.

        A GUID that uniquely identifies the project.  # noqa: E501

        :param survey_group: The survey_group of this SurveySubmissionWithSkillRating.
        :type survey_group: SurveyGroup
        """

        self._survey_group = survey_group

    @property
    def ratings(self):
        """Gets the ratings of this SurveySubmissionWithSkillRating.

        SkillRatings for the subject employee  # noqa: E501

        :return: The ratings of this SurveySubmissionWithSkillRating.
        :rtype: List[SkillRating]
        """
        return self._ratings

    @ratings.setter
    def ratings(self, ratings):
        """Sets the ratings of this SurveySubmissionWithSkillRating.

        SkillRatings for the subject employee  # noqa: E501

        :param ratings: The ratings of this SurveySubmissionWithSkillRating.
        :type ratings: List[SkillRating]
        """

        self._ratings = ratings

    @property
    def id(self):
        """Gets the id of this SurveySubmissionWithSkillRating.

        A GUID that uniquely identifies a survey submitted for a project.  # noqa: E501

        :return: The id of this SurveySubmissionWithSkillRating.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SurveySubmissionWithSkillRating.

        A GUID that uniquely identifies a survey submitted for a project.  # noqa: E501

        :param id: The id of this SurveySubmissionWithSkillRating.
        :type id: str
        """

        self._id = id

    @property
    def survey_author(self):
        """Gets the survey_author of this SurveySubmissionWithSkillRating.

        Employee that is reviewing.  # noqa: E501

        :return: The survey_author of this SurveySubmissionWithSkillRating.
        :rtype: Employee
        """
        return self._survey_author

    @survey_author.setter
    def survey_author(self, survey_author):
        """Sets the survey_author of this SurveySubmissionWithSkillRating.

        Employee that is reviewing.  # noqa: E501

        :param survey_author: The survey_author of this SurveySubmissionWithSkillRating.
        :type survey_author: Employee
        """

        self._survey_author = survey_author

    @property
    def survey_subject(self):
        """Gets the survey_subject of this SurveySubmissionWithSkillRating.

        Employee that is being reviewed.  # noqa: E501

        :return: The survey_subject of this SurveySubmissionWithSkillRating.
        :rtype: EmployeeAssignment
        """
        return self._survey_subject

    @survey_subject.setter
    def survey_subject(self, survey_subject):
        """Sets the survey_subject of this SurveySubmissionWithSkillRating.

        Employee that is being reviewed.  # noqa: E501

        :param survey_subject: The survey_subject of this SurveySubmissionWithSkillRating.
        :type survey_subject: EmployeeAssignment
        """

        self._survey_subject = survey_subject

    @property
    def submission_date(self):
        """Gets the submission_date of this SurveySubmissionWithSkillRating.

        The date the survey was submitted to the Feedback 360 Survey API in UTC.  # noqa: E501

        :return: The submission_date of this SurveySubmissionWithSkillRating.
        :rtype: datetime
        """
        return self._submission_date

    @submission_date.setter
    def submission_date(self, submission_date):
        """Sets the submission_date of this SurveySubmissionWithSkillRating.

        The date the survey was submitted to the Feedback 360 Survey API in UTC.  # noqa: E501

        :param submission_date: The submission_date of this SurveySubmissionWithSkillRating.
        :type submission_date: datetime
        """

        self._submission_date = submission_date

    @property
    def submission_status(self):
        """Gets the submission_status of this SurveySubmissionWithSkillRating.

        Returns a status of \"Complete\" or \"Incomplete\"  # noqa: E501

        :return: The submission_status of this SurveySubmissionWithSkillRating.
        :rtype: str
        """
        return self._submission_status

    @submission_status.setter
    def submission_status(self, submission_status):
        """Sets the submission_status of this SurveySubmissionWithSkillRating.

        Returns a status of \"Complete\" or \"Incomplete\"  # noqa: E501

        :param submission_status: The submission_status of this SurveySubmissionWithSkillRating.
        :type submission_status: str
        """
        allowed_values = ["Complete", "Incomplete"]  # noqa: E501
        if submission_status not in allowed_values:
            raise ValueError(
                "Invalid value for `submission_status` ({0}), must be one of {1}"
                .format(submission_status, allowed_values)
            )

        self._submission_status = submission_status

    @property
    def feedback(self):
        """Gets the feedback of this SurveySubmissionWithSkillRating.

        Any feedback the author of the survey would like to include in the rating.  # noqa: E501

        :return: The feedback of this SurveySubmissionWithSkillRating.
        :rtype: str
        """
        return self._feedback

    @feedback.setter
    def feedback(self, feedback):
        """Sets the feedback of this SurveySubmissionWithSkillRating.

        Any feedback the author of the survey would like to include in the rating.  # noqa: E501

        :param feedback: The feedback of this SurveySubmissionWithSkillRating.
        :type feedback: str
        """

        self._feedback = feedback
