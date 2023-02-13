
import math


class Fraction:
    def __init__(self, num, den):
        self.num, self.den = self.get_reduced_fraction(num, den)

    @staticmethod
    def get_reduced_fraction(num, den):
        """Принимает числитель и знаменатель дроби
        и возвращает кортеж: числитель и знаменатель сокращенной дроби."""
        gcd = math.gcd(num, den)
        return num // gcd, den // gcd

    @staticmethod
    def get_common_denominator(den1, den2):
        """Принимает знаменатель первой и знаменатель второй дроби и
        возвращает общий знаменатель."""
        common_den = den1 * den2 // math.gcd(den1, den2)
        return common_den

    def __add__(self, other):
        common_den = self.get_common_denominator(self.den, other.den)
        num = common_den // self.den * self.num + common_den // other.den * other.num
        num, den = self.get_reduced_fraction(num, common_den)
        return Fraction(num, den)

    def __sub__(self, other):
        common_den = self.get_common_denominator(self.den, other.den)
        num = common_den // self.den * self.num - common_den // other.den * other.num
        num, den = self.get_reduced_fraction(num, common_den)
        return Fraction(num, den)

    def __mul__(self, other):
        num = self.num * other.num
        den = self.den * other.den
        num, den = self.get_reduced_fraction(num, den)
        return Fraction(num, den)

    def __truediv__(self, other):
        num = self.num * other.den
        den = self.den * other.num
        num, den = self.get_reduced_fraction(num, den)
        return Fraction(num, den)

    def __str__(self):
        return f'Дробь {self.num}/{self.den}'


num, den = map(int, input().split())
fraction1 = Fraction(num, den)
num, den = map(int, input().split())
fraction2 = Fraction(num, den)
print(fraction1 + fraction2)
print(fraction1 - fraction2)
print(fraction1 * fraction2)
print(fraction1 / fraction2)




import math


class Fraction:
    def __init__(self, num, den):
        self.num, self.den = self.get_reduced_fraction(num, den)

    @staticmethod
    def get_reduced_fraction(num, den):
        """Принимает числитель и знаменатель дроби
        и возвращает кортеж: числитель и знаменатель сокращенной дроби."""
        gcd = math.gcd(num, den)
        return num // gcd, den // gcd

    @staticmethod
    def get_common_denominator(den1, den2):
        """Принимает знаменатель первой и знаменатель второй дроби и
        возвращает общий знаменатель."""
        common_den = den1 * den2 // math.gcd(den1, den2)
        return common_den

    def __eq__(self, other):
        common_den = self.get_common_denominator(self.den, other.den)
        return common_den // self.den * self.num == common_den // other.den * other.num

    def __ne__(self, other):
        common_den = self.get_common_denominator(self.den, other.den)
        return common_den // self.den * self.num != common_den // other.den * other.num

    def __gt__(self, other):
        common_den = self.get_common_denominator(self.den, other.den)
        return common_den // self.den * self.num > common_den // other.den * other.num

    def __ge__(self, other):
        common_den = self.get_common_denominator(self.den, other.den)
        return common_den // self.den * self.num >= common_den // other.den * other.num

    def __lt__(self, other):
        common_den = self.get_common_denominator(self.den, other.den)
        return common_den // self.den * self.num < common_den // other.den * other.num

    def __le__(self, other):
        common_den = self.get_common_denominator(self.den, other.den)
        return common_den // self.den * self.num <= common_den // other.den * other.num

    def __str__(self):
        return f'Дробь {self.num}/{self.den}'


num, den = map(int, input().split())
fraction1 = Fraction(num, den)
num, den = map(int, input().split())
fraction2 = Fraction(num, den)
print(fraction1 == fraction2)
print(fraction1 != fraction2)
print(fraction1 > fraction2)
print(fraction1 >= fraction2)
print(fraction1 < fraction2)
print(fraction1 <= fraction2)



import math


class Fraction:
    def __init__(self, num, den):
        self.num, self.den = self.get_reduced_fraction(num, den)

    @staticmethod
    def get_reduced_fraction(num, den):
        """
        Принимает числитель и знаменатель дроби
        и возвращает кортеж: числитель и знаменатель сокращенной дроби.
        """
        gcd = math.gcd(num, den)
        return num // gcd, den // gcd

    @staticmethod
    def get_common_denominator(den1, den2):
        """
        Принимает знаменатель первой и знаменатель второй дроби и
        возвращает общий знаменатель.
        """
        common_den = den1 * den2 // math.gcd(den1, den2)
        return common_den

    def __call__(self):
        return Fraction(self.den, self.num)

    def __str__(self):
        return f'Дробь {self.num}/{self.den}'


num, den = map(int, input().split())
fraction = Fraction(num, den)
new_fraction = fraction()
print(new_fraction)
