from ipaddress import ip_address
from socket import gethostbyname
from subprocess import Popen, PIPE

'''
1. Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность 
сетевых узлов. Аргументом функции является список, в котором каждый сетевой узел должен быть представлен 
именем хоста или ip-адресом. 
В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего 
сообщения («Узел доступен», «Узел недоступен»). 
При этом ip-адрес сетевого узла должен создаваться с помощью функции ip_address().
'''
host_list = ['ya.ru', 'google.com', '192.168.1.1', '192.168.1.254']


def host_ping(host_list, count=1):
    ip_list = []
    result_list = []
    for host in host_list:
        ip_list.append(ip_address(gethostbyname(host)))
    for ip in ip_list:
        ping = Popen(f'ping -c {count} {ip}', shell=True, stdout=PIPE)
        ping.wait()
        if ping.returncode == 0:
            result_list.append(f'{ip} - доступен')
        else:
            result_list.append(f'{ip} - недоступен')
    return result_list


def main():
    print(host_ping(host_list))


if __name__ == '__main__':
    main()
