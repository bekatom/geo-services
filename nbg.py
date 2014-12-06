# -*- coding: utf-8 -*-
__author__ = 'Beka Tomashvili'
from suds.client import Client


class NBG:
    def __init__(self, curr):
        self.client = Client("http://nbg.gov.ge/currency.wsdl")
        self.curr = curr

    def get_currency_description(self):
        return self.client.service.GetCurrencyDescription(self.curr)

    def get_currency(self):
        return self.client.service.GetCurrency(self.curr)

    def get_currency_rate(self):
        return self.client.service.GetCurrencyRate(self.curr)

    def get_curr_change(self):
        return self.client.service.GetCurrencyChange(self.curr)

    def get_date(self):
        return self.client.service.GetDate()

    def get_currency_nbg(self):
        return {
            "abr": self.curr,  # კურსის აბრევიატურა , USD , RUB და ა.შ
            "currency": self.get_currency(),  # აბრუნებს ვალუტის კურსს, მაგ. "1.0754"
            "description": self.get_currency_description(),  # აბრუნებს ვალუტის აღწერას, მაგ. "10 ესტორნური კრონი"
            "change": self.get_curr_change(),  # აბრუნებს ვალუტის ცვლილების მნიშვნელობას, მაგ. "-0.0121"
            "rate": self.get_currency_rate(),  # 1 - თუ გაიზარდა; -1 - თუ დაიკლო, 0 - თუ იგივე დარჩა
            "date": self.get_date()  # აბრუნებს კურსების შესაბამის თარიღს
        }




