import random 

class Game:
    def __init__(self):

        self.incorrect_letters = []
        self.asked_question = {}
        self.data_words = []
        self.guessed_letters = []
        self.actual_word = []

    def reading_random_word(self):   
        "Чтеное рандомного слова"
        for i in open(f"word.txt", 'r', encoding="utf-8"):   
            words = i.split('\n')
            self.data_words.append(words[0])

    def create_dict_for_word(self):
        "Создание словарика"
        self.main_word = self.data_words[random.randint(0, len(self.data_words) - 1)]
        for number, letters in enumerate(self.main_word):
            self.asked_question[number] = {letters: False}
    
    def checking_question(self, user_ansver):
        "Проверка ответа"
        if len(list(user_ansver)) == 1:
            for number, letters in self.asked_question.items():
                for letter, enter in letters.items():
                    if user_ansver == letter or user_ansver == 'й' and letter == 'и' or user_ansver == 'и' and letter == 'й' or user_ansver == 'е' and letter == 'ё' or user_ansver == 'ё' and letter == 'е':
                        self.asked_question[number] = {letter: True}
                        self.guessed_letters.append(user_ansver)

            if user_ansver not in list(self.main_word) and user_ansver not in self.incorrect_letters:
                self.incorrect_letters.append(user_ansver)
        else:
            return False

    def ask_question(self):
        "Задать вопрос"
        self.actual_word.clear()
        for number, letters in self.asked_question.items():
            for letter, enter in letters.items():
                if enter == False:
                    self.actual_word.append('__')
                else:
                    self.actual_word.append(letter)
        full_word = ' '.join(self.actual_word)
        
        return full_word

class Interface:
    def __init__(self, user):
        self.user = user

    def hidden_word(self):
        "Загаданное слово"
        full_word = self.user.ask_question()
        print('\n')
        print(f'Слово: {full_word}')

    def picture_gallows(self):
        "Фото виселицы"
        for i in open(f"foto/{len(self.user.incorrect_letters)}.txt", 'r', encoding="utf-8"):   
            print(i)

    def user_errors(self):
        "Ошибки пользователей"
        print(f'Ошибки ({len(self.user.incorrect_letters)}): {", ".join(self.user.incorrect_letters)}')

    def number_of_errors(self):
        'Количество ошибок'
        number_attempts = 7 - len(user_1.incorrect_letters) 
        print(f'Количество попыток: {number_attempts}')

    def entering_the_next_letter(self):
        "Вывод следующей буквы"
        user_ansver = input('Введите следующую букву: ')
        if self.user.checking_question(user_ansver) == False:
            print('Введите букву !')


user_1 = Game()  
console = Interface(user_1)

loop = True
while loop:
    console.hidden_word()
    console.picture_gallows()
    console.user_errors()
    console.number_of_errors()
    console.entering_the_next_letter()

