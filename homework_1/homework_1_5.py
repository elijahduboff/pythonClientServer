# Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового
# в строковый тип на кириллице.

import subprocess

yandex = ['ping', '-c 4', 'yandex.ru']
youtube = ['ping', '-c 4', 'youtube.com']


def ping_website(args):
    subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in subproc_ping.stdout:
        dec_line = line.decode('utf-8')
        print(dec_line)


ping_website(yandex)
ping_website(youtube)
