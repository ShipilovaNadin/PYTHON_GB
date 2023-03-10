# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод: 
# пара-ра-рам рам-пам-папам па-ра-па-дам 
# Вывод:
# Парам пам-пам

vowels = "аеёиоуыэюя"
song = input().split()
rhythm = [sum([True for j in word if j.lower() in vowels]) for word in song]
#  если 16 строчку кода развернуть в цикл то получится следующее
# rhythm = [] #  рифма это пустой спсиок
# for word in song: #  по каждому слову в песне проходимся и 
#     rhythm.append(sum([True for j in word if j.lower() in vowels]))  #  в случае если в слове есть символ, совпадающий с теми что в строке гласные то в список будет добавляться тру(функция сум считает тру в кажом слове и в список попадает цифра, означающее количество гласных в слове)

if all(rhythm) and len(set(rhythm)) == 1:
    print("Парам пам-пам")
else:
    print("пам парам")

    
# def vowels_counter(S):
# 	vowels = list('а е ё и о у ы э ю я'.split())
# 	vowels_counter = list()
# 	for i in S:
# 	    counter = 0
# 	    for ch in i:
# 	        if ch in vowels:
# 	            counter += 1
# 	    vowels_counter.append(counter)
# 	return vowels_counter
	
# 	# пара-ра-рам рам-пам-папам па-ра-па-дам
# s = list("фа ма па ра".split())  # можно заменить на input().split()
	
# print("Парам пам-пам" if len(set(r := vowels_counter(s))) == 1 and r[0] != 0 else "Пам парам")