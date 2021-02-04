# Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание
# соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode
# и также проверить тип и содержимое переменных.
word1 = 'разработка'
word2 = 'сокет'
word3 = 'декоратор'
print(word1)  # разработка
print(type(word1))  # <class 'str'>
print(word2)  # сокет
print(type(word2))  # <class 'str'>
print(word3)  # декоратор
print(type(word3))  # <class 'str'>
word_uc1 = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
word_uc2 = '\u0441\u043e\u043a\u0435\u0442'
word_uc3 = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
print(word_uc1)  # разработка
print(type(word_uc1))  # <class 'str'>
print(word_uc2)  # сокет
print(type(word_uc2))  # <class 'str'>
print(word_uc3)  # декоратор
print(type(word_uc3))  # <class 'str'>
