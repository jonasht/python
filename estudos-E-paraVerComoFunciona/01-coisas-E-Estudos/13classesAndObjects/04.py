import datetime
def l (): print("="*30)

class User:
    def __init__(self, nome_completo, birthday):
        self.nome = nome_completo
        self.birthday = birthday

        nome_pieces = nome_completo.split(' ')
        self.primeiro_nome = nome_pieces[0]
        self.sobrenome = nome_pieces[-1]
    def age(self):
        today = datetime.date(2001, 5, 12)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd)
        age_in_days = (today - dob).days
        age_in_years = age_in_days / 365
        
        return int(age_in_years)
        
user = User("dave bowman".title(), "19710315")
print(user.nome)
print(user.primeiro_nome)
print(user.sobrenome)
print(user.birthday)

print(user.age())


        

