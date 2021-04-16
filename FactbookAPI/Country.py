class Country:
    def __init__(self, data):
        self.name = data['name']
        self.intro = data['introduction']
        self.geo = data['geography']
        self.people = data['people']
        self.gov = data['government']
        self.economy = data['energy']
        self.comm = data['communications']
        self.transportation = data['transportation']
        self.mil = data['military_and_security']
        self.transnational = data['transnational_issues']

    def __str__(self):
        return self.name    