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
```

**Chamadas Recursivas**

Chamando fatorial(4), temos a seguinte sequência:

```
fatorial(4)
→ 4 * fatorial(3)
→ 3 * fatorial(2)
→ 2 * fatorial(1)
→ retorna 1
```
