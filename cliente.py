import socket

HOST = "127.0.0.1"
PORTA = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

mensagem = "Olá servidor!".encode()  #converter o texto em bytes (comunicação UDP)
sock.sendto(mensagem, (HOST,PORTA))

print("[CLIENTE] Mensagem enviada")
sock.close()
