from ipaddress import ip_address
from task_1 import host_ping

'''
. Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона. Меняться должен только 
последний октет каждого адреса. По результатам проверки должно выводиться соответствующее сообщение.
'''


def create_ip_range():
    try:
        start_ip = input('Введите ip адрес для проверки доступности ')
        last_oct = str(start_ip).split('.')[3]
        last_oct = int(last_oct)
        start_ip = ip_address(start_ip)
    except ValueError:
        print('Введите корректный ip-адрес')
        exit(1)
    except IndexError:
        print('Введите корректный ip-адрес')
        exit(1)
    try:
        range_length = int(input('Введите длину диапазона ip адресов для проверки доступности '))
    except ValueError:
        print('Длина диапазона должна быть целым числом!')
        exit(1)
    ip_list = []
    ip_range_gen = [start_ip + i if (last_oct + range_length) < 255 else start_ip - i for i in range(range_length)]
    for ip in ip_range_gen:
        ip_list.append(str(ip))
    return ip_list


def main():
    host_list = create_ip_range()
    print(host_ping(host_list))


if __name__ == '__main__':
    main()
