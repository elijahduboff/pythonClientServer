import time
import json
from socket import socket, AF_INET, SOCK_STREAM
import argparse


def get_server_response(server):
    server_json_response = server.recv(640).decode('utf-8')
    return server_json_response


def make_presence_msg():
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
    return presence_json_msg


def send_msg_to_server(server, json_msg):
    server.send(json_msg.encode('utf-8'))
    print('Сообщение отправлено')


def get_data_from_msg(server_response_msg):
    server_response_data = json.loads(server_response_msg)
    print(f'Ответ сервера {server_response_data}')
    return server_response_data


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
