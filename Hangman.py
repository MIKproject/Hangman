from random import *

word_list = ['слово', 'раз', 'работа']


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
    word = get_word(word_list)
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6
    print()
    print('Давайте играть в угадайку слов!')
    while tries:
        print(word_completion)
        print(f'Список уже названных букв {guessed_letters}')
        print(f'Список уже названных слов {guessed_words}')
        letter = input('Введите букву или слово целиком, если уже догадались:_').upper()
        if len(letter) == 1:
            guessed_letters.append(letter)
        if len(letter) > 1:
            guessed_words.append(letter)
        if letter == word:
            return 'Поздравляем, вы угадали слово! Вы победили!'
        if not letter.isalpha():
            print('Введите символ, являющийся буквой')
            continue
        if letter in word_completion:
            print('Эту букву Вы уже отгадали')
            continue
        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    word_completion = word_completion[:i] + letter + word_completion[i + 1:]
                    if word_completion == word:
                        return 'Поздравляем, вы угадали слово! Вы победили!'
        
        else:
            if len(letter) == 1:
                print('Такой буквы нет')
            if len(letter) > 1:
                print('Не верное слово!')
            tries -= 1
            print(display_hangman(tries))
        if tries == 0:
            return f'Вы проиграли! Правильный ответ: {word}'


print(play(get_word(word_list)))
