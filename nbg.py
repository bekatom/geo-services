# -*- coding: utf-8 -*-
__author__ = 'Beka Tomashvili'
from suds.client import Client
## See service documentation here
# https://services.nbg.gov.ge/

class NBG:
    def __init__(self, curr):
        self.client = Client("https://services.nbg.gov.ge/Rates/Service.asmx?wsdl")
        self.curr = curr
        self.data = self.client.service.GetCurrentRates(curr).CurrencyRate[0]

    def get_currency_description(self):
        return self.data.Name

    def get_currency(self):
        return self.data.Code

    def get_currency_rate(self):
        return self.data.Rate

    def get_curr_change(self):
        return self.data.Diff

    def get_date(self):
        return str(self.data.Date)

    def get_valid_date(self):
        return str(self.data.Date)

    def get_currency_nbg(self):
        return {
            "abr": self.data.Code,  # კურსის აბრევიატურა , USD , RUB და ა.შ
            "currency": self.data.Rate,  # აბრუნებს ვალუტის კურსს, მაგ. "1.0754"
            "description": self.data.Name,  # აბრუნებს ვალუტის აღწერას, მაგ. "10 ესტორნური კრონი"
            "quantity": self.data.Quantity,  # აბრუნებს ვალუტის აღწერას, მაგ. "10 ესტორნური კრონი"
            "change": self.data.Diff,  # აბრუნებს ვალუტის ცვლილების მნიშვნელობას, მაგ. "-0.0121"
            "valid_from_date" : str(self.data.ValidFromDate),
            "date":  str(self.data.Date)  # აბრუნებს კურსების შესაბამის თარიღს
        }
