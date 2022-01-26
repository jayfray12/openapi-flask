import connexion
import six

from openapi_server.models.employee import Employee  # noqa: E501
from openapi_server.models.employee_assignment_with_survey_group import EmployeeAssignmentWithSurveyGroup  # noqa: E501
from openapi_server import util

from openapi_server.models.employeemodel import EmployeeModel  # noqa: E501
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify


def get_employee_by_id(employee_id):  # noqa: E501
    """Find an Employee resource by ID

    Returns a single employee matching the given ID. # noqa: E501

    :param employee_id: Kerberos ID of the employee.
    :type employee_id: str

    :rtype: Employee
    """
    employee = EmployeeModel.query.filter_by(id = employee_id).first()
    if employee == None:
        return "Record not found for id", 404
        
    return employee


def get_employees(filter_by=None, filter=None, sort_by=None, sort_order=None, offset=None, max_results=None):  # noqa: E501
    """List all employees available in the Feedback 360 Survey API.

    This operation fetches a full list of employees available in the Feedback 360 Survey API.  The filtering and sorting mechanism for fetching this list is yet To Be Determined.  The Employees in the Feedback 360 Survey API data store will be populated from outside resources such as LDAP or Rover.  # noqa: E501

    :param filter_by: Field by which to filter results.
    :type filter_by: str
    :param filter: String to filter on, query string
    :type filter: str
    :param sort_by: Field by which to sort
    :type sort_by: str
    :param sort_order: Sort Order
    :type sort_order: str
    :param offset: Page offset
    :type offset: int
    :param max_results: Maximum number of results to return, defaults to 20
    :type max_results: int

    :rtype: List[Employee]
    """
    return EmployeeModel.query.all()


def get_survey_group_by_employee_id(employee_id):  # noqa: E501
    """Find an all Survey Groups an employee is part of resource by ID

    Returns a List of Survey Groups matching the given employee ID. # noqa: E501

    :param employee_id: Employee&#39;s RedHat Kerberos ID.
    :type employee_id: str

    :rtype: List[EmployeeAssignmentWithSurveyGroup]
    """
    return 'do some magic!'


def update_employee_by_id(employee_id, employee=None):  # noqa: E501
    """Update an Employee resource by ID 

    The representation of the employee contained in this request will replace the employee located at this URI. This operation is idempotent.  # noqa: E501

    :param employee_id: Kerberos ID of the employee.
    :type employee_id: str
    :param employee: 
    :type employee: dict | bytes

    :rtype: Employee
    """
    if connexion.request.is_json:
        employee = Employee.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
