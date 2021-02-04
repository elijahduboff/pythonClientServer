# Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое
# и выполнить обратное преобразование (используя методы encode и decode).

word1 = 'разработка'
word2 = 'администрирование'
word3 = 'standard'
word4 = 'protocol'


def enc_dec_word(word):
    enc_word = word.encode()
    dec_word = enc_word.decode()
    return f'{word}, encoded: {enc_word}, decoded: {dec_word}'


print(enc_dec_word(word1))
print(enc_dec_word(word2))
print(enc_dec_word(word3))
print(enc_dec_word(word4))
