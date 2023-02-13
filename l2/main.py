class Button:
    pass


name, value = input(), input()
setattr(Button, name, value)
print(Button.__dict__)
