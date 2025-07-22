**03 – Descrições Sintáticas e Semânticas**

**Objetivo**

Este desafio propõe a criação de uma mini-gramática fictícia e exemplos práticos de análise léxica para demonstrar o entendimento de regras sintáticas e semânticas em linguagens de programação.


**Mini-gramática: Liguagem fictícia chamada **CalcLang****

**Objetivo da linguagem**

Simular uma linguagem simples que permita somas e subtrações de números inteiros.


**Gramática (BNF simplificada)**

```bnf
<expressao> ::= <numero> | <numero> <operador> <expressao>
<numero>    ::= [0-9]+
<operador>  ::= '+' | '-'
```

Essa gramática permite expressões como:

```
10 + 5 - 2
7
100 + 4
```

**Análise Léxica (tokenização)**

Expressão de entrada:

```
10 + 5 - 2
```
Tokens gerados:

```
[NUM:10] [OP:+] [NUM:5] [OP:-] [NUM:2]
```

**Regras Semânticas (exemplo de interpretação)**

- O resultado da expressão 10 + 5 - 2 é 13
- A ordem da avaliação é da esquerda para a direita (sem precedência de operadores).

**Observações**

- A gramática é propositalmente simples, ideal para simular uma linguagem de expressões matemáticas básicas.
- Pode ser usada para construir um interpretador básico em Python ou outra linguagem, se desejado.

**Dica: Linguagens para tokenizar (opcional)**

Se quiser mostrar isso de forma prática, pode usar Python com uma função simples como:

```python
def lexer(expr):
    tokens = []
    for part in expr.split():
        if part.isdigit():
            tokens.append(f"[NUM:{part}]")
        else:
            tokens.append(f"[OP:{part}]")
    return tokens

print(lexer("10 + 5 - 2"))
# Saída: ['[NUM:10]', '[OP:+]', '[NUM:5]', '[OP:-]', '[NUM:2]']
```
