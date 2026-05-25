import threading
import time

contador = 0
ITERACIONES = 100_000
lock = threading.Lock()

def incrementar():
    global contador

    for _ in range(ITERACIONES):
        with lock:
            valor = contador
            valor = valor + 1

            time.sleep(0)

            contador = valor

hilo_a = threading.Thread(target=incrementar)
hilo_b = threading.Thread(target=incrementar)

hilo_a.start()
hilo_b.start()

hilo_a.join()
hilo_b.join()

print("Resultado esperado:", ITERACIONES * 2)
print("Resultado obtenido:", contador)
