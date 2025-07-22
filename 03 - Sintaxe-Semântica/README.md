**03 – Descrições Sintáticas e Semânticas**

**Objetivo**

Criar uma linguagem fictícia simples com gramática própria e apresentar exemplos de análise léxica para representar os conceitos de sintaxe e semântica estudados em linguagens de programação.


**Linguagem fictícia: **CalcLang****

**Descrição**

A **CalcLang** é uma linguagem fictícia criada para representar expressões matemáticas simples envolvendo **somas e subtrações** de inteiros.


**Gramática (BNF simplificada)**

```bnf
<expressao> ::= <numero> | <numero> <operador> <expressao>
<numero>    ::= [0-9]+
<operador>  ::= '+' | '-'
```

**Exemplos válidos segundo a gramática:**
```
7
10 + 5
8 - 2 + 3
```

**Análise Léxica**

Para a entrada:

```
10 + 5 - 2
```

Os tokens gerados seriam:

```
[NUM:10] [OP:+] [NUM:5] [OP:-] [NUM:2]
```
