from task_2 import create_ip_range
from ipaddress import ip_address
from subprocess import Popen, PIPE
from socket import gethostbyname
from tabulate import tabulate

'''
3. Написать функцию host_range_ping_tab(), возможности которой основаны на функции из примера 2. 
Но в данном случае результат должен быть итоговым по всем ip-адресам, 
представленным в табличном формате (использовать модуль tabulate). Таблица должна состоять из двух колонок
'''


def host_range_ping_tab(host_list, count=1):
    ip_list = []
    result = {
        'reached': [],
        'unreached': []
    }
    for host in host_list:
        ip_list.append(ip_address(gethostbyname(host)))
    for ip in ip_list:
        ping = Popen(f'ping -c {count} {ip}', shell=True, stdout=PIPE)
        ping.wait()
        if ping.returncode == 0:
            result['reached'].append(ip)
        else:
            result['unreached'].append(ip)
    print(tabulate(result, headers='keys'))


def main():
    host_list = create_ip_range()
    host_range_ping_tab(host_list)


if __name__ == '__main__':
    main()
