""" Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

school_register = [
  {'studying_class': '4a', 'scores': [3,4,4,5,2]},
  {'studying_class': '5a', 'scores': [3,2,4,4,2]},
  {'studying_class': '6a', 'scores': [5,5,2,3,4]},
  {'studying_class': '7a', 'scores': [3,4,2,5,5]},
]

print('------')

for school_class in school_register:
    score_sum = 0
    students_num = 0
    for score in school_class['scores']:
      score_sum += score
      students_numb += len(score)
      
    current_class = school_class['studying_class']
    average_score = score_sum/len(school_class['scores']  
    print(f'Средняя оценка в классе {current_class} : {average_score}')
    
    school_grades_sum += score_sum
    school_students_sum += len(students_numb)

print()
print(f'Всего учеников: {school_students_sum}')
print('Сумма всех оценок: {}'.format(school_grades_sum))
school_avarage = school_grades_sum/school_students_sum
print(f'Средняя оценка по школе: {school_avarage}')
  #Комментарий 1: А что будет, если колличество оценок в разных классах будет разным?
  #Будет ли программа работать правильно?
  #Статус: исправленно. 
  #Заменил скадывание средних оценок по классу повторным суммированием оценок из списка.
