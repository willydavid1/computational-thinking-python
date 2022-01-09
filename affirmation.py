def get_first_letter(list_of_words):
    response = []

    for word in list_of_words:
        assert type(word) == str, f'{word} is not a str'
        assert len(word) > 0, f'{word} is empty'

        response.append(word[0])

    return response

def run ():
    list_of_words = ['test', 'hi', '123']
    list_of_words_bad = ['test', 'hi', 123]
    print(get_first_letter(list_of_words))

    try:
        print(get_first_letter(list_of_words_bad))
    except Exception as e:
        print(e)

if __name__ == '__main__':
    run()
