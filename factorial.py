def factorial(n):
    '''Calculate the factorial of n
    n int > 0
    returns n!
    '''
    print(n)
    if n == 1:
        return 1

    return n * factorial(n - 1)

def run ():
    n = int(input('Write an integer: '))
    print(factorial(n))

if __name__ == '__main__':
    run()
