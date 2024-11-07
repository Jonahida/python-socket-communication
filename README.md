# Python Socket Communication: Echo Client-Server

This project demonstrates a basic client-server application using Python's `socket` library. The client sends a message to the server, and the server responds with the received message followed by a fixed string `" Response from server."`.

## Overview

- **Echo Client**: A Python script that connects to a server, sends a message, and prints the server's response.
- **Echo Server**: A Python script that listens for incoming client connections, receives messages, and sends back a response.

## Features

- **Socket Communication**: Uses TCP/IP to send and receive messages between the client and server.
- **Error Handling**: The scripts include error handling for connection issues and message transmission failures.
- **Command-Line Usage**: Both scripts can be run from the command line, with the client accepting a message as an argument.

## Prerequisites

- Python 3.x
- `socket` library (included by default in Python's standard library)

## How to Use

### 1. Clone the repository

```bash
git clone https://github.com/Jonahida/python-socket-echo-server-client.git
cd python-socket-communication
```

### 2. Run the server

To start the server, run the following command in one terminal window:

```bash
python echo-server.py
```

The server will start listening on `127.0.0.1` (localhost) and port `65432`.

### 3. Run the client

To send a message to the server, use the following command in a different terminal window:

```bash
python echo-client.py <your-message>
```

Replace `<your-message>` with the text you want to send. For example:

```bash
python echo-client.py "Hello, Server!"
```

The client will send the message to the server, and the server will respond with the received message plus `" Response from server."`.

## Example Output

**Client**:

```bash
python echo-client.py "Hello, Server!"
```

Output:

```bash
Received: b'Hello, Server! Response from server.'
```

**Server**:

```bash
python echo-server.py
```
Output:

```bash
Server is listening on 127.0.0.1:65432
Connected by ('127.0.0.1', 12345)
```

### 4. Stop the server
To stop the server, simply press `Ctrl+C` in the terminal where the server is running.

# Contributing

Contributions are welcome! To contribute to this project:

- Fork the repository.
- Create a new branch for your feature or bug fix.
- Submit a pull request or open an issue to discuss any enhancements or bug fixes.

# License

This project is licensed under the MIT License. See the LICENSE file for details.