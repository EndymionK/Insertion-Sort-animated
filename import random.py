import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import numpy as np

def intercambiar(A, i, j):
    """Función auxiliar para intercambiar los elementos i y j de la lista A."""
    if i != j:
        A[i], A[j] = A[j], A[i]

def orden_insercion(A):
    """Ordenamiento por inserción: ordenar A de menor a mayor"""
    for i in range(1, len(A)):
        j = i
        while j > 0 and A[j] < A[j - 1]:
            intercambiar(A, j, j - 1)
            j -= 1
            yield A

def grafico(A, N, titulo, generador):
    # Inicializar figura y ejes.
    fig, ax = plt.subplots()
    ax.set_title(titulo)

    # Inicializar un gráfico de barras. Los valores de las barras se actualizarán en cada iteración de la animación.
    bar_rects = ax.bar(range(len(A)), A, align="edge")

    # Establecer límites de los ejes.
    ax.set_xlim(0, N)
    ax.set_ylim(0, float(max(A)) * 1.1)

    # Colocar una etiqueta de texto en la esquina superior izquierda del gráfico para mostrar
    # el número de operaciones realizadas por el algoritmo de ordenamiento (cada "yield" se
    # trata como 1 operación).
    texto = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    iteracion = [0]
    def update_fig(A, rects, iteracion):
        for rect, val in zip(rects, A):
            rect.set_height(val)
        iteracion[0] += 1
        texto.set_text("Número de operaciones: {}".format(iteracion[0]))

    animacion = animation.FuncAnimation(fig, func=update_fig,
        fargs=(bar_rects, iteracion), frames=generador, interval=1,
        repeat=False)
    plt.show()

def extraer_array():
    data2 = pd.read_csv("C:/Users/andre/Downloads/IPLogger-output.csv", sep='\t', skiprows=1)
    ips_arr = data2['Ip'].tolist()
    
    ips_without_dots_arr = []

    for ip in ips_arr:
      ip_without_dots = ip.replace('.', '') # Elimina los puntos de las ip
      ips_without_dots_arr.append(ip_without_dots)

      ip_without_dots_to_int = np.array(ips_without_dots_arr).astype(float)
      ip_without_dots_to_int_to_list = ip_without_dots_to_int.tolist()
    return ip_without_dots_to_int_to_list

if __name__ == "__main__":
    # Obtener la entrada del usuario para determinar el rango de enteros (1 a N)

    mensaje_metodo = "Seleccione una opción: \n(1) Ordenar array aleatorio \n(2) Organizar array desde archivo \n"
    metodo = input(mensaje_metodo)

    if metodo == "1":
        titulo = "Array aleatorio"
        N = int(input("Ingrese el número de enteros: "))
        A = [x + 1 for x in range(N)]
        random.seed(time.time())
        random.shuffle(A)
        titulo = "Ordenamiento por inserción"
        generador = orden_insercion(A)

        grafico(A, N, titulo, generador)

    elif metodo == "2":
        titulo = "Array desde archivo"
        A = extraer_array()
        N = len(A)
        titulo = "Ordenamiento por inserción"
        generador = orden_insercion(A)
        print(A)
        grafico(A, N, titulo, generador)
        

    else:
        print("Opción no válida")
        exit()
