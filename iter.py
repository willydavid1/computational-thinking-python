# En Python, un iterable es un objeto que se puede utilizar en un bucle definido. Si un objeto es iterable significa que se puede pasar como argumento a la función iter. El iterable que se pasa como parámetro a la función iter
# regresa un iterator.

def run ():
    frutas = ['manzana', 'pera', 'mango']
    iterador = iter(frutas)
    print(f'iterador {iterador}')
    print(f'iterador {next(iterador)}')
    print(f'iterador {next(iterador)}')
    print(f'iterador {next(iterador)}')
    # print(next(iterador)) # Error StopIteration

    for fruta in frutas:
        print(fruta)

if __name__ == '__main__':
    run()
