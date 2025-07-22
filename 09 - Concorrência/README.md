**09 – Concorrência**

**Objetivo**

Explicar os conceitos de **concorrência** em linguagens de programação, comparando **processos** e **threads**, e demonstrar um exemplo com execução simultânea.


**Diferença entre Threads e Processos**

| Conceito   | Threads                              | Processos                           |
|------------|--------------------------------------|-------------------------------------|
| Memória    | Compartilham a mesma memória         | Cada processo tem sua memória       |
| Leveza     | Mais leves e rápidas                 | Mais pesados, criam cópias isoladas |
| Uso comum  | Pequenas tarefas simultâneas         | Execução paralela completa          |


**Exemplo: Execução concorrente com `threading` em Python**

Código: `concorrencia.py`

O código executa duas tarefas (Tarefa A e Tarefa B) com tempos diferentes, ao mesmo tempo, usando `threading`.

Saída esperada (pode variar):

```
Tarefa A - passo 1
Tarefa B - passo 1
Tarefa A - passo 2
Tarefa B - passo 2
...
Todas as tarefas finalizadas.
```

