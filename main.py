import random 


def read_random_word():
    'Вывод рандоиного слова'  
    with open('words.txt', 'r', encoding='utf-8') as file:
        return file.readlines()[random.randint(0, 9)].strip()

class Game:
    def __init__(self, word):
        self.main_word = word
        self.guessed_letters_user = []
        self.incorrect_letters = []
        self.shaded_word = ['__' for i in list(self.main_word)]

    def won(self):
        if len(self.main_word) == len(self.guessed_letters_user):
            return True
        else:
            return False

    def lose(self):
        if len(self.incorrect_letters) == 7:
            return True
        else:
            return False

    def update_game_status(self, user_answer):
        'Обновление состояние игры'  
        for number, true_letter in enumerate(list(self.main_word)):
            if true_letter == user_answer:
                self.shaded_word[number] = user_answer
                self.guessed_letters_user.append(user_answer)
        
        if user_answer not in list(self.main_word) and user_answer not in self.incorrect_letters:
            self.incorrect_letters.append(user_answer)
                
class Interface:
    def __init__(self, user):
        self.user = user

    def hidden_word(self):
        "Загаданное слово"
        print('\n')
        print(f'Слово: ' + ' '.join(self.user.shaded_word))

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
        user_answer = input('Введите следующую букву: ')
        return user_answer[0]

    def game_over(self):
        if self.user.won() == True:
            print(f"Слово {self.user.main_word} отгаданно. Вы выиграли !!!")
            exit() 

        if self.user.lose() == True:
            print("К сожалению все попытки потрачены, игра окончена :(")
            exit()
        pass

word = read_random_word()
user = Game(word)  
console = Interface(user)

loop = True
while loop:
    print(user.guessed_letters_user)
    console.game_over()
    console.hidden_word()
    console.picture_gallows()
    console.user_errors()
    console.number_of_attempts()
    user_answer = console.entering_the_next_letter()
    user.update_game_status(user_answer)
