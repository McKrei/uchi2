class Number:
    ALPHABET = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    def __init__(self, number, base):
        result = ''
        while number != 0:
            digit = number % base
            if digit >= 10:
                digit = self.ALPHABET[digit]
            result += str(digit)
            number //= base
        self.value = result[::-1]

    def __str__(self):
        return f'{self.__class__.__name__}: {self.value}'



class Bin(Number):
    def __init__(self, number):
        super().__init__(number, 2)

    def to_dec(self):
        return int(self.value, 2)

    def __add__(self, other):
        return Bin(self.to_dec() + other.to_dec())

    def __sub__(self, other):
        return Bin(self.to_dec() - other.to_dec())

    def __mul__(self, other):
        return Bin(self.to_dec() * other.to_dec())

    def __floordiv__(self, other):
        return Bin(self.to_dec() // other.to_dec())


class Oct(Number):
    def __init__(self, number):
        super().__init__(number, 8)

    def to_dec(self):
        return int(self.value, 8)

    def __add__(self, other):
        return Oct(self.to_dec() + other.to_dec())

    def __sub__(self, other):
        return Oct(self.to_dec() - other.to_dec())

    def __mul__(self, other):
        return Oct(self.to_dec() * other.to_dec())

    def __floordiv__(self, other):
        return Oct(self.to_dec() // other.to_dec())


class Hex(Number):
    def __init__(self, number):
        super().__init__(number, 16)

    def to_dec(self):
        return int(self.value, 16)

    def __add__(self, other):
        return Hex(self.to_dec() + other.to_dec())

    def __sub__(self, other):
        return Hex(self.to_dec() - other.to_dec())

    def __mul__(self, other):
        return Hex(self.to_dec() * other.to_dec())

    def __floordiv__(self, other):
        return Hex(self.to_dec() // other.to_dec())


n1 = int(input())
n2 = int(input())
s = input()
if s == 'Bin':
    n1 = Bin(n1)
    n2 = Bin(n2)
elif s == 'Oct':
    n1 = Oct(n1)
    n2 = Oct(n2)
elif s == 'Hex':
    n1 = Hex(n1)
    n2 = Hex(n2)

print(n1 + n2)
print(n1 - n2)
print(n1 * n2)
print(n1 // n2)
