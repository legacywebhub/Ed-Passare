import multiprocessing
import time

def task(name):
    print(f"Task {name} started")
    time.sleep(2)  # Simulate a task taking some time
    print(f"Task {name} finished")

if __name__ == "__main__":
    process1 = multiprocessing.Process(target=task, args=("A",))
    process2 = multiprocessing.Process(target=task, args=("B",))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("Both tasks are done!")