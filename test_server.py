import json
import unittest
import time

from chat.client import make_presence_msg, get_server_response, send_msg_to_server, get_data_from_msg
from chat.server import get_client_msg, make_response_to_client, send_response_to_client


class TestSocket:
    def __init__(self, test_msg):
        self.test_msg = test_msg
        self.encoded_msg = None
        self.received_msg = None

    def send(self, json_message_to_send):
        self.encoded_msg = self.test_msg.encode('utf-8')
        self.received_msg = json_message_to_send

    def recv(self, max_len):
        return self.test_msg.encode('utf-8')


class TestServer(unittest.TestCase):
    def test_get_client_msg(self):
        test_client_msg = make_presence_msg()
        test_socket = TestSocket(test_client_msg)
        self.assertEqual(get_client_msg(test_socket), test_client_msg)

    def test_make_response_to_client_200(self):
        client_msg = make_presence_msg()
        server_response_data = {
            'response': '200',
            'alert': 'ok'
        }
        response_json = json.dumps(server_response_data)
        self.assertEqual(make_response_to_client(client_msg), response_json)

    def test_make_response_to_client_400(self):
        client_msg_data = {}
        client_msg = json.dumps(client_msg_data)
        server_response_data = {
            'response': '400',
            'alert': 'bad request'
        }
        response_json = json.dumps(server_response_data)
        self.assertEqual(make_response_to_client(client_msg), response_json)

    def test_send_response_to_client(self):
        server_response_data = {
            'response': '400',
            'alert': 'bad request'
        }
        response_json = json.dumps(server_response_data)
        test_socket = TestSocket(response_json)
        send_response_to_client(test_socket, response_json)
        self.assertEqual(test_socket.encoded_msg, test_socket.received_msg)



if __name__ == '__main__':
    unittest.main()
