import connexion
import six

from openapi_server.models.employee import Employee  # noqa: E501
from openapi_server.models.survey_submission import SurveySubmission  # noqa: E501
from openapi_server.models.survey_submission_entity import SurveySubmissionEntity  # noqa: E501
from openapi_server.models.survey_submission_with_skill_rating import SurveySubmissionWithSkillRating  # noqa: E501
from openapi_server import util


def create_survey_submissions(survey_group_id):  # noqa: E501
    """Create a batch of SurveySubmissions for a survey group in the Feedback 360 Survey API.

    Returns a List of Employees in which surveys where created. # noqa: E501

    :param survey_group_id: ID of the survey group as a GUID.
    :type survey_group_id: str
    :type survey_group_id: str

    :rtype: List[Employee]
    """
    return 'do some magic!'


def disable_survey_submission(survey_submission_id):  # noqa: E501
    """Disable a surveySubmission from Feedback 360 Survey API.

    This operation will disable a survey submission and all child resources  associated with it. This operation is idempotent.  # noqa: E501

    :param survey_submission_id: ID of the survey submission as a GUID.
    :type survey_submission_id: str
    :type survey_submission_id: str

    :rtype: None
    """
    return 'do some magic!'


def get_reviewed_by_by_employee_id(employee_id):  # noqa: E501
    """Fetch the survey submissions reviewed by the given employee Id.

    Returns all survey submissions that have been reviewed by the employee ID. # noqa: E501

    :param employee_id: Employee&#39;s RedHat Kerberos ID.
    :type employee_id: str

    :rtype: List[SurveySubmission]
    """
    return 'do some magic!'


def get_reviewed_on_by_employee_id(employee_id):  # noqa: E501
    """Fetch the survey submissions that the given employee Id was reviewed on.

    Returns all survey submissions that the employee has been reviewed on. # noqa: E501

    :param employee_id: Employee&#39;s RedHat Kerberos ID.
    :type employee_id: str

    :rtype: List[SurveySubmission]
    """
    return 'do some magic!'


def get_survey_submission_by_id(survey_submission_id):  # noqa: E501
    """Fetch the survey submission associated with the survey submission resource ID

    Returns a survey submission matching the submission ID. # noqa: E501

    :param survey_submission_id: ID of the surveyGroup as a GUID.
    :type survey_submission_id: str
    :type survey_submission_id: str

    :rtype: SurveySubmissionWithSkillRating
    """
    return 'do some magic!'


def get_survey_submissions_by_survey_group_id(survey_group_id):  # noqa: E501
    """Fetch the survey submissions associated with the Survey Group.

    Returns all survey submissions that are part of the SurveyGroup. # noqa: E501

    :param survey_group_id: ID of the surveyGroup as a GUID.
    :type survey_group_id: str
    :type survey_group_id: str

    :rtype: List[SurveySubmission]
    """
    return 'do some magic!'


def update_survey_submission_by_id(survey_submission_id, survey_submission_with_skill_rating=None):  # noqa: E501
    """Update a survey Submission in Feedback 360 Survey API. 

    This representation of the survey submission contained in this request will replace  the survey submission located at this URI. This operation is idempotent. TODO  # noqa: E501

    :param survey_submission_id: ID of the employee assignment as a GUID.
    :type survey_submission_id: str
    :type survey_submission_id: str
    :param survey_submission_with_skill_rating: 
    :type survey_submission_with_skill_rating: dict | bytes

    :rtype: SurveySubmissionEntity
    """
    if connexion.request.is_json:
        survey_submission_with_skill_rating = SurveySubmissionWithSkillRating.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
