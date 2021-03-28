'''
Класс для работы с БД
'''


'''
Инициализация базы данных
@return session
'''
def init_db(instance):
	if instance is None:
		print('db created')
	else 
		print('db getted')


'''
Получение всех вопросов из бд
@return dict
'''
def get_all_questions_from_db(session)
	print('questions getted')

'''
Обновление БД
@return void
'''
def update_db(session)
	print('update db')

'''
Удаление пользователя из БД
@return bool
'''
def delete_user(session)
	print('user deleted')

'''
Добавление вопроса в БД
@return db_models.Question
'''
def add_new_question(session):
	print('question added')

'''
Проверка соединение
@return session
'''
def test_connection(session):
	print("okey")