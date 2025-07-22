**06 – Subprogramas**

**Objetivo**

Demonstrar a diferença entre **passagem por valor** e **passagem por referência** em linguagens de programação, usando exemplos em **C** e **Python**.


**Exemplo em C**

- `por_valor(int x)` modifica apenas uma cópia da variável.
- `por_referencia(int *x)` modifica a variável original via ponteiro.


**Exemplo em Python**

- Inteiros são imutáveis, então `x` dentro da função não altera o valor externo.
- Já listas são objetos mutáveis: alterações no conteúdo afetam fora da função.


**Conclusão**

- **C** permite controlar diretamente como os parâmetros são passados.
- **Python** simula passagem por referência ao usar objetos mutáveis (como listas).


