import time, os
from multiprocessing import Process

stop_flag = False ##

def burn():
    while not stop_flag:
        pass

processes = []
for i in range(os.cpu_count()):
    t = Process(target=burn)
    t.start()
    processes.append(t)
    print(f"Thread {i} started")

time.sleep(2500)

stop_flag = True

for p in processes:
    p.terminate()

print("All threads stopped.")