import threading
import time

def task(name):
    print(f"Task {name} started")
    time.sleep(2)  # Simulate a task taking some time
    print(f"Task {name} finished")

thread1 = threading.Thread(target=task, args=("A",))
thread2 = threading.Thread(target=task, args=("B",))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Both tasks are done!")