**07 – Implementação de Subprogramas**

**Objetivo**

Simular a **pilha de chamadas de subprogramas** usando um exemplo recursivo simples.


**Exemplo: Fatorial Recursivo**

Código (`recursao.py`)

```python
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)

print(fatorial(4))
