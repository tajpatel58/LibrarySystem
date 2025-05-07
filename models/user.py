
class User:
    def __init__(self, name: str, date_of_birth: str, postcode: str):
        self.name = name
        self.date_of_birth = date_of_birth
        self.postcode = postcode
    
    def change_postcode(self, changed_postcode: str):
        self.postcode = changed_postcode