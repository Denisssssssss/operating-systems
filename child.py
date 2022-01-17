# Шегай Денис, 11-901

import os
import random
import sys
import time

args = sys.argv
arg = int(args[1])
print(f"Запущена программа Child в процессе с PID {os.getpid()} с аргументом {arg}.")
time.sleep(arg)
os._exit(random.randint(0, 1))
