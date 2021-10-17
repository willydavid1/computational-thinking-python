def run ():
    num1 = int(input('Choose an integer: '))
    num2 = int(input('Choose another integer: '))

    if num1 > num2:
        print('num1 > num2')
    elif num1 < num2:
        print('num1 < num2')
    else:
        print('The two numbers are equal')

if __name__ == '__main__':
    run()
