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
