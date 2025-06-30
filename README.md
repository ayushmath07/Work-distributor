# Work-distributor
A multi-threaded Python server that distributes arithmetic computation tasks between the local machine and a connected external worker over sockets.
# 🔢 Distributed Arithmetic Task Processor

A Python-based client-server system that distributes arithmetic computation tasks between a local server and a connected remote worker. Designed to demonstrate basic distributed computing and concurrent task handling using sockets and threading.

---

## 🚀 Features

- ✅ **Task Offloading**: Distributes arithmetic expressions between local CPU and connected worker.
- 🔀 **Round-Robin Assignment**: Even-indexed tasks go to the worker; odd-indexed tasks are evaluated locally.
- ⚡ **Multi-threaded Execution**: Each task runs in a separate thread for faster processing.
- 🔗 **Socket Communication**: Uses TCP sockets for real-time worker-server interaction.
- 🧠 **Expression Evaluation**: Evaluates math expressions like `1+1`, `2*3`, `5**2`.

---

## 📁 Project Structure

main_server.py # Accepts user input and distributes tasks
worker_client.py # Receives tasks from server and sends back results

## 🛠️ How It Works

1. **Start the server** (`main_server.py`)
   - Binds to port `12345`
   - Waits for a worker to connect

2. **Start the worker** (`worker_client.py`)
   - Connects to the server
   - Listens for tasks, evaluates them, and returns results

3. **Input Tasks**
   - You enter comma-separated math expressions (e.g., `2+2, 5*3, 10/2`)
   - The server splits them across threads and sends some to the worker

4. **Output**
   - Each task is evaluated
   - Results are printed on the server side

---

## 💻 Example

**Input:**

Enter tasks (comma separated, e.g., 1+1, 23): 2+3, 56, 10-4

**Output:**

Task '2+3' result: 5
Task '5*6' result: 30
Task '10-4' result: 6

---

## ⚙️ Technologies Used

- Python 3
- `socket` (TCP communication)
- `threading` (for concurrency)
- `eval()` for simple math expression evaluation

---

## 📌 Notes

- Ensure both scripts are running in the same network environment.
- Avoid unsafe or malicious inputs since `eval()` is used without sanitization.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

