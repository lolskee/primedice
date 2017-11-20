import requests, json, os, time
from datetime import datetime

class PrimeDice:
    def __init__(self, api_key):
        self.BASE_URL = 'https://api.primedice.com/api/'
        self.api_key = api_key

    def make_bet(self, bet_amount):
        pass


