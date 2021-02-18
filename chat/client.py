import time
import json
from socket import socket, AF_INET, SOCK_STREAM
import argparse
import logging
import log.client_log_config

logger = logging.getLogger('client')


def get_server_response(server):
    """ Функция принимает на вход сокет сервера, получает сообщение, декодирует его в UTF-8 и возвращает Json"""
    server_json_response = server.recv(640).decode('utf-8')
    logger.info(f'Получен ответ сервера {server}')
    return server_json_response


def make_presence_msg():
    """ Функция формирует presense сообщение клиента и возвращает json объект с сообщением"""
    presence_msg_data = {
        "action": "presence",
        "time": time.time(),
        "type": "status",
        "user": {
            "account_name": "elijahduboff",
            "status": "Yep, I am here!"
        }
    }
    presence_json_msg = json.dumps(presence_msg_data)
    logger.info('Сформировано сообщение о присутствии')
    return presence_json_msg


def send_msg_to_server(server, json_msg):
    """ Функция принимает на вход сокет сервера, подготовленное сообщение в Json, кодирует сообщение
    и отправляет серверу"""
    server.send(json_msg.encode('utf-8'))
    logger.info('Сообщение отправлено')
    # print('Сообщение отправлено')


def get_data_from_msg(server_response_msg):
    """ Функция принимает на вход ответ сервера в Json, обрабатывает его и возвращает данные в словаре"""
    server_response_data = json.loads(server_response_msg)
    logger.info(f'Ответ сервера {server_response_data}')
    # print(f'Ответ сервера {server_response_data}')
    return server_response_data


# TODO Добавить проверку порта > 1024, добавить проверку коннекта к серверу

def main():
    parser = argparse.ArgumentParser(description='Chat Client\' Terminal Launcher')
    parser.add_argument('-a', required=True, type=str, help='Chat server address, required parameter')
    parser.add_argument('-p', default=7777, type=int, help='Chat server port, default is 7777')
    args = parser.parse_args()
    addr = args.a
    port = args.p
    server = socket(AF_INET, SOCK_STREAM)
    server.connect((addr, port))

    presence_msg = make_presence_msg()
    send_msg_to_server(server, presence_msg)
    server_response = get_server_response(server)
    get_data_from_msg(server_response)
    server.close()


if __name__ == '__main__':
    main()
