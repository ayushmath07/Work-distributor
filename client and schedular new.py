import socket
import threading

def process_task(task, use_worker, worker_conn):
    try:
        if use_worker:
            worker_conn.send(task.encode())
            result = worker_conn.recv(1024).decode()
        else:
            result = str(eval(task))
        print(f"Task '{task}' result: {result}")
        print()
    except Exception as e:
        print(f"Error processing task '{task}': {e}")

server = socket.socket()
server.bind(("0.0.0.0", 12345))
server.listen(1)
print("Waiting for a worker connection...")

worker_conn, addr = server.accept()
print(f"Worker connected: {addr}")

while True:
    user_input = input("Enter tasks (comma separated, e.g., 1+1, 2*3) or 'exit': ")
    if user_input.lower() == "exit":
        break

    tasks = [task.strip() for task in user_input.split(",") if task.strip()]
    threads = []
    for i, task in enumerate(tasks):
        use_worker = (i % 2 == 0)
        thread = threading.Thread(target=process_task, args=(task, use_worker, worker_conn))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

worker_conn.close()
server.close()
print("Server shut down.")

