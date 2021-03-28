'''
Класс, который получает запросы пользователя и 
управляет вводом-выводом информации в программе
'''

'''
Метод, который выводи вопрос с вариантами ответа
@return dict
'''
def print_question_with_variants():
	print("question with variants")

'''
Метод, который получает ответ пользователя
@return str
'''
def get_user_answer():
	print('user answer getted')

'''
Метод, который выполняет сохранение данных в БД
@return void
'''
def save_user_result_to_db():
	print('data saved')

'''
Метод, который выводит сообщение-поздравление в конце игры
@return void
'''
def print_conglaturation_message():
	print('conglaturations!!!!')

'''
Метод для обновления рейтинга пользователя
и его вывода на экран
@return str
'''
def update_user_rating():
	print('rating updated')

'''
Метод, выполняющий возврат из статистики в главное меню
@return void
'''
def exit_from_statistic():
	print('close stats')