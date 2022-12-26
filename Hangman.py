from random import *

word_list = ['слово', 'работа', 'КЛЮЧ', 'КНИГА', 'ЕНОТ', 'МАШИНКА', 'КОРОВА', 'ТЕЛЕЖКА', 'ШЛЕМ', 'КНОПКА', 'ШНУР', 'ЧЕРНЫЙ',
'ВЛАСТЕЛИН', 'СКАЙП', 'ДУБ', 'ЧАСЫ', 'ТРУБА', 'ЕЛКА', 'ИНСТИТУТ', 'КОРОБКА', 'ТАБЛИЧКА', 'ВОДА', 'СКОВОРОДА',
'МНОГОНОЖКА', 'ЕВРЕЙ', 'ТЕРМИТ', 'КАЧЕК', 'РУЛОН', 'МАГНИТОФОН', 'НОГА', 'СЛОН', 'МИКРОВОЛНОВКА', 'ТОРТ', 'МАК',
'ДЫМ', 'ЧАЙКА', 'ВАЛЕТ', 'ПЛИНТУС', 'ШАПКА', 'ДИНОЗАВР', 'ТОРШЕР', 'БАЛАЛАЙКА', 'БАНКА', 'ЯХТА', 'ОВЦА', 'БАНАН',
'ДУБ', 'АНИМЕ', 'РАДУГА', 'БУКВА', 'ВЕЛОСИПЕД', 'БАНДЖО', 'ГОЛУБЬ', 'ВИНТОВКА', 'КУБОК', 'ЖАСМИН', 'ТЕЛЕФОН',
'АНДРОИД', 'ГОРА', 'ХАЛАТ', 'ЖЕТОН', 'ОБОД', 'МЫЛО', 'ЙОГ', 'ШИШКА', 'ДОЛЛАР', 'КОЛОНКА', 'КУБИК', 'ОМАР',
'РАКЕТА', 'МОРКОВКА', 'ЗЕРКАЛО', 'МОЛОТ', 'ВОЗДУХ', 'ЗМЕЙ', 'ЁЖ', 'ПАЛЬМА', 'МАСЛО', 'ДИДЖЕЙ', 'МЕШОК', 'ТЮБИК',
'МОЗГ', 'ПОЕЗД', 'РОЗЕТКА', 'ПАРАШЮТИСТ', 'БЕЛКА', 'ШПРОТЫ', 'САМОСВАЛ', 'ПАЗЛ', 'БУТЫЛКА', 'КРЕМЛЬ', 'ПИЦЦА',
'МАКАРОНЫ', 'КОВЕР', 'ЗУБЫ', 'ЯРЛЫК', 'КАШАЛОТ', 'МАРС', 'ШАКАЛ', 'ПОМАДА', 'ДЖИП']


def get_word(word):
    return choice(word_list).upper()


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
        # голова, торс, обе руки, одна нога
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                ''',
        # голова, торс, обе руки
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                ''',
        # голова, торс и одна рука
        '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                ''',
        # голова и торс
        '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                ''',
        # голова
        '''
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                ''',
        # начальное состояние
        '''
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                '''
    ]
    return stages[tries]


def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6 # количество попыток
    
    print('Давайте играть в угадайку слов!')
    print(f'Виселица: {display_hangman(tries)}')
    print(f'Загаданное слово: {word_completion}')
    
    while tries:
        print(f'Список уже названных букв {guessed_letters}')
        print(f'Список уже названных слов {guessed_words}')
        letter = input('Введите букву или слово целиком: ').upper()
        if not letter.isalpha():
            print('Введите букву или слово, попробуйте еще раз')
            continue
        if letter in guessed_letters or letter in guessed_words:
            print('Вы это уже вводили')
            continue

        if len(letter) > 1:
            if letter == word or guessed:
                print('Поздравляем, вы угадали слово! Вы победили!')
                print(f'Загаданное слово: {word}')
                break
            elif letter != word:
                print(f'Не верное слово! Осталось попыток {tries - 1}')
                tries -= 1
                print(f'Виселица: {display_hangman(tries)}')
                guessed_words.append(letter)
            
        if len(letter) == 1:
            if letter in word:
                word_completion_as_list = list(word_completion)
                indices = [i for i in range(len(word)) if word[i] == letter]
                for index in indices:
                    word_completion_as_list[index] = letter
                word_completion = ''.join(word_completion_as_list)
                guessed_letters.append(letter)
                print('Вы угадали букву!')
                print(word_completion)
                if '_' not in word_completion:
                    print('Поздравляем, вы угадали слово! Вы победили!')
                    print(f'Загаданное слово: {word}')
                    break
                    
            elif letter not in word:
                print(f'Такой буквы нет! Осталось попыток {tries - 1}')
                tries -= 1
                print(f'Виселица: {display_hangman(tries)}')
                guessed_letters.append(letter)
        
        if tries == 0:
            print(f'Виселица: {display_hangman(tries)}')
            print(f'Вы проиграли! Правильный ответ: {word}')
            break


def hangman(word):
    wanna_play = int(input('Играть снова? (да-1/0-нет): '))
    while wanna_play == 1:
        word = get_word(word_list)
        play(word)
        wanna_play = int(input('Играть снова? (да-1/0-нет): '))
        print()
    return 'Возвращайтесь снова, до свидания!'


print(hangman(play(get_word(word_list))))