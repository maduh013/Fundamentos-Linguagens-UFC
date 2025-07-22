import threading
import time

def tarefa(nome, tempo):
    for i in range(3):
        print(f"{nome} - passo {i+1}")
        time.sleep(tempo)

# Criando duas threads
t1 = threading.Thread(target=tarefa, args=("Tarefa A", 1))
t2 = threading.Thread(target=tarefa, args=("Tarefa B", 1.5))

t1.start()
t2.start()

t1.join()
t2.join()

print("Todas as tarefas finalizadas.")
