class OperationError(Exception):
    pass

def main():
    try:
    #     # print(4/0)
    #     print(4/2)

        raise ValueError


    except ValueError:
        print(f'ValueError')


    # finally:
    #     print('final')

if __name__ == '__main__':
    main()


# s = 'Привет мир'
# s2 = 'Прив'
