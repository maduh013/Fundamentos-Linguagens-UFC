**05 – Estruturas de Controle**

**Objetivo**

Criar um programa simples utilizando **estrutura condicional (`if`)**, **laços (`while`)** e **controle de fluxo** com uma lógica personalizada.


**Contexto escolhido**

Simulação de um sistema de **atendimento por senhas**. A cada chamada, o atendente pergunta se a pessoa está presente. Se não estiver, ela volta para o fim da fila.


**Explicação do Código (`controle.py`)**

- A fila é uma lista de nomes simulando senhas.
- Um loop `while` percorre os nomes.
- A cada nome:
  - O programa pergunta se a pessoa está presente.
  - Se sim, ela é atendida.
  - Se não, é colocada de volta ao final da fila.
- A repetição continua até todos serem chamados.


**Estruturas utilizadas**

- `while` → para percorrer a fila
- `if/else` → para tomar decisões com base na resposta do usuário
- `append` → controle de fluxo para reordenar fila


