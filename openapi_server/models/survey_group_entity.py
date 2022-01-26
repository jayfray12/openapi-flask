# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.skill import Skill
from openapi_server.models.survey_group import SurveyGroup
from openapi_server import util

from openapi_server.models.skill import Skill  # noqa: E501
from openapi_server.models.survey_group import SurveyGroup  # noqa: E501

class SurveyGroupEntity(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, assignments=None, disabled=False, id=None, created_date=None, created_by=None, modified_date=None, modified_by=None, opportunity_id=None, project_name=None, project_creator_id=None, tsm_id=None, default_skills=None):  # noqa: E501
        """SurveyGroupEntity - a model defined in OpenAPI

        :param assignments: The assignments of this SurveyGroupEntity.  # noqa: E501
        :type assignments: List[EmployeeAssignment]
        :param disabled: The disabled of this SurveyGroupEntity.  # noqa: E501
        :type disabled: bool
        :param id: The id of this SurveyGroupEntity.  # noqa: E501
        :type id: str
        :param created_date: The created_date of this SurveyGroupEntity.  # noqa: E501
        :type created_date: datetime
        :param created_by: The created_by of this SurveyGroupEntity.  # noqa: E501
        :type created_by: str
        :param modified_date: The modified_date of this SurveyGroupEntity.  # noqa: E501
        :type modified_date: datetime
        :param modified_by: The modified_by of this SurveyGroupEntity.  # noqa: E501
        :type modified_by: str
        :param opportunity_id: The opportunity_id of this SurveyGroupEntity.  # noqa: E501
        :type opportunity_id: str
        :param project_name: The project_name of this SurveyGroupEntity.  # noqa: E501
        :type project_name: str
        :param project_creator_id: The project_creator_id of this SurveyGroupEntity.  # noqa: E501
        :type project_creator_id: str
        :param tsm_id: The tsm_id of this SurveyGroupEntity.  # noqa: E501
        :type tsm_id: str
        :param default_skills: The default_skills of this SurveyGroupEntity.  # noqa: E501
        :type default_skills: List[Skill]
        """
        self.openapi_types = {
            'disabled': bool,
            'id': str,
            'created_date': datetime,
            'created_by': str,
            'modified_date': datetime,
            'modified_by': str,
            'opportunity_id': str,
            'project_name': str,
            'project_creator_id': str,
            'tsm_id': str,
            'default_skills': List[Skill]
        }

        self.attribute_map = {
            'assignments': 'assignments',
            'disabled': 'disabled',
            'id': 'id',
            'created_date': 'createdDate',
            'created_by': 'createdBy',
            'modified_date': 'modifiedDate',
            'modified_by': 'modifiedBy',
            'opportunity_id': 'opportunityId',
            'project_name': 'projectName',
            'project_creator_id': 'projectCreatorId',
            'tsm_id': 'tsmId',
            'default_skills': 'defaultSkills'
        }

        self._assignments = assignments
        self._disabled = disabled
        self._id = id
        self._created_date = created_date
        self._created_by = created_by
        self._modified_date = modified_date
        self._modified_by = modified_by
        self._opportunity_id = opportunity_id
        self._project_name = project_name
        self._project_creator_id = project_creator_id
        self._tsm_id = tsm_id
        self._default_skills = default_skills

    @classmethod
    def from_dict(cls, dikt) -> 'SurveyGroupEntity':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SurveyGroupEntity of this SurveyGroupEntity.  # noqa: E501
        :rtype: SurveyGroupEntity
        """
        return util.deserialize_model(dikt, cls)

    @property
    def assignments(self):
        """Gets the assignments of this SurveyGroupEntity.


        :return: The assignments of this SurveyGroupEntity.
        :rtype: List[EmployeeAssignment]
        """
        return self._assignments

    @assignments.setter
    def assignments(self, assignments):
        """Sets the assignments of this SurveyGroupEntity.


        :param assignments: The assignments of this SurveyGroupEntity.
        :type assignments: List[EmployeeAssignment]
        """

        self._assignments = assignments

    @property
    def disabled(self):
        """Gets the disabled of this SurveyGroupEntity.

        A flag indicating if this Survey Group is disabled  # noqa: E501

        :return: The disabled of this SurveyGroupEntity.
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this SurveyGroupEntity.

        A flag indicating if this Survey Group is disabled  # noqa: E501

        :param disabled: The disabled of this SurveyGroupEntity.
        :type disabled: bool
        """

        self._disabled = disabled

    @property
    def id(self):
        """Gets the id of this SurveyGroupEntity.

        A GUID that uniquely identifies the SurveyGroup.  # noqa: E501

        :return: The id of this SurveyGroupEntity.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SurveyGroupEntity.

        A GUID that uniquely identifies the SurveyGroup.  # noqa: E501

        :param id: The id of this SurveyGroupEntity.
        :type id: str
        """

        self._id = id

    @property
    def created_date(self):
        """Gets the created_date of this SurveyGroupEntity.

        The date the project was created in the Feedback 360 Survey API in UTC.  # noqa: E501

        :return: The created_date of this SurveyGroupEntity.
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this SurveyGroupEntity.

        The date the project was created in the Feedback 360 Survey API in UTC.  # noqa: E501

        :param created_date: The created_date of this SurveyGroupEntity.
        :type created_date: datetime
        """

        self._created_date = created_date

    @property
    def created_by(self):
        """Gets the created_by of this SurveyGroupEntity.

        The employee id (Kerberos) of the user that created the project.  # noqa: E501

        :return: The created_by of this SurveyGroupEntity.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this SurveyGroupEntity.

        The employee id (Kerberos) of the user that created the project.  # noqa: E501

        :param created_by: The created_by of this SurveyGroupEntity.
        :type created_by: str
        """

        self._created_by = created_by

    @property
    def modified_date(self):
        """Gets the modified_date of this SurveyGroupEntity.

        The date the project was last modified in the Feedback 360 Survey API in UTC.  # noqa: E501

        :return: The modified_date of this SurveyGroupEntity.
        :rtype: datetime
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        """Sets the modified_date of this SurveyGroupEntity.

        The date the project was last modified in the Feedback 360 Survey API in UTC.  # noqa: E501

        :param modified_date: The modified_date of this SurveyGroupEntity.
        :type modified_date: datetime
        """

        self._modified_date = modified_date

    @property
    def modified_by(self):
        """Gets the modified_by of this SurveyGroupEntity.

        The employee id (Kerberos) of the user that last modifed the project.  # noqa: E501

        :return: The modified_by of this SurveyGroupEntity.
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this SurveyGroupEntity.

        The employee id (Kerberos) of the user that last modifed the project.  # noqa: E501

        :param modified_by: The modified_by of this SurveyGroupEntity.
        :type modified_by: str
        """

        self._modified_by = modified_by

    @property
    def opportunity_id(self):
        """Gets the opportunity_id of this SurveyGroupEntity.

        The ID of the Opportunity from PSA.  # noqa: E501

        :return: The opportunity_id of this SurveyGroupEntity.
        :rtype: str
        """
        return self._opportunity_id

    @opportunity_id.setter
    def opportunity_id(self, opportunity_id):
        """Sets the opportunity_id of this SurveyGroupEntity.

        The ID of the Opportunity from PSA.  # noqa: E501

        :param opportunity_id: The opportunity_id of this SurveyGroupEntity.
        :type opportunity_id: str
        """
        if opportunity_id is None:
            raise ValueError("Invalid value for `opportunity_id`, must not be `None`")  # noqa: E501

        self._opportunity_id = opportunity_id

    @property
    def project_name(self):
        """Gets the project_name of this SurveyGroupEntity.

        The name of the project.  # noqa: E501

        :return: The project_name of this SurveyGroupEntity.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this SurveyGroupEntity.

        The name of the project.  # noqa: E501

        :param project_name: The project_name of this SurveyGroupEntity.
        :type project_name: str
        """
        if project_name is None:
            raise ValueError("Invalid value for `project_name`, must not be `None`")  # noqa: E501

        self._project_name = project_name

    @property
    def project_creator_id(self):
        """Gets the project_creator_id of this SurveyGroupEntity.

        The email address of the creator of the project.  # noqa: E501

        :return: The project_creator_id of this SurveyGroupEntity.
        :rtype: str
        """
        return self._project_creator_id

    @project_creator_id.setter
    def project_creator_id(self, project_creator_id):
        """Sets the project_creator_id of this SurveyGroupEntity.

        The email address of the creator of the project.  # noqa: E501

        :param project_creator_id: The project_creator_id of this SurveyGroupEntity.
        :type project_creator_id: str
        """
        if project_creator_id is None:
            raise ValueError("Invalid value for `project_creator_id`, must not be `None`")  # noqa: E501

        self._project_creator_id = project_creator_id

    @property
    def tsm_id(self):
        """Gets the tsm_id of this SurveyGroupEntity.

        The email address of the TSM in charge of the project.  # noqa: E501

        :return: The tsm_id of this SurveyGroupEntity.
        :rtype: str
        """
        return self._tsm_id

    @tsm_id.setter
    def tsm_id(self, tsm_id):
        """Sets the tsm_id of this SurveyGroupEntity.

        The email address of the TSM in charge of the project.  # noqa: E501

        :param tsm_id: The tsm_id of this SurveyGroupEntity.
        :type tsm_id: str
        """
        if tsm_id is None:
            raise ValueError("Invalid value for `tsm_id`, must not be `None`")  # noqa: E501

        self._tsm_id = tsm_id

    @property
    def default_skills(self):
        """Gets the default_skills of this SurveyGroupEntity.


        :return: The default_skills of this SurveyGroupEntity.
        :rtype: List[Skill]
        """
        return self._default_skills

    @default_skills.setter
    def default_skills(self, default_skills):
        """Sets the default_skills of this SurveyGroupEntity.


        :param default_skills: The default_skills of this SurveyGroupEntity.
        :type default_skills: List[Skill]
        """

        self._default_skills = default_skills
