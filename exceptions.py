def divide_elements(list, divider):
    try:
        return [i / divider for i in list]
    except ZeroDivisionError as e:
        print(e)
        return list

def run ():
    array = list(range(10))
    divider = 0
    print(divide_elements(array, divider))

if __name__ == '__main__':
    run()
