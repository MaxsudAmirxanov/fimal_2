import random 

class Game:
    def __init__(self):

        self.incorrect_letters = []
        self.asked_question = {}
        self.data_words = []
        self.guessed_letters = []
        self.actual_word = []

        for i in open(f"word.txt", 'r', encoding="utf-8"):   
            words = i.split('\n')
            self.data_words.append(words[0])
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

            letters_in_correct_word = []
            for i in self.main_word:
                letters_in_correct_word.append(i)

            if user_ansver not in letters_in_correct_word and user_ansver not in self.incorrect_letters:
                self.incorrect_letters.append(user_ansver)
                

        else:
            return 'Введите букву !'

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
        
        return f'Слово: {full_word}'

class Interface:
    def __init__(self, user):
        self.user = user

    def output_result(self):
        "Вывод результата"
        for i in open(f"foto/{len(self.user.incorrect_letters)}.txt", 'r', encoding="utf-8"):   
            print(i)
        print(f'Ошибки ({len(self.user.incorrect_letters)}): {", ".join(self.user.incorrect_letters)}')
        if len(list(user_1.main_word)) == len(user_1.guessed_letters):
            print(f'Слово {user_1.main_word} отгаданно, вы выиграли ))')
            exit()
        
    def ask_question_Interface(self):
        result = self.user.ask_question()
        print(result)
    
    def checking_question_Interface(self):
        user_ansver = input('Введите следующую букву: ')
        if self.user.checking_question(user_ansver) == 'Введите букву !':
            print(self.user.checking_question(user_ansver))
        number_attempts = 7 - len(user_1.incorrect_letters) 
        print(f'Количество попыток: {number_attempts}')

user_1 = Game()  
console = Interface(user_1)

loop = True
while loop:
    console.ask_question_Interface() 
    console.output_result()
    console.checking_question_Interface()

