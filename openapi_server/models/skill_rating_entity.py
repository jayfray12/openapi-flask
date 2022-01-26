# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.skill import Skill
from openapi_server.models.skill_rating import SkillRating
from openapi_server import util

from openapi_server.models.skill import Skill  # noqa: E501
from openapi_server.models.skill_rating import SkillRating  # noqa: E501

class SkillRatingEntity(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, skill=None, rating=None):  # noqa: E501
        """SkillRatingEntity - a model defined in OpenAPI

        :param id: The id of this SkillRatingEntity.  # noqa: E501
        :type id: str
        :param skill: The skill of this SkillRatingEntity.  # noqa: E501
        :type skill: Skill
        :param rating: The rating of this SkillRatingEntity.  # noqa: E501
        :type rating: int
        """
        self.openapi_types = {
            'id': str,
            'skill': Skill,
            'rating': int
        }

        self.attribute_map = {
            'id': 'id',
            'skill': 'skill',
            'rating': 'rating'
        }

        self._id = id
        self._skill = skill
        self._rating = rating

    @classmethod
    def from_dict(cls, dikt) -> 'SkillRatingEntity':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SkillRatingEntity of this SkillRatingEntity.  # noqa: E501
        :rtype: SkillRatingEntity
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this SkillRatingEntity.

        A GUID that uniquely identifies a skill rathing.  # noqa: E501

        :return: The id of this SkillRatingEntity.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SkillRatingEntity.

        A GUID that uniquely identifies a skill rathing.  # noqa: E501

        :param id: The id of this SkillRatingEntity.
        :type id: str
        """

        self._id = id

    @property
    def skill(self):
        """Gets the skill of this SkillRatingEntity.

        A GUID that uniquely identifies a skill.  # noqa: E501

        :return: The skill of this SkillRatingEntity.
        :rtype: Skill
        """
        return self._skill

    @skill.setter
    def skill(self, skill):
        """Sets the skill of this SkillRatingEntity.

        A GUID that uniquely identifies a skill.  # noqa: E501

        :param skill: The skill of this SkillRatingEntity.
        :type skill: Skill
        """

        self._skill = skill

    @property
    def rating(self):
        """Gets the rating of this SkillRatingEntity.

        The rating -1 -> 4 of the skill. -1 - 'Not Applicable', 0 - No Experience, 1 - Foundational, 2 - Experienced, 3 - Advanced, 4 - Expert  # noqa: E501

        :return: The rating of this SkillRatingEntity.
        :rtype: int
        """
        return self._rating

    @rating.setter
    def rating(self, rating):
        """Sets the rating of this SkillRatingEntity.

        The rating -1 -> 4 of the skill. -1 - 'Not Applicable', 0 - No Experience, 1 - Foundational, 2 - Experienced, 3 - Advanced, 4 - Expert  # noqa: E501

        :param rating: The rating of this SkillRatingEntity.
        :type rating: int
        """
        if rating is not None and rating > 4:  # noqa: E501
            raise ValueError("Invalid value for `rating`, must be a value less than or equal to `4`")  # noqa: E501
        if rating is not None and rating < -1:  # noqa: E501
            raise ValueError("Invalid value for `rating`, must be a value greater than or equal to `-1`")  # noqa: E501

        self._rating = rating