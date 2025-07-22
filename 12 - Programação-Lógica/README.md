**12 – Programação Lógica**

**Objetivo**

Modelar um problema usando **programação lógica** com base na linguagem **Prolog**. O exemplo aborda uma **árvore genealógica**.


**Domínio escolhido: Genealogia**

O programa representa relações familiares como:

- pai/2 → quem é pai de quem
- mae/2 → quem é mãe de quem
- irma/2 → quem é irmã de quem (com base em pai, mãe e gênero)


**Código em Prolog: `genealogia.pl`**

O código define os **fatos** e **regras** lógicas que permitem inferir relacionamentos.

Exemplo de consulta:
```prolog
?- irma(maria, jose).
true.
```


**Ferramentas**

Interpretador recomendado: SWI-Prolog (https://www.swi-prolog.org/)


