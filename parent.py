# Шегай Денис, 11-901

import sys
import os
import random


args = sys.argv
n = int(args[1])
print(f"Запущен Parent.py с PID {os.getpid()} и аргументом {n}")
children = list()
for i in range(0, n):
    child = os.fork()
    if child == 0:
        os.execvp("./child.py", ("python3", "child.py", str(random.randint(5, 10))))
    else:
        children.append(child)

for subprocess in children:
    status = os.wait()
    print(f"Дочерний процесс с PID {subprocess} завершился. Статус завершения {status}.")
