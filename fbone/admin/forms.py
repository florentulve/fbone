# -*- coding: utf-8 -*-

from flask.ext.wtf import Form
from flask.ext.wtf import HiddenField, SubmitField, RadioField, DateField
from flask.ext.wtf import AnyOf

from ..user import USER_ROLE, USER_STATUS


class UserForm(Form):
    next = HiddenField()
    role_id = RadioField(u"Role", [AnyOf([str(val) for val in USER_ROLE.keys()])],
            choices=[(str(val), label) for val, label in USER_ROLE.items()])
    status_id = RadioField(u"Status", [AnyOf([str(val) for val in USER_STATUS.keys()])],
            choices=[(str(val), label) for val, label in USER_STATUS.items()])
    # A demo of datepicker.
    created_time = DateField(u'Created time')
    submit = SubmitField(u'Save')
