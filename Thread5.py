from threading import Thread, Barrier
import time
import random

barrera = Barrier(3)  # esperar a 3 hilos


def trabajador(nombre):
    print(f"{nombre} trabajando antes de la barrera")
    time.sleep(random.uniform(1, 3))

    print(f"{nombre} llegó a la barrera")
    barrera.wait()

    print(f"{nombre} pasó la barrera")


Thread(target=trabajador, args=("Hilo 1",)).start()
Thread(target=trabajador, args=("Hilo 2",)).start()
Thread(target=trabajador, args=("Hilo 3",)).start()
