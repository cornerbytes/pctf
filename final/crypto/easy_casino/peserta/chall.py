FLAG = 'PCTF{FAKE_FLAG}'

def convert_to_int(x, y):
    try:
        x = int(x, 16)
        y = int(y, 16)
        return x, y
    except:
        return False

if __name__ == "__main__":
    print('='*40)
    print('Welcome to Easy_Casino!!!')
    x = input('Enter first lucky number in hexadecimal : ')
    y = input('Enter second lucky number in hexadecimal : ')

    if convert_to_int(x, y) == False:
        print('[NUMBER ERROR]')
        exit()

    if x != y:
        x, y = convert_to_int(x, y)
        if x == y :
            print('[Congratulation you guess the same number!]')
            print(FLAG)
    else:
        print('[DUPLICATE NUMBER]')
    print('='*40)
