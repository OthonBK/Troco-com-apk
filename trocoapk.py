import tkinter as tk

root = tk.Tk()
root.title("Calculadora de troco")

preco_label = tk.Label(root, text="Preço do item:")
preco_label.grid(row=0, column=0)

preco_entry = tk.Entry(root)
preco_entry.grid(row=0, column=1)

pago_label = tk.Label(root, text="Quantia paga:")
pago_label.grid(row=1, column=0)

pago_entry = tk.Entry(root)
pago_entry.grid(row=1, column=1)

def calcular_troco():
    preco = float(preco_entry.get())
    pago = float(pago_entry.get())

    troco = pago - preco
    troco = round(troco, 2)

    num_cedulas = [0, 0, 0, 0, 0, 0, 0]
    num_moedas = [0, 0, 0, 0, 0]

    for i in range(len(cedulas)):
        while troco >= cedulas[i]:
            troco -= cedulas[i]
            num_cedulas[i] += 1

    for i in range(len(moedas)):
        while troco >= moedas[i]:
            troco -= moedas[i]
            num_moedas[i] += 1

    resultado_label.config(text="O troco é:")
    cedulas_label.config(text="")
    moedas_label.config(text="")

    for i in range(len(cedulas)):
        if num_cedulas[i] > 0:
            cedulas_label.config(text=cedulas_label.cget("text") + f"{num_cedulas[i]} nota(s) de R${cedulas[i]:.2f}\n")

    for i in range(len(moedas)):
        if num_moedas[i] > 0:
            moedas_label.config(text=moedas_label.cget("text") + f"{num_moedas[i]} moeda(s) de R${moedas[i]:.2f}\n")

cedulas = [100, 50, 20, 10, 5, 2,]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

resultado_label = tk.Label(root, text="")
resultado_label.grid(row=2, column=0, columnspan=2)

cedulas_label = tk.Label(root, text="")
cedulas_label.grid(row=3, column=0, columnspan=2)

moedas_label = tk.Label(root, text="")
moedas_label.grid(row=4, column=0, columnspan=2)

calcular_troco_button = tk.Button(root, text="Calcular troco", command=calcular_troco)
calcular_troco_button.grid(row=5, column=0, columnspan=2)

root.mainloop()
