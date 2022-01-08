import time
start_time = time.time()

def run ():
    objective = int(input('Choose an integer:'))
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
    print(f"--- {time.time() - start_time} seconds ---")

if __name__ == '__main__':
    run()
