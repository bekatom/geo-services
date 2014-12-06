# -*- coding: utf-8 -*-
__author__ = 'Beka Tomashvili'
from suds.client import Client

class RS:
    def __init__(self, identification):
        self.client = Client("https://services.rs.ge/WayBillService/WayBillService.asmx?WSDL")
        self.user = "vobi:12345678910"
        self.password = "vobi1234"
        self.identification = identification

    def __get_company_name(self):
        return self.client.service.get_name_from_tin(self.user, self.password, self.identification)

    def __get_company_is_payer(self):
        return self.client.service.is_vat_payer_tin(self.user, self.password, self.identification)

    def get_company_rs_info(self):
        return {
            "name": self.get_company_name(),
            "is_payer": self.get_company_is_payer()
        }


















