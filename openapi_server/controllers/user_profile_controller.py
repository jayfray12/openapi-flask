import connexion
import six

from openapi_server.models.employee import Employee  # noqa: E501
from openapi_server import util


def get_user_profile():  # noqa: E501
    """get_user_profile

    For the currently authenticated user, return the user profile information # noqa: E501


    :rtype: Employee
    """
    return 'do some magic!'


def update_user_profile(employee=None):  # noqa: E501
    """Update the user profile resource 

    The representation of the user profile contained in this request will replace the user profile. This operation is idempotent.  # noqa: E501

    :param employee: 
    :type employee: dict | bytes

    :rtype: Employee
    """
    if connexion.request.is_json:
        employee = Employee.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
