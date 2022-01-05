def run ():
    objective = int(input('Choose an integer:'))
    response = 0

    while response ** 2 < objective:
        print(response)
        response += 1

    if response ** 2 == objective:
        print(f'The square root of {objective} is {response}')
    else:
        print(f'{objective} does not have an exact square root')

if __name__ == '__main__':
    run()
