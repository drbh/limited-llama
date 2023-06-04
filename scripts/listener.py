from dataclasses import dataclass
import socket
import re

# Set up simple TCP server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen(1)

# dataclass for storage
@dataclass
class Storage:
    data: str = ''
    result: float = 0
    operator: str = ''

# Create a storage instance
storage = Storage()

while True:
    # Accept a connection
    conn, addr = server.accept()
    print('Connection from', addr)

    # Process incoming messages
    while True:
        data = conn.recv(1024)
        if not data:
            break

        # try to parse the data
        data = data.decode()
        storage.data += data

        # print the result
        print('data:', storage.data)

        response = '' # default response unless we have an action

        # check if the storage.data ends in '{"action": 0}'
        if storage.data.endswith('{"action": 0}'):

            # Regex pattern
            pattern = r'\[\s*(\d+),\s*([\/\+\-\*]),\s*(\d+)'

            # Find matches
            matches = re.findall(pattern, storage.data)

            # if len is not 1 make matches None
            if len(matches) != 1:
                matches = None
            else:
                matches = matches[0]

            print(matches)  # [('13', '/', '4')]

            # compute the result use operator matches[1] on the ..[0] and ..[2]
            if matches:
                if matches[1] == '+':
                    storage.result = int(matches[0]) + int(matches[2])
                elif matches[1] == '-':
                    storage.result = int(matches[0]) - int(matches[2])
                elif matches[1] == '*':
                    storage.result = int(matches[0]) * int(matches[2])
                elif matches[1] == '/':
                    storage.result = int(matches[0]) / int(matches[2])

            response = str(storage.result)

        # Send a response
        conn.sendall(response.encode())

    conn.close()
