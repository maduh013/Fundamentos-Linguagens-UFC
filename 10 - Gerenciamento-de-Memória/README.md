**10 – Gerenciamento de Memória**

**Objetivo**

Comparar como linguagens diferentes gerenciam a memória durante a execução de programas, especialmente em relação à **alocação** e **liberação** manual ou automática.


**Comparação: C vs Java**

| Característica          | C                            | Java                                  |
|-------------------------|------------------------------|----------------------------------------|
| Alocação de memória     | Manual (`malloc`, `calloc`)  | Automática com operadores (`new`)      |
| Liberação de memória    | Manual (`free`)              | Automática via Garbage Collector       |
| Riscos                  | Vazamento de memória, uso de ponteiros inválidos | GC resolve, mas pode causar pausas    |
| Controle do programador | Total                        | Parcial (o GC decide quando limpar)    |
| Exemplo de GC           | Não possui                   | Sim – `System.gc()` pode ser sugerido  |


**Explicações**

Linguagem C

O programador precisa alocar e liberar memória manualmente.

```c
#include <stdlib.h>
int* vetor = malloc(sizeof(int) * 10);
// ...
free(vetor);
```
Se esquecer de liberar (free), ocorre vazamento de memória.

Linguagem Java

A memória é alocada com new e liberada automaticamente pelo Garbage Collector.

```java
int[] vetor = new int[10];
// Java coleta o lixo automaticamente
```

Programadores não têm controle direto sobre quando a memória é liberada, mas podem sugerir com:

```
System.gc();
```
