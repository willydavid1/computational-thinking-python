import time
start_time = time.time()

def run ():
    objective = int(input('Choose a number:'))
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
    print(f"--- {round(time.time() - start_time, 2)} seconds ---")

if __name__ == '__main__':
    run()
