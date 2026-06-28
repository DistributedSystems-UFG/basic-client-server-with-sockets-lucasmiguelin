# client.py
from socket import *
from constCS import *

s = socket(AF_INET, SOCK_STREAM)
print(f"Conectando ao servidor {HOST}:{PORT}...")
s.connect((HOST, PORT)) 

print("\n=== Calculadora Remota Conectada ===")
print("Operações suportadas: add, subtract, multiply, divide")
print("Formato de uso: <operacao> <numero1> <numero2>")
print("Exemplo: add 10 5")
print("Digite 'sair' para encerrar a conexão.")

while True:
    mensagem = input("\nDigite a operação: ")
    
    if mensagem.lower() == 'sair':
        print("Encerrando cliente...")
        break
        
    if not mensagem.strip():
        continue # Ignora entradas vazias

    # Envia a string codificada para o servidor
    s.send(str.encode(mensagem))  
    
    # Recebe e imprime a resposta
    data = s.recv(1024)      
    print(f"Resultado do servidor: {bytes.decode(data)}")  

s.close()
