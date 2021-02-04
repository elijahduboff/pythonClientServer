# Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность
# кодов (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.

word1 = b'class'
word2 = b'function'
word3 = b'method'
print(word1)  # b'class'
print(type(word1))  # <class 'bytes'>
print(len(word1))  # 5
print(word2)  # b'function'
print(type(word2))  # <class 'bytes'>
print(len(word2))  # 8
print(word3)  # b'method'
print(type(word3))  # <class 'bytes'>
print(len(word3))  # 6
