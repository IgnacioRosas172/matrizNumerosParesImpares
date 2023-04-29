#Ejercicio 2 matriz 3x2

import tkinter as tk


def numeros_pares_impares(matriz):
    numeros_pares = 0
    numeros_impares = 0

    for row in matriz:
        for elem in row:
            if elem%2 == 0:
                numeros_pares +=1
            else:
                numeros_impares +=1
    return numeros_pares, numeros_impares

def salida():
    root = tk.Tk()
    root.quit()

def obtener_numeros():
    matrix = [[0 for j in range(2)] for i in range(3)]
    for i in range(3):
        for j in range(2):
            try:
                num = int(entries[i][j].get())
                matrix[i][j] = num
            except ValueError:
                label_result.config(text="Por favor, ingrese solo números enteros")
                return

    numeros_pares, numeros_impares = numeros_pares_impares(matrix)
    label_result.config(text=f"Hay {numeros_pares} números pares y {numeros_impares} números impares en la matriz")

window = tk.Tk()
window.title("Números pares e impares en una matriz")

labels = []
entries = []

for i in range(3):
    row_labels = []
    row_entries = []
    for j in range(2):
        label = tk.Label(text=f"Número {i+1},{j+1}:")
        label.grid(row=i, column=j*2, padx=5, pady=5)
        entry = tk.Entry()
        entry.grid(row=i, column=j*2+1, padx=5, pady=5)
        row_labels.append(label)
        row_entries.append(entry)
    labels.append(row_labels)
    entries.append(row_entries)

button_count = tk.Button(text="Contar", bg="#009186", command=obtener_numeros)
button_count.grid(row=3, column=1, pady=10)
button_salir = tk.Button(text = "Salir", bg="#ff0000", command =salida)
button_salir.grid(row=3, column=3, pady=10)


label_result = tk.Label()
label_result.grid(row=4, column=0, columnspan=3, pady=10)

window.mainloop()
