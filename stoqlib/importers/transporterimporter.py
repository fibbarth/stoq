# -*- coding: utf-8 -*-
# vi:si:et:sw=4:sts=4:ts=4

##
## Copyright (C) 2007 Async Open Source
##
## This program is free software; you can redistribute it and/or
## modify it under the terms of the GNU Lesser General Public License
## as published by the Free Software Foundation; either version 2
## of the License, or (at your option) any later version.
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
##
## Author(s):       Johan Dahlin                <jdahlin@async.com.br>
##
##

from stoqlib.domain.address import Address, CityLocation
from stoqlib.domain.interfaces import IIndividual, ITransporter
from stoqlib.domain.person import Person
from stoqlib.importers.csvimporter import CSVImporter

class TransporterImporter(CSVImporter):
    fields = ['name',
              'phone_number',
              'mobile_number',
              'email',
              'rg',
              'cpf',
              'city',
              'country',
              'state',
              'street',
              'street_number',
              'district',
              'open_contract',
              'freight_percentage']

    def process_one(self, data, fields, trans):
        person = Person(
            connection=trans,
            name=data.name,
            phone_number=data.phone_number,
            mobile_number=data.mobile_number)

        person.addFacet(IIndividual,
                        connection=trans,
                        cpf=data.cpf,
                        rg_number=data.rg)

        ctloc = CityLocation.get_or_create(trans=trans,
                                           city=data.city,
                                           state=data.state,
                                           country=data.country)
        address = Address(is_main_address=True,
                          person=person, city_location=ctloc,
                          connection=trans,
                          street=data.street,
                          number=int(data.street_number),
                          district=data.district)

        dict(open_contract_date=self.parse_date(data.open_contract),
             freight_percentage=data.freight_percentage),
        person.addFacet(ITransporter, connection=trans)

