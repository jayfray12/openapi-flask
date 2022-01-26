# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from sqlalchemy import Column, String, Boolean, Float
from openapi_server import util
from __main__ import db


class EmployeeModel(db.Model):
    __tablename__ = 'employees'

    id = Column('id', String, primary_key=True)
    name = Column(String)
    email = Column(String)
    role = Column(String)
    date_terms_accepted = Column(Boolean)
    terms_version_number = Column(Float)

    openapi_types = {
            'id': str,
            'name': str,
            'email': str,
            'role': str,
            'date_terms_accepted': date,
            'terms_version_number': float
        }
    attribute_map = {
            'id': 'id',
            'name': 'name',
            'email': 'email',
            'role': 'role',
            'date_terms_accepted': 'dateTermsAccepted',
            'terms_version_number': 'termsVersionNumber'
        }

    @classmethod
    def from_dict(cls, dikt) -> 'EmployeeModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Employee of this Employee.  # noqa: E501
        :rtype: Employee
        """
        return util.deserialize_model(dikt, cls)


