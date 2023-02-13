class Point:
    def __init__(self, *args):
        self.coords = args

    def __str__(self):
        return f'Точка с координатами {self.coords}'


coords = map(int, input().split())
my_point1 = Point(*coords)
print(my_point1)

class Point():
    def __init__(self, *args):
        self.coor = args

    def __str__(self):
        return f"Точка с координатами {self.coor}"
        
p = Point(list(map(int, input().split())))
print (p)


class Sequence:
    def __init__(self, *args):
        self.elements = list(args)

    def __str__(self):
        return f'Последовательность {self.elements}'

    def __len__(self):
        return len(self.elements)

elements = map(int, input().split())

seq = Sequence(*elements)
print(seq)
print(len(seq))



class RomanNumber:
   def __init__(self, number):
       self.number = number

   def __str__(self):
       return f'Число {self.number}'

   def __len__(self):
       return len(self.number)

   def __bool__(self):
       return bool(self.number)

number = RomanNumber(input())
print(number)
print(len(number))
print(bool(number))




class PrimeNumbers:
    def __init__(self, n):
        number = 2
        numbers = []
        while len(numbers) < n:
            for d in range(2, number - 1):
                if number % d == 0:
                    break
            else:
                numbers.append(number)
            number += 1
        self.numbers = numbers

    def __str__(self):
        return f'Последовательность из {len(self.numbers)} простых чисел {self.numbers}'

    def total(self):
        return sum(self.numbers)
n = int(input())
numbers = PrimeNumbers(n)
print(numbers)
print(numbers.total())
