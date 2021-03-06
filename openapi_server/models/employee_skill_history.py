# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class EmployeeSkillHistory(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, project=None, skills=None):  # noqa: E501
        """EmployeeSkillHistory - a model defined in OpenAPI

        :param project: The project of this EmployeeSkillHistory.  # noqa: E501
        :type project: str
        :param skills: The skills of this EmployeeSkillHistory.  # noqa: E501
        :type skills: List[str]
        """
        self.openapi_types = {
            'project': str,
            'skills': List[str]
        }

        self.attribute_map = {
            'project': 'project',
            'skills': 'skills'
        }

        self._project = project
        self._skills = skills

    @classmethod
    def from_dict(cls, dikt) -> 'EmployeeSkillHistory':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EmployeeSkillHistory of this EmployeeSkillHistory.  # noqa: E501
        :rtype: EmployeeSkillHistory
        """
        return util.deserialize_model(dikt, cls)

    @property
    def project(self):
        """Gets the project of this EmployeeSkillHistory.

        Name of project that consultant was part of  # noqa: E501

        :return: The project of this EmployeeSkillHistory.
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this EmployeeSkillHistory.

        Name of project that consultant was part of  # noqa: E501

        :param project: The project of this EmployeeSkillHistory.
        :type project: str
        """

        self._project = project

    @property
    def skills(self):
        """Gets the skills of this EmployeeSkillHistory.

        Array of skills that the consultant used at the project  # noqa: E501

        :return: The skills of this EmployeeSkillHistory.
        :rtype: List[str]
        """
        return self._skills

    @skills.setter
    def skills(self, skills):
        """Sets the skills of this EmployeeSkillHistory.

        Array of skills that the consultant used at the project  # noqa: E501

        :param skills: The skills of this EmployeeSkillHistory.
        :type skills: List[str]
        """

        self._skills = skills
