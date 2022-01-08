import time
start_time = time.time()

def getNumber(text='Choose an integer:'):
    return int(input(text))

def enumeration(objective):
    response = 0

    while response ** 2 < objective:
        print(response)
        response += 1

    if response ** 2 == objective:
        print(f'The square root of {objective} is {response}')
    else:
        print(f'{objective} does not have an exact square root')

def approximation(objective):
    epsilon = 0.01
    step = epsilon ** 2
    response = 0.0

    while abs(response ** 2 - objective) >= epsilon and response <= objective:
        print(abs(response ** 2 - objective), response)
        response += step

    if abs(response ** 2 - objective) >= epsilon:
        print(f'The square root of {objective} was not found')
    else:
        print(f'The square root of {objective} is {response}')

def binary_search(objective):
    epsilon = 0.001
    low = 0.0
    high = max(1.0, objective)
    response = (high + low) / 2

    while abs(response ** 2 - objective) >= epsilon:
        print(f'low={low},  high={high}, response={response}')
        if response ** 2 < objective:
            low = response
        else:
            high = response

        response = (high + low) / 2

    print(f'The square root of {objective} is {response}')

def run ():
    text = """Select an option:
    1 - enumeration
    2 - approximation
    3 - binary_search
    """
    option = getNumber(text)
    objective = getNumber()

    if option == 1:
        enumeration(objective)
    elif option == 2:
        approximation(objective)
    elif option == 3:
        binary_search(objective)
    else:
        print('? xD')
    print(f"--- {round(time.time() - start_time, 2)} seconds ---")

if __name__ == '__main__':
    run()
