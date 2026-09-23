import socket
import sys #leitura de parâmetros no terminal
import os #lida com arquivos e caminhos

HOST = "127.0.0.1"
PORTA = 5000
TAMANHO_PCT = 1024

#lê o nome do arquivo digitado no terminal ("python cliente.py texte.txt")
#o sys.argv gera uma lista com tudo que foi escrito no terminal
if len(sys.argv) != 2: #se o tamanho da lista ta diferente de 2 você esqueceu algo
    print("Uso: python cliente.py <nome_do_arquivo>") #com essa formatação -> sys.argv[1] = <nome_do_arquivo>
    sys.exit(1)

caminho = sys.argv[1]  #assimila o caminho ao nome do arquivo escrito no terminal

#verifica se o arquivo existe
if not os.path.isfile(caminho):
    print(f"[CLIENTE] Arquivo '{caminho}' não encontrado")
    sys.exit(1)

nome_arquivo = os.path.basename(caminho)  #pega o nome do arquivo

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Primeio pacote informa o nome e indica que o que chega agora faz parte desse pacote
sock.sendto(f"INICIO|{nome_arquivo}".encode(), (HOST,PORTA)) #o encode converte o texto em bytes
print(f"[CLIENTE] Enviando arquivo '{nome_arquivo}'...")

#Pacotes de dados (blocos de até 1024 bytes)
numero = 0
with open (caminho, "rb") as f:  #abre o arquivo em read binary (rb)
    while True:
        bloco = f.read(TAMANHO_PCT) #lê até 1024 bytes por vez
        if not bloco:
            break
        sock.sendto(bloco, (HOST,PORTA))
        numero +=1
        print(f"[CLIENTE] Pacote {numero} enviado ({len(bloco)} bytes)")

#Último pacote, encerra o recebimento desse pacote
sock.sendto(b"FIM", (HOST,PORTA))
print(f"[CLIENTE] Envio concluído: {numero} pacotes.")


sock.close()
