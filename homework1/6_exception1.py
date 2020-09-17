"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user(some_dict):
  while True:
    try:
      user_reply = input('Спросите у друга что-нибудь ')
      if user_reply == 'Пока':
        print('Ну пока-пока')
        break
      elif user_reply in some_dict:
        print(some_dict[user_reply])
    except KeyboardInterrupt:
      print()
      print('Пока')
      break
    
dictionary = {
  "Как дела" : "Отлично",
  "Что делаешь" : "Программирую",
  "Что программируешь" : "Да тут всякую дичь",
  "Пока" : "Ну пока",
  "Привет" : "Даров"
}
ask_user(dictionary)