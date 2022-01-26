import connexion
import six

from openapi_server.models.employee_aggregate_skill_ratings import EmployeeAggregateSkillRatings  # noqa: E501
from openapi_server.models.employee_skill_history import EmployeeSkillHistory  # noqa: E501
from openapi_server import util


def get_employee_aggregate_skill_ratings(employee_id):  # noqa: E501
    """Find a list ggregate Skill Ratings for each skill that the employee has be rated on 3 or more times.

    Return a Map&lt;skill,rating&gt; of all the the skills that the employee has been rated on 3 or more times. # noqa: E501

    :param employee_id: Kerberos ID of the employee.
    :type employee_id: str

    :rtype: List[EmployeeAggregateSkillRatings]
    """
    return 'do some magic!'


def get_employee_skills_history(employee_id):  # noqa: E501
    """Find a list of all the project and corresponding skills associated with an employee.

    Return a Map&lt;project,skills&gt; of all the projects an employee is part of and a list of skills that the employee used at each project. # noqa: E501

    :param employee_id: Kerberos ID of the employee.
    :type employee_id: str

    :rtype: List[EmployeeSkillHistory]
    """
    return 'do some magic!'
