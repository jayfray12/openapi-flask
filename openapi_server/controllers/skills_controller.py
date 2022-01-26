import connexion
import six

from openapi_server.models.skill import Skill  # noqa: E501
from openapi_server import util


def get_all_skills(filter_by=None, filter_string=None, sort_by=None, sort_order=None, offset=None, max_results=None):  # noqa: E501
    """Fetch all the skills available to be added on a survey submission.

    Returns all skills that are active in the Skills table. # noqa: E501

    :param filter_by: Field by which to filter
    :type filter_by: str
    :param filter_string: String to filter on, query string
    :type filter_string: str
    :param sort_by: Field by which to sort
    :type sort_by: str
    :param sort_order: Sort Order
    :type sort_order: str
    :param offset: Page offset
    :type offset: int
    :param max_results: Maximum number of results to return, defaults to 20
    :type max_results: int

    :rtype: List[Skill]
    """
    return 'do some magic!'
