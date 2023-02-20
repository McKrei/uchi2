class MinLengthPasswordError(Exception):
   pass


class NoSpecialCharactersError(Exception):
    pass


class Password:
    SPECIAL = '!@#$%^&*()<>?,.'

    def __init__(self, password):
        if len(password) < 8:
            raise MinLengthPasswordError('Короткий пароль')
        elif not set(self.SPECIAL) & set(password):
            raise NoSpecialCharactersError('Нет специального символа')
        else:
            self.password = password

    def __str__(self):
        return f'Пароль: {self.password}'

s = input()

try:
    password = Password(s)
except MinLengthPasswordError as e:
    print(e)
except NoSpecialCharactersError as e:
    print(e)
else:
    print(password)
