import socket
import web_app 

HOST, PORT = '', 5000
QUEUE = 5

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(QUEUE)

print('Starting server on port {}.\n'.format(PORT))
print('Open http://localhost:{} in your browser to view your site!\n'.format(PORT))

while True:

    client, address = s.accept()
    data = client.recv(4096)

    if data:
        # get a string representation of the incoming http request
        request_text = data.decode('utf-8')

        # use the handle_request function from web_app.py
        response_text = web_app.handle_request(request_text)
        client.send(bytes(response_text, 'utf-8'))

    client.close()
