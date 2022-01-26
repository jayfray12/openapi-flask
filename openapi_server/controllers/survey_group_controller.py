import connexion
import six

from openapi_server.models.employee_assignment_with_employee import EmployeeAssignmentWithEmployee  # noqa: E501
from openapi_server.models.generic_error import GenericError  # noqa: E501
from openapi_server.models.survey_group import SurveyGroup  # noqa: E501
from openapi_server.models.survey_group_entity import SurveyGroupEntity  # noqa: E501
from openapi_server.models.survey_submission import SurveySubmission  # noqa: E501
from openapi_server import util


def add_default_skill(survey_group_id, request_body):  # noqa: E501
    """Add a default skill to a survey group.

    When a default skill is added to a survey group all survey submissions created for the survey group will include the default skill.  # noqa: E501

    :param survey_group_id: ID of the survey group as a GUID.
    :type survey_group_id: str
    :type survey_group_id: str
    :param request_body: An array of skillIds contained in the request body.
    :type request_body: List[str]

    :rtype: None
    """
    return 'do some magic!'


def assign_employee_to_survey_group(survey_group_id, employee_id, employee_assignment):  # noqa: E501
    """Assign an employee under their GUID to a survey group

    Assign an employee under their GUID to a survey group # noqa: E501

    :param survey_group_id: 
    :type survey_group_id: str
    :type survey_group_id: str
    :param employee_id: 
    :type employee_id: str
    :param employee_assignment: 
    :type employee_assignment: dict | bytes

    :rtype: EmployeeAssignment
    """

    return 'do some magic!'


def create_survey_group(survey_group):  # noqa: E501
    """Create a new survey group in the Feedback 360 Survey API.

    A survey group is the starting point for creating a Feedback 360 Survey. A survey group contains the project information, list of employees on the project that will receive the survey, and a list of technologies used on the project.  # noqa: E501

    :param survey_group: A new survey group resource contained in the request body.
    :type survey_group: dict | bytes

    :rtype: SurveyGroup
    """
    if connexion.request.is_json:
        survey_group = SurveyGroup.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_default_skill(survey_group_id, default_skill_id):  # noqa: E501
    """Delete default skills for a Survey Group.

    This operation will delete the given default skill from the survey group.  # noqa: E501

    :param survey_group_id: ID of the survey group as a GUID.
    :type survey_group_id: str
    :type survey_group_id: str
    :param default_skill_id: ID of the Default Skill as a GUID.
    :type default_skill_id: str
    :type default_skill_id: str

    :rtype: None
    """
    return 'do some magic!'


def delete_survey_group_by_id(survey_group_id):  # noqa: E501
    """Disable a survey group from Feedback 360 Survey API.

    This operation will delete an entire survey group and all child resources  associated with it. This operation is idempotent.  # noqa: E501

    :param survey_group_id: ID of the survey group as a GUID.
    :type survey_group_id: str
    :type survey_group_id: str

    :rtype: None
    """
    return 'do some magic!'


def get_all_survey_groups():  # noqa: E501
    """Get all survey groups from Feedback 360 Survey API.

    Get all survey groups in Feedback 360 Survey API.  # noqa: E501


    :rtype: List[SurveyGroup]
    """
    return 'do some magic!'


def get_employees_by_survey_group(survey_group_id):  # noqa: E501
    """Get list of assigned employees for a given survey group

    This request will return an array of Employee objects which are associated with a particular survey group. # noqa: E501

    :param survey_group_id: 
    :type survey_group_id: str
    :type survey_group_id: str

    :rtype: List[EmployeeAssignmentWithEmployee]
    """
    return 'do some magic!'


def get_survey_group_by_id(survey_group_id):  # noqa: E501
    """Find a survey group resource by ID

    Returns a single survey group matching the given ID. # noqa: E501

    :param survey_group_id: ID of the survey group as a GUID.
    :type survey_group_id: str
    :type survey_group_id: str

    :rtype: SurveyGroup
    """
    return 'do some magic!'


def get_survey_group_submissions(survey_group_id):  # noqa: E501
    """Find all submissions associated to a survey group.

    A submission contains all the ratings for the skills for a colleague receiving feedback. This operation will return all submissions submitted for a survey group. An empty resource collection is a valid response and indicates no feedback has been submitted.  # noqa: E501

    :param survey_group_id: ID of the survey group as a GUID.
    :type survey_group_id: str
    :type survey_group_id: str

    :rtype: List[SurveySubmission]
    """
    return 'do some magic!'


def remove_employee_assignment(survey_group_id, employee_id):  # noqa: E501
    """Remove an employee association with a survey group

    Remove an employee association with a survey group # noqa: E501

    :param survey_group_id: 
    :type survey_group_id: str
    :type survey_group_id: str
    :param employee_id: 
    :type employee_id: str

    :rtype: None
    """
    return 'do some magic!'


def update_default_skills(survey_group_id, request_body=None):  # noqa: E501
    """Update the default skills for a survey group. 

    When a default skill is added to a survey group all survey submissions created for the survey group will include the default skill.  # noqa: E501

    :param survey_group_id: ID of the survey group as a GUID.
    :type survey_group_id: str
    :type survey_group_id: str
    :param request_body: 
    :type request_body: List[str]

    :rtype: SurveyGroupEntity
    """
    return 'do some magic!'


def update_employee_assignment(survey_group_id, employee_id, employee_assignment):  # noqa: E501
    """Allows for updating start/end date and perhaps role for an existing assignment

    Allows for updating start/end date and perhaps role f # noqa: E501

    :param survey_group_id: 
    :type survey_group_id: str
    :type survey_group_id: str
    :param employee_id: 
    :type employee_id: str
    :param employee_assignment: 
    :type employee_assignment: dict | bytes

    :rtype: EmployeeAssignment
    """

    return 'do some magic!'


def update_survey_group_by_id(survey_group_id, survey_group=None):  # noqa: E501
    """Update a Survey Group in Feedback 360 Survey API. 

    This representation of the survey group contained in this request will replace  the survey group located at this URI. This operation is idempotent.  # noqa: E501

    :param survey_group_id: ID of the survey group as a GUID.
    :type survey_group_id: str
    :type survey_group_id: str
    :param survey_group: 
    :type survey_group: dict | bytes

    :rtype: SurveyGroup
    """
    if connexion.request.is_json:
        survey_group = SurveyGroup.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
