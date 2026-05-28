from threading import Thread, Condition
import time

cola = []
cv = Condition()

def consumidor():
    with cv:
        while len(cola) == 0:
            print("Consumidor espera...")
            cv.wait()

        x = cola.pop(0)

    print("Consumidor recibió:", x)


def productor():
    time.sleep(2)

    with cv:
        cola.append("dato")
        print("Productor agregó dato")
        cv.notify()


Thread(target=consumidor).start()
Thread(target=productor).start()
