import random 

class Game:
    def __init__(self):

        self.incorrect_letters = []
        self.guessed_letters_user = []
        self.actual_word = []
        self.main_word = []

    def reset_the_letter(self):
        "Спросить букву" 
        print(self.main_word[0])
        self.actual_word.clear()
        for letter in list(self.main_word[0]):
            if letter not in self.guessed_letters_user:
                self.actual_word.append('__')
            else:
                self.actual_word.append(letter)

        return ' '.join(self.actual_word)  

    def update_game_status(self, user_answer):
        'Обновление состояние игры'             
    
        for letter in self.main_word[0]:
            if user_answer == letter or user_answer in 'ий' and letter in 'йи' or user_answer in 'её' and letter in 'её':
                self.guessed_letters_user.append(user_answer)

        if user_answer not in list(self.main_word[0]) and user_answer not in self.incorrect_letters and user_answer not in self.guessed_letters_user :
            self.incorrect_letters.append(user_answer)

    def checking_for_winnings(self):

        full_word = self.reset_the_letter()
        if '_' not in full_word:
            return True

class Interface:
    def __init__(self, user):
        self.user = user

    def hidden_word(self):
        "Загаданное слово"
        full_word = self.user.reset_the_letter()
        print('\n')
        print(f'Слово: {full_word}')

    def picture_gallows(self):
        "Фото виселицы"
        for i in open(f"foto/{len(self.user.incorrect_letters)}.txt", 'r', encoding="utf-8"):   
            print(i)

    def user_errors(self):
        "Ошибки пользователей"
        print(f'Ошибки ({len(self.user.incorrect_letters)}): {", ".join(self.user.incorrect_letters)}')

    def number_of_attempts(self):
        'Количество попыток'
        number_attempts = 7 - len(self.user.incorrect_letters) 
        print(f'Количество попыток: {number_attempts}')

    def entering_the_next_letter(self):
        "Вывод следующей буквы"
        self.user.user_answer = input('Введите следующую букву: ')
        return self.user.user_answer[0]
    
    def cheking_for_exit(self):
        if self.user.checking_for_winnings() == True:
            self.hidden_word()
            self.picture_gallows()
            print(f'Слово {self.user.main_word[0]} отгаданно, вы выиграли ))')
            exit()


user = Game()  
console = Interface(user)

def read_random_word():
    'Вывод рандоиного слова'  
    with open('word.txt', 'r', encoding='utf-8') as file:
        line = file.readlines()
        user.main_word = line[random.randint(0, len(line) - 1)].split('\n')

read_random_word()
loop = True
while loop:
    console.cheking_for_exit()
    console.hidden_word()
    console.picture_gallows()
    console.user_errors()
    console.number_of_attempts()
    user_answer = console.entering_the_next_letter()
    user.update_game_status(user_answer)