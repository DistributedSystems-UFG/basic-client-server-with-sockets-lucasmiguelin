# Client-Server Basics (2.0) - Calculadora Remota

Este projeto é uma atividade prática da disciplina de Sistemas Distribuídos que implementa uma arquitetura Cliente-Servidor utilizando a biblioteca `socket` do Python. O projeto original (Fig 2.3 do livro-texto) foi expandido para atuar como uma **Calculadora Remota**.

## Funcionalidades Implementadas

A complexidade do processamento no servidor foi aumentada. Ele não apenas ecoa mensagens, mas atua processando operações matemáticas enviadas pelo cliente. 

O cliente pode invocar de forma contínua as seguintes funcionalidades (operações) no servidor em uma única requisição/sessão:
- `add` (Adição)
- `subtract` (Subtração)
- `multiply` (Multiplicação)
- `divide` (Divisão com tratamento para divisão por zero)

O servidor também possui tratamento de exceções para pacotes mal formatados ou uso de strings onde deveriam ser valores numéricos.

## Como executar

1. Certifique-se de ter o Python 3 instalado em sua máquina.
2. Os três arquivos (`server.py`, `client.py` e `constCS.py`) devem estar no mesmo diretório.
3. Abra um terminal e inicie o servidor primeiro:
   ```bash
   python server.py
