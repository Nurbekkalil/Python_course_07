

language_eng_rus = {
    'white': 'белый',
    'black': 'черный',
    'red': 'красный',
    'green': 'зеленый',

}

language_rus_eng = {
   'белый': 'white',
    'черный': 'black',
    'красный': 'red',
    'зеленый': 'green',

}

language_rus_krg = {
    'белый': 'ак',
    'черный': 'кара',
    'красный': 'кызыл',
    'зеленый': 'жашыл',
}

word = []

while True:


    language = input('Choose the language')
    if language == 'eng to rus':
        word = input('The words in english')
        print(language_eng_rus[word])

    elif language == 'rus to eng':
        word = input('The words in russian')
        print(language_rus_eng[word])

    elif language == 'rus to krg':
        word = input('The words in russian')
        print(language_rus_krg[word])

    else: print('error')