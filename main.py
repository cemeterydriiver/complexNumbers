import tkinter as tk
from tkinter import ttk, messagebox

def somar():
    try:
        real1 = float(entry_real1.get())
        imag1 = float(entry_imag1.get())
        num1 = complex(real1, imag1)

        real2 = float(entry_real2.get())
        imag2 = float(entry_imag2.get())
        num2 = complex(real2, imag2)

        resultado = num1 + num2
        messagebox.showinfo("Resultado", f"Resultado da adição: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

def subtrair():
    try:
        real1 = float(entry_real1.get())
        imag1 = float(entry_imag1.get())
        num1 = complex(real1, imag1)

        real2 = float(entry_real2.get())
        imag2 = float(entry_imag2.get())
        num2 = complex(real2, imag2)

        resultado = num1 - num2
        messagebox.showinfo("Resultado", f"Resultado da subtração: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

def multiplicar():
    try:
        real1 = float(entry_real1.get())
        imag1 = float(entry_imag1.get())
        num1 = complex(real1, imag1)

        real2 = float(entry_real2.get())
        imag2 = float(entry_imag2.get())
        num2 = complex(real2, imag2)

        resultado = num1 * num2
        messagebox.showinfo("Resultado", f"Resultado da multiplicação: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

def dividir():
    try:
        real1 = float(entry_real1.get())
        imag1 = float(entry_imag1.get())
        num1 = complex(real1, imag1)

        real2 = float(entry_real2.get())
        imag2 = float(entry_imag2.get())
        num2 = complex(real2, imag2)

        denominador_conjugado = num2.conjugate()
        numerador = num1 * denominador_conjugado
        denominador = num2 * denominador_conjugado

        resultado = numerador / denominador
        messagebox.showinfo("Resultado", f"Resultado da divisão: {resultado}")
    except (ValueError, ZeroDivisionError):
        messagebox.showerror("Erro", "Entrada inválida ou divisão por zero!")

window = tk.Tk()
window.title("Calculadora de Números Complexos")

style = ttk.Style()
style.configure("TLabel",
                padding=10,
                font=("Arial", 12))

style.configure("TEntry",
                padding=10,
                font=("Arial", 12))

style.configure("TButton",
                background="#8ecae6",
                padding=10,
                relief="raised",
                font=("Arial", 12, "bold"))

frame = ttk.Frame(window, padding=20)
frame.grid(row=0, column=0, sticky="nsew")

label_real1 = ttk.Label(frame, text="Parte real do primeiro número:")
label_real1.grid(row=0, column=0, sticky="w")
entry_real1 = ttk.Entry(frame)
entry_real1.grid(row=0, column=1)

label_imag1 = ttk.Label(frame, text="Parte imaginária do primeiro número:")
label_imag1.grid(row=1, column=0, sticky="w")
entry_imag1 = ttk.Entry(frame)
entry_imag1.grid(row=1, column=1)

label_real2 = ttk.Label(frame, text="Parte real do segundo número:")
label_real2.grid(row=2, column=0, sticky="w")
entry_real2 = ttk.Entry(frame)
entry_real2.grid(row=2, column=1)

label_imag2 = ttk.Label(frame, text="Parte imaginária do segundo número:")
label_imag2.grid(row=3, column=0, sticky="w")
entry_imag2 = ttk.Entry(frame)
entry_imag2.grid(row=3, column=1)

button_adicao = ttk.Button(frame, text="Adição", command=somar)
button_adicao.grid(row=4, column=0, pady=10, sticky="we")

button_subtracao = ttk.Button(frame, text="Subtração", command=subtrair)
button_subtracao.grid(row=4, column=1, pady=10, sticky="we")

button_multiplicacao = ttk.Button(frame, text="Multiplicação", command=multiplicar)
button_multiplicacao.grid(row=5, column=0, pady=10, sticky="we")

button_divisao = ttk.Button(frame, text="Divisão", command=dividir)
button_divisao.grid(row=5, column=1, pady=10, sticky="we")

window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

frame.columnconfigure(1, weight=1)
frame.rowconfigure(4, weight=1)

window.mainloop()
