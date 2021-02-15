import json
import unittest
import time

from chat.client import make_presence_msg, get_server_response, send_msg_to_server, get_data_from_msg


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


class TestClient(unittest.TestCase):
    def test_make_presence_message(self):
        presence_message = make_presence_msg()
        self.assertTrue(presence_message, 'Ошибка в формировании presence сообщения')

    def test_send_message_to_server(self):
        test_msg = make_presence_msg()
        test_socket = TestSocket(test_msg)
        send_msg_to_server(test_socket, test_msg)
        self.assertEqual(test_socket.encoded_msg, test_socket.received_msg)

    def test_get_server_response(self):
        response_200 = {
            'response': '200',
            'alert': 'ok'
        }
        response_400 = {
            'response': '400',
            'alert': 'bad request'
        }
        response_200_json = json.dumps(response_200)
        response_400_json = json.dumps(response_400)
        test_socket_200 = TestSocket(response_200_json)
        self.assertEqual(get_server_response(test_socket_200), response_200_json)
        test_socket_400 = TestSocket(response_400_json)
        self.assertEqual(get_server_response(test_socket_400), response_400_json)

    def test_get_data_from_msg(self):
        response_200 = {
            'response': '200',
            'alert': 'ok'
        }
        response_400 = {
            'response': '400',
            'alert': 'bad request'
        }
        server_response = json.dumps(response_200)
        server_response_400 = json.dumps(response_400)
        self.assertEqual(get_data_from_msg(server_response), response_200)
        self.assertEqual(get_data_from_msg(server_response_400), response_400)




if __name__ == '__main__':
    unittest.main()
