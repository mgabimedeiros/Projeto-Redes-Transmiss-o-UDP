import socket
import os

HOST = "127.0.0.1" #este computador
PORTA = 5000
TAMANHO_BUFFER = 2048 #1024x2 (folga)
PASTA_DESTINO = "arquivos_servidor" #onde os arquivos recebidos serão salvos

#cria a pasta de destino, caso não exista
os.makedirs(PASTA_DESTINO, exist_ok=True) 

#criação do socket UDP
#AF_INET - endereço IPv4
#SOCK_DGRAM - UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#associa o socket ao endereço e a porta
sock.bind((HOST,PORTA))

print(f"[SERVIDOR] escutando em {HOST}:{PORTA}...")

nome_arquivo_atual = None
blocos = []
try:
    while True: #mantem o servidor sempre ligado
        #espera a chegada de algum pacote, se não chega ele fica travado esperando
        dados, endereco = sock.recvfrom(TAMANHO_BUFFER)

        if dados.startswith(b"INICIO|"):
            nome_arquivo_atual = dados.decode().split("|",1)[1]
            blocos = [] #zera a lista para um novo arquivo
            print(f"[SERVIDOR] Início do arquivo '{nome_arquivo_atual}' vindo de {endereco}")
        elif dados == b"FIM":
            #junta todos os pedaços em uma sequência única de bytes
            conteudo_completo = b"".join(blocos)

            #salva com o prefixo "servidor_"
            nome_salvar = f"servidor_{nome_arquivo_atual}"
            caminho_salvar = os.path.join(PASTA_DESTINO, nome_salvar)

            with open(caminho_salvar, "wb") as f:
                f.write(conteudo_completo)

            print(f"[SERVIDOR] Arquivo salvo como '{caminho_salvar}'"
                  f"({len(conteudo_completo)} bytes, {len(blocos)} pacotes)")

            #Retorno do arquivo para o cliente
            print(f"[SERVIDOR] Devolvendo {nome_arquivo_atual} para {endereco}...") #endereço do cliente, de onde veio os dados
            sock.sendto(f"INICIO|{nome_arquivo_atual}".encode(), endereco)
            
        else:  #é um bloco do arquivo
            blocos.append(dados)
            print(f"[SERVIDOR] Pacote {len(blocos)} recebido ({len(dados)} bytes)")



except KeyboardInterrupt:
    print("\n[SERVIDOR] Encerrado pelo usuário")
finally:
    sock.close()
