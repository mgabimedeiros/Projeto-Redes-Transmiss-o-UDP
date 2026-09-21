import socket

HOST = "127.0.0.1" #este computador
PORTA = 5000
TAMANHO_BUFFER = 2048 #1024x2 (folga)

#criação do socket UDP
#AF_INET - endereço IPv4
#SOCK_DGRAM - UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#associa o socket ao endereço e a porta
sock.bind((HOST,PORTA))

print(f"[SERVIDOR] escutando em {HOST}:{PORTA}...")

try:
    while True: #mantem o servidor sempre ligado
        #espera a chegada de algum pacote, se não chega ele trava
        dados, endereco = sock.recvfrom(TAMANHO_BUFFER)
        print(f"[SERVIDOR] recebi {len(dados)} bytes de {endereco}:{dados}")
except KeyboardInterrupt:
    print("\n[SERVIDOR] Encerrado pelo usuário")
finally:
    sock.close()
