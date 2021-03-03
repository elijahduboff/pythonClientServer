import time
import json
from socket import socket, AF_INET, SOCK_STREAM
import argparse
import logging
import log.client_log_config
from log.client_log_config import Log, log_func

logger = logging.getLogger('client')


# @Log()
@log_func
def get_server_response(server):
    """ Функция принимает на вход сокет сервера, получает сообщение, декодирует его в UTF-8 и возвращает Json"""
    server_json_response = server.recv(640).decode('utf-8')
    logger.info(f'Получен ответ сервера {server}')
    return server_json_response


# @Log()
@log_func
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


# @Log()
@log_func
def send_msg_to_server(server, json_msg):
    """ Функция принимает на вход сокет сервера, подготовленное сообщение в Json, кодирует сообщение
    и отправляет серверу"""
    server.send(json_msg.encode('utf-8'))
    logger.info('Сообщение отправлено')
    # print('Сообщение отправлено')


# @Log()
@log_func
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
    parser.add_argument('-m', default='text', type=str, help='Mode of launching client (text/only listen)')
    args = parser.parse_args()
    addr = args.a
    port = args.p
    mode = args.m
    server = socket(AF_INET, SOCK_STREAM)
    server.connect((addr, port))
    if mode == 'text':
        while True:
            message = str(input('Введите свое сообщение в общий чат, для выхода нажмите q'))
            if message == 'q':
                server.close()
                break
            send_msg_to_server(server, message)
            response = get_server_response(server)
            print(f'Сообщение в чат от {server} {response}')
    elif mode == 'listen':
        while True:
            response = get_server_response(server)
            if response:
                print(f'Сообщение в чат от {server} {response}')
    else:
        logger.error('Неправильно указан режим запуска клиента')
        exit(1)



    # presence_msg = make_presence_msg()
    # send_msg_to_server(server, presence_msg)
    # server_response = get_server_response(server)
    # get_data_from_msg(server_response)
    # server.close()


if __name__ == '__main__':
    main()
