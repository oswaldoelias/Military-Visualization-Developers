import json, os

from .Country import Country

class FactbookApi:

    def __init__(self):
        filename = os.path.join(os.path.dirname(__file__), 'factbook.json')
        with open(filename) as f:
            fb = json.load(f)

        try:
            self.fb = fb['countries']
            self.countries = list(self.fb.keys())
        except Exception:
            raise Exception("An error occurred while processing factbook.json")

    def getCountry(self, country):
        '''
        country: string

        Returns country: Country
        '''

        if not self.isCountry(country):
            raise ValueError("Error: Country not found")

        return Country(self.fb[country]['data'])

    def isCountry(self, country):
        return country in self.countries