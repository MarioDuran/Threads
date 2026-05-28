import threading
import time

N = 3
buffer = []

empty = threading.Semaphore(N)  # espacios libres
full = threading.Semaphore(0)   # elementos disponibles
mutex = threading.Lock()


def producer():
    for i in range(5):
        item = f"item-{i}"

        empty.acquire()  # esperar espacio libre

        with mutex:
            buffer.append(item)
            print("Produce:", item)

        full.release()  # avisar que hay un elemento

        time.sleep(1)


def consumer():
    for i in range(5):
        full.acquire()  # esperar elemento disponible

        with mutex:
            item = buffer.pop(0)
            print("Consume:", item)

        empty.release()  # avisar que hay espacio libre

        time.sleep(2)


t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

t1.start()
t2.start()

t1.join()
t2.join()

print("Fin")
