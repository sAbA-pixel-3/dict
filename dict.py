# dict - dictionary
# ключом может быть только неизменяемый тип данных
#                   key  : value
# study_exams = {'Ivanov': 60, 'Petrov' :78, 'Sidorov' :85} # можно юзать любой тип данных

# methods

# print(study_exams.keys()) # просто показывает все "key" 
# print(study_exams.values()) # показывает все "value"
# print(study_exams.items()) # показывает все "key", "value" по отдельности
# print(study_exams.get('Ivanov')) # показывает значение по 'key', но если сделать ошибку все равно работает
# print(study_exams.pop('Ivanov')) # удаляет "key" и "value" по значению
# print(study_exams.clear()) # удаляет весь список dict
# print(study_exams.popitem()) # удаляет последний ключ и значение
#### study_exams.update({'Ivnov': 60}) # добавляет ключ и значение
#### print(study_exams)
# ##study_exams['Petrov'] = 90 # обновляет написаное, т е изменяет значение по ключу
# ##print(study_exams) # 
# del study_exams['Petrov'] # удаляет ключ и значение
## study_exams.setdefault('Ivnov', 80) # добавляет ключ и значение если в словаре его нет
## print(study_exams)
# q = study_exams.fromkeys(['Ivanov2', 'Petrov2', 'Bok'], 80) # создаёт ключ и значение
# w = study_exams.copy() # копирует словарь
# print(study_exams, q, w)





# students = {'Jhon':85, 'Emily':92, 'Michael': 78, 'Sophia':95, 'David': 87} 
# print("Average score of students: ", sum(students.values()) / 5) 

# people = {'John': 25, 'Alice': 30, 'Bob': 22}
# print("Alice: ", max(people.values()))
  
# students = {"John": [5, 4, 3], "Alice": [2, 4, 5], "Bob": [4, 4, 4]}
# q = sum(students.get('John')) / 3
# w = sum(students.get('Alice')) / 3
# e = sum(students.get('Bob')) / 3
# print("John:",q, "Alice:",w, "Bob:",e)

# fruits = {"apple": 2, "banana": 4, "cherry": 3}
# print("Banana: ", max(fruits.values()))  


