import os
import tkinter as tk
import random
os.getcwd()


class MegaSena:
    def __init__(self, master):
        self.master = master
        self.master.title("Gerador de Números da Mega-Sena")
        self.master.geometry("300x200")

        self.label = tk.Label(self.master, text="Clique no botão para gerar números aleatórios")
        self.label.pack(pady=10)

        self.button = tk.Button(self.master, text="Gerar Números", command=self.gerar_numeros)
        self.button.pack()

        self.resultado = tk.Label(self.master, text="", font=("Arial", 18))
        self.resultado.pack(pady=10)

    def gerar_numeros(self):
        numeros = []
        while len(numeros) < 6:
            numero = random.randint(1, 60)
            if numero not in numeros:
                numeros.append(numero)
        numeros.sort()
        self.resultado.configure(text=str(numeros))


if __name__ == "__main__":
    root = tk.Tk()
    app = MegaSena(root)
    root.mainloop()


