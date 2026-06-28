# server.py
from socket import *
from constCS import *

s = socket(AF_INET, SOCK_STREAM) 
s.bind((HOST, PORT)) 
s.listen(1) 

print(f"Servidor de Calculadora rodando em {HOST}:{PORT}...")
print("Aguardando conexões...")

while True: # Mantém o servidor vivo para múltiplos clientes (um por vez)
    (conn, addr) = s.accept()  
    print(f"\n[+] Cliente conectado: {addr}")
    
    while True: # Loop para receber múltiplas requisições do mesmo cliente
        data = conn.recv(1024) 
        if not data: 
            break # Encerra o loop interno se o cliente desconectar
            
        mensagem = bytes.decode(data).strip()
        print(f"Requisição recebida: {mensagem}")
        
        # Lógica da Calculadora
        partes = mensagem.split()
        
        try:
            operacao = partes[0].lower()
            num1 = float(partes[1])
            num2 = float(partes[2])
            
            if operacao == 'add':
                resultado = num1 + num2
            elif operacao == 'subtract':
                resultado = num1 - num2
            elif operacao == 'multiply':
                resultado = num1 * num2
            elif operacao == 'divide':
                if num2 == 0:
                    resultado = "Erro: Divisão por zero não permitida."
                else:
                    resultado = num1 / num2
            else:
                resultado = f"Erro: Operação '{operacao}' desconhecida."
                
        except IndexError:
            resultado = "Erro: Formato inválido. Use: operacao num1 num2"
        except ValueError:
            resultado = "Erro: Por favor, envie apenas números válidos."
        except Exception as e:
            resultado = f"Erro inesperado no servidor: {str(e)}"
            
        # Envia a resposta de volta ao cliente
        conn.send(str.encode(str(resultado))) 
        
    conn.close() 
    print(f"[-] Conexão com {addr} encerrada.")
