
class User:
    def __init__(self, name: str, date_of_birth: str, postcode: str, ):
        self.name = name
        self.date_of_birth = date_of_birth
        self.postcode = postcode
        self.borrowed_books = []
        self.balance = 0
    
    def change_postcode(self, changed_postcode: str):
        self.postcode = changed_postcode

    def __str__(self):
        user_as_string = f'User: {self.name}, DOB: {self.date_of_birth}'
        return user_as_string

    
