import socket

MASTER_IP = "X.X.X.X"  # Master IP address
MASTER_PORT = 12345      # Master port

# Connect to the master server.
worker = socket.socket()
print("Connecting to master...")
worker.connect((MASTER_IP, MASTER_PORT))
print("Connected to master.")

# Task loop: receive a task, evaluate it, and send back the result.
while True:
    data = worker.recv(1024)
    if not data:
        break
    task = data.decode()
    try:
        result = str(eval(task))
    except Exception as e:
        result = f"Error: {e}"
    worker.send(result.encode())

worker.close()
