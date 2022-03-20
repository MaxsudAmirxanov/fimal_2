from multiprocessing.dummy import active_children
import random 
import os

asked_question = {}
data_words = []
topical_word = []

class Game:
    def __init__(self):
        self.number_of_errors = 0
        self.foto_name = 0
        for i in open(f"word.txt", 'r', encoding="utf-8"):   
            words = i.split('\n')
            data_words.append(words[0])
        self.main_word = data_words[random.randint(0, len(data_words) - 1)]
        for number, letters in enumerate(self.main_word):
            print(f'{letters} -- {number}')
            asked_question[number] = {letters: False}
        


    def checking_question(self, user_ansver):
        "Проверка ответа"
        print(asked_question)
        for number, letters in asked_question.items():
            print(letters)
            for letter, enter in letters.items():
                if user_ansver == letter:
                    asked_question[number] = {letter: True}
        word = []
        for i in self.main_word:
            word.append(i)
        if user_ansver not in word:
            self.number_of_errors += 1

        print(asked_question)

    def ask_question(self):
        "Задать вопрос"
        topical_word.clear()
        for number, letters in asked_question.items():
            for letter, enter in letters.items():
                if enter == False:
                    topical_word.append('__')
                else:
                    topical_word.append(letter)
        full_word = ' '.join(topical_word)
        
        print(f'Слово: {full_word}')


    def output_result(self):
        "Вывод результата"


class Interface:
    def __init__(self, user):
        self.user = user

    def output_result(self):
        "Вывод результата"
        for i in open(f"foto/{user_1.number_of_errors}.txt", 'r', encoding="utf-8"):   
            print(i)


user_1 = Game()  
console = Interface(user_1)


loop = True
while loop:
    user_1.ask_question() 
    user_ansver = input('Введите следующую букву: ')
    user_1.checking_question(user_ansver)
    console.output_result()
    number_attempts = 7 - user_1.number_of_errors 
    print(f'Количество попыток: {number_attempts}')
    if user_1.number_of_errors == 7:
        loop = False



