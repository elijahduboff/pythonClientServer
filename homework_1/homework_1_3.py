# Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
word1 = b'attribute'  # ok
# word2 = b'класс'  # SyntaxError: bytes can only contain ASCII literal characters.
# word3 = b'функция'  # SyntaxError: bytes can only contain ASCII literal characters.
word4 = b'type'  # ok
