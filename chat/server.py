from socket import socket, AF_INET, SOCK_STREAM
import json
import argparse
import logging
import log.server_log_config
from log.server_log_config import Log, log_func

logger = logging.getLogger('server')


# @Log()
@log_func
def get_client_msg(chat_client):
    client_json_msg = chat_client.recv(640).decode('utf-8')
    logger.info(f'Сообщение принято сервером от {chat_client}')
    # print(f'Сообщение принято сервером от {chat_client}')
    return client_json_msg


# TODO добавить проверку на вводимые данные клиента и добавить тесты
# @Log()
@log_func
def make_response_to_client(client_json_msg):
    client_msg_data = json.loads(client_json_msg)
    if client_msg_data:
        server_response_data = {
            'response': '200',
            'alert': 'ok'
        }
        server_json_response = json.dumps(server_response_data)
        logger.info('Сформирован ответ клиенту')
        return server_json_response
    else:
        server_response_data = {
            'response': '400',
            'alert': 'bad request'
        }
        server_json_response = json.dumps(server_response_data)
        logger.info('Сформирован ответ клиенту')
        return server_json_response


# @Log()
@log_func
def send_response_to_client(chat_client, server_json_response):
    chat_client.send(server_json_response.encode('utf-8'))
    logger.info(f'Ответ сервера отправлен клиенту {chat_client}')
    # print(f'Ответ сервера отправлен клиенту {chat_client}')


# TODO Добавить проверку порта > 1024
def main():
    parser = argparse.ArgumentParser(description='Chat Server Terminal\' Launcher')
    parser.add_argument('-p', default=7777, type=int, help='Chat server port number, default 7777')
    parser.add_argument('-a', default='', type=str, help='IP-address for listening, default is any')
    args = parser.parse_args()
    addr = args.a
    port = args.p
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind((addr, port))
    sock.listen(1)

    while True:
        chat_client, addr = sock.accept()
        chat_client_msg = get_client_msg(chat_client)
        server_response_msg = make_response_to_client(chat_client_msg)
        send_response_to_client(chat_client, server_response_msg)


if __name__ == '__main__':
    main()
