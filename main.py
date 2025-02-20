import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        entrada = caixa_entrada.get()
        if "/ 0" in entrada or entrada.endswith("/0"):  
            raise ZeroDivisionError
        resultado = eval(entrada)
        caixa_entrada.delete(0, tk.END)
        caixa_entrada.insert(tk.END, str(resultado))
    except ZeroDivisionError:
        messagebox.showerror
        caixa_entrada.delete(0, tk.END)
    except Exception:
        messagebox.showerror
        caixa_entrada.delete(0, tk.END)

def adicionar_texto(texto):
    caixa_entrada.insert(tk.END, texto)

def apagar():
    caixa_entrada.delete(0, tk.END)

app = tk.Tk()
app.title("Calculadora")
app.configure(bg='#b0e0e6')
app.geometry('350x400')
app.resizable(False, False)

frame = tk.Frame(app, bg='#b0e0e6')
frame.pack(expand=True, fill='both', padx=10, pady=10)

caixa_entrada = tk.Entry(frame, bg='white', fg='black', font=('Arial', 30), bd=5, insertbackground='black', justify='right')
caixa_entrada.grid(row=0, column=0, columnspan=4, padx=5, pady=20, sticky='we')

botoes = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('*', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('/', 4, 3)
]

for texto, linha, coluna in botoes:
    comando = apagar if texto == 'C' else calcular if texto == '=' else lambda t=texto: adicionar_texto(t)
    tk.Button(frame, text=texto, width=5, height=2, command=comando, bg='#87CEEB', fg='black', font=('Arial', 12, 'bold'))\
        .grid(row=linha, column=coluna, padx=3, pady=3, sticky='nsew')

for i in range(5):
    frame.grid_rowconfigure(i, weight=1)
for j in range(4):
    frame.grid_columnconfigure(j, weight=1)

app.mainloop()
