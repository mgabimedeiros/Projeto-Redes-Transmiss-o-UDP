# Projeto-Redes-Transmissão-UDP
Integrantes - Equipe 1:

Miriam Gonzaga da Silva Santos - <mgss4> \n
Maria Gabriella Medeiros da Silva - <mgms> \n
Lucas Jose Duarte Cavalcanti - <ljdc> \n
Mario Daniel Teles da Silva Filho - <mdtsf> \n

Instruções para execução:

Deve acontecer em dois terminais, um que vai rodar o Servidor e outro para o cliente, isso se deve pois o servidor permanece sempre ativo aguardando a chegada de novos arquivos. Os programas se conectam entre si a partir dos endereços com conexão socket.

No primeiro terminal coloque "python servidor.py" -> o servidor vai iniciar e indicar que está esperando 

Abra um segundo terminal e coloque"python cliente.py arquivos_teste/<nome do arquivo>" -> o cliente vai começar a enviar o arquivo e o servidor a receber, ao encerrar acontece o retorno, dessa forma:

cliente envia arquivo -> servidor recebe e armazena em "arquivos_servidor" ->
arquivo totalmente carregado e armazenado -> servidor envia arquivo para o cliente ->
cliente recebe o arquivo e armazena em "arquivos_cliente"

As respectivas pastas de armazenamento de arquivos (servidor e cliente) são criadas enquanto o programa estiver rodando

Durante o envio e recebimento de arquivos é possível acompanhar o tamanho de cada pacote e em quantos pacotes um arquivo foi quebrado.

