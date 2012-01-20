# -*- coding: utf-8 -*-
# vi:si:et:sw=4:sts=4:ts=4

##
## Copyright (C) 2012 Async Open Source <http://www.async.com.br>
## All rights reserved
##
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU Lesser General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU Lesser General Public License for more details.
##
## You should have received a copy of the GNU Lesser General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., or visit: http://www.gnu.org/.
##
""" Domain classes to define required and visible fields """

from stoqlib.database.orm import ForeignKey, BoolCol, UnicodeCol
from stoqlib.database.orm import SingleJoin
from stoqlib.domain.base import Domain
from stoqlib.lib.translation import stoqlib_gettext

_ = stoqlib_gettext


class UIField(Domain):
    """This describes a field in form a.
    Can be used makae fields mandatory or hide them completely.
    """
    ui_form = ForeignKey('UIForm')
    field_name = UnicodeCol()
    description = UnicodeCol()
    visible = BoolCol()
    mandatory = BoolCol()


class UIForm(Domain):
    """This describes a form which has a number of fields"""
    form_name = UnicodeCol()
    description = UnicodeCol()
    fields = SingleJoin('UIField')

    def get_field(self, field_name):
        return UIField.selectOneBy(field_name=field_name,
                                   ui_form=self,
                                   connection=self.get_connection())


def create_default_forms(trans):
    person_fields = [
        ('name', _('Name'), True, True),
        ('phone_number', _('Phone number'), True, False),
        ('mobile_number', _('Mobile number'), True, False),
        ('fax', _('Fax'), True, False),
        ('email', _('Email'), True, False),
        ('street', _('Street'), True, True),
        ('street_number', _('Street number'), True, True),
        ('postal_code', _('Postal code'), True, False),
        ('district', _('District'), True, True),
        ('complement', _('Complement'), True, False),
        ('city', _('City'), True, False),
        ('state', _('State'), True, True),
        ('country', _('Country'), True, True),
        ]

    for name, desc in [('user', _('User')),
                       ('client', _('Client')),
                       ('employee', _('Employee')),
                       ('supplier', _('Supplier')),
                       ('transporter', _('Transporter')),
                       ('branch', _('Branch'))]:
        ui_form = UIForm(connection=trans,
                         form_name=name,
                         description=desc)
        for (field_name, field_description,
             visible, mandatory) in person_fields:
            UIField(connection=trans,
                    ui_form=ui_form,
                    field_name=field_name,
                    description=field_description,
                    visible=visible,
                    mandatory=mandatory)