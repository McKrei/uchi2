class OperationError(Exception):
    pass


operations = '+-*/'


try:
    a = int(input())
    b = int(input())
    op = input()

    if op not in ('+-*/'):
        raise OperationError

    if op == '+':
        result = a + b

    elif op == '-':
        result = a - b

    elif op == '*':
        result = a * b

    elif op == '/':
        result = a / b

except ValueError:
    print('Ошибка ввода')

except OperationError:
    print('Неверная операция')

except Exception:
    print('Невозможно выполнить операцию')

else:
    print(result)
