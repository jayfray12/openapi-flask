# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class EmployeeAssignmentWithEmployee(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, employee_id=None, name=None, email=None, start_date=None, end_date=None, billable_role=None, employee_role=None):  # noqa: E501
        """EmployeeAssignmentWithEmployee - a model defined in OpenAPI

        :param id: The id of this EmployeeAssignmentWithEmployee.  # noqa: E501
        :type id: str
        :param employee_id: The employee_id of this EmployeeAssignmentWithEmployee.  # noqa: E501
        :type employee_id: str
        :param name: The name of this EmployeeAssignmentWithEmployee.  # noqa: E501
        :type name: str
        :param email: The email of this EmployeeAssignmentWithEmployee.  # noqa: E501
        :type email: str
        :param start_date: The start_date of this EmployeeAssignmentWithEmployee.  # noqa: E501
        :type start_date: datetime
        :param end_date: The end_date of this EmployeeAssignmentWithEmployee.  # noqa: E501
        :type end_date: datetime
        :param billable_role: The billable_role of this EmployeeAssignmentWithEmployee.  # noqa: E501
        :type billable_role: str
        :param employee_role: The employee_role of this EmployeeAssignmentWithEmployee.  # noqa: E501
        :type employee_role: str
        """
        self.openapi_types = {
            'id': str,
            'employee_id': str,
            'name': str,
            'email': str,
            'start_date': datetime,
            'end_date': datetime,
            'billable_role': str,
            'employee_role': str
        }

        self.attribute_map = {
            'id': 'id',
            'employee_id': 'employeeId',
            'name': 'name',
            'email': 'email',
            'start_date': 'startDate',
            'end_date': 'endDate',
            'billable_role': 'billableRole',
            'employee_role': 'employeeRole'
        }

        self._id = id
        self._employee_id = employee_id
        self._name = name
        self._email = email
        self._start_date = start_date
        self._end_date = end_date
        self._billable_role = billable_role
        self._employee_role = employee_role

    @classmethod
    def from_dict(cls, dikt) -> 'EmployeeAssignmentWithEmployee':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EmployeeAssignmentWithEmployee of this EmployeeAssignmentWithEmployee.  # noqa: E501
        :rtype: EmployeeAssignmentWithEmployee
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this EmployeeAssignmentWithEmployee.

        The Employee Assignment ID as a GUUID  # noqa: E501

        :return: The id of this EmployeeAssignmentWithEmployee.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EmployeeAssignmentWithEmployee.

        The Employee Assignment ID as a GUUID  # noqa: E501

        :param id: The id of this EmployeeAssignmentWithEmployee.
        :type id: str
        """

        self._id = id

    @property
    def employee_id(self):
        """Gets the employee_id of this EmployeeAssignmentWithEmployee.

        The Employee Kerboros ID  # noqa: E501

        :return: The employee_id of this EmployeeAssignmentWithEmployee.
        :rtype: str
        """
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        """Sets the employee_id of this EmployeeAssignmentWithEmployee.

        The Employee Kerboros ID  # noqa: E501

        :param employee_id: The employee_id of this EmployeeAssignmentWithEmployee.
        :type employee_id: str
        """

        self._employee_id = employee_id

    @property
    def name(self):
        """Gets the name of this EmployeeAssignmentWithEmployee.

        Name of the employee.  # noqa: E501

        :return: The name of this EmployeeAssignmentWithEmployee.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EmployeeAssignmentWithEmployee.

        Name of the employee.  # noqa: E501

        :param name: The name of this EmployeeAssignmentWithEmployee.
        :type name: str
        """

        self._name = name

    @property
    def email(self):
        """Gets the email of this EmployeeAssignmentWithEmployee.

        The email address of the employee.  # noqa: E501

        :return: The email of this EmployeeAssignmentWithEmployee.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this EmployeeAssignmentWithEmployee.

        The email address of the employee.  # noqa: E501

        :param email: The email of this EmployeeAssignmentWithEmployee.
        :type email: str
        """

        self._email = email

    @property
    def start_date(self):
        """Gets the start_date of this EmployeeAssignmentWithEmployee.

        The start date of this employee's assignment  # noqa: E501

        :return: The start_date of this EmployeeAssignmentWithEmployee.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this EmployeeAssignmentWithEmployee.

        The start date of this employee's assignment  # noqa: E501

        :param start_date: The start_date of this EmployeeAssignmentWithEmployee.
        :type start_date: datetime
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this EmployeeAssignmentWithEmployee.

        The end date of this employee's assignment  # noqa: E501

        :return: The end_date of this EmployeeAssignmentWithEmployee.
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this EmployeeAssignmentWithEmployee.

        The end date of this employee's assignment  # noqa: E501

        :param end_date: The end_date of this EmployeeAssignmentWithEmployee.
        :type end_date: datetime
        """

        self._end_date = end_date

    @property
    def billable_role(self):
        """Gets the billable_role of this EmployeeAssignmentWithEmployee.

        Role that the employee is billed for on the project.  # noqa: E501

        :return: The billable_role of this EmployeeAssignmentWithEmployee.
        :rtype: str
        """
        return self._billable_role

    @billable_role.setter
    def billable_role(self, billable_role):
        """Sets the billable_role of this EmployeeAssignmentWithEmployee.

        Role that the employee is billed for on the project.  # noqa: E501

        :param billable_role: The billable_role of this EmployeeAssignmentWithEmployee.
        :type billable_role: str
        """

        self._billable_role = billable_role

    @property
    def employee_role(self):
        """Gets the employee_role of this EmployeeAssignmentWithEmployee.

        Employee's Red Hat Role.  # noqa: E501

        :return: The employee_role of this EmployeeAssignmentWithEmployee.
        :rtype: str
        """
        return self._employee_role

    @employee_role.setter
    def employee_role(self, employee_role):
        """Sets the employee_role of this EmployeeAssignmentWithEmployee.

        Employee's Red Hat Role.  # noqa: E501

        :param employee_role: The employee_role of this EmployeeAssignmentWithEmployee.
        :type employee_role: str
        """

        self._employee_role = employee_role