import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Preços dos produtos
precos = {
    "açai": 8.00,
    "casquinha": 2.00,
    "churros": 1.50,
    "sorvete": 7.00,
    "pote": 5.00,
    "milkshake": 7.00,
    "cupcake": 1.50,
    "picolé": 1.50,
    "brownie": 1.50,
    "refresco": 1.00,
    "Suco": 1.50
}

# Função para calcular o total
def calcular_total():
    total = 0
    for item, preco in precos.items():
        quantidade = int(quantidade_vars[item].get())
        total += quantidade * preco
    total_var.set(f"R${total:.2f}")

# Função para calcular o troco
def calcular_troco():
    try:
        total = float(total_var.get().replace("R$", ""))
        valor_pago = float(valor_pago_var.get())
        if valor_pago >= total:
            troco = valor_pago - total
            troco_var.set(f"R${troco:.2f}")
        else:
            messagebox.showwarning("Aviso", "Valor pago é insuficiente para cobrir o total.")
            troco_var.set("R$0.00")
    except ValueError:
        messagebox.showerror("Erro", "Insira um valor válido para o pagamento.")

# Configuração da janela principal
root = tk.Tk()
root.title("Sistema de Sorveteria")
root.geometry("600x700")
root.configure(bg="#eaf4fc")

# Criação de um frame rolável
canvas = tk.Canvas(root, bg="#eaf4fc")
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="#eaf4fc")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Variáveis de interface
quantidade_vars = {item: tk.StringVar(value="0") for item in precos}
total_var = tk.StringVar(value="R$0.00")
valor_pago_var = tk.StringVar(value="0")
troco_var = tk.StringVar(value="R$0.00")

# Título
titulo = tk.Label(scrollable_frame, text="Sistema de Sorveteria", font=("Helvetica", 24, "bold"), bg="#eaf4fc", fg="#007bff")
titulo.pack(pady=15)

# Formulário de produtos
form_frame = tk.Frame(scrollable_frame, bg="#eaf4fc")
form_frame.pack(pady=15)

for item, preco in precos.items():
    item_label = tk.Label(form_frame, text=f"{item.capitalize()} (R${preco:.2f}):", font=("Helvetica", 12, "bold"), bg="#eaf4fc", fg="#0d6efd")
    item_label.grid(row=list(precos.keys()).index(item), column=0, sticky="w", padx=5, pady=5)
    item_entry = tk.Entry(form_frame, textvariable=quantidade_vars[item], font=("Helvetica", 12), width=5, justify="center", relief="solid", bd=1)
    item_entry.grid(row=list(precos.keys()).index(item), column=1, padx=10)

# Botão para calcular o total
calcular_button = tk.Button(scrollable_frame, text="Calcular Total", font=("Helvetica", 12, "bold"), bg="#007bff", fg="white", command=calcular_total, relief="solid", bd=1)
calcular_button.pack(pady=15)

# Resultado do total
total_label = tk.Label(scrollable_frame, text="Total:", font=("Helvetica", 14, "bold"), bg="#eaf4fc", fg="#000")
total_label.pack()
total_display = tk.Label(scrollable_frame, textvariable=total_var, font=("Helvetica", 14), bg="#eaf4fc", fg="#28a745")
total_display.pack()

# Seção de pagamento e troco
troco_frame = tk.Frame(scrollable_frame, bg="#eaf4fc")
troco_frame.pack(pady=20)

valor_pago_label = tk.Label(troco_frame, text="Valor Pago:", font=("Helvetica", 12, "bold"), bg="#eaf4fc", fg="#0d6efd")
valor_pago_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
valor_pago_entry = tk.Entry(troco_frame, textvariable=valor_pago_var, font=("Helvetica", 12), width=10, justify="center", relief="solid", bd=1)
valor_pago_entry.grid(row=0, column=1, padx=10)

# Botão para calcular o troco
troco_button = tk.Button(scrollable_frame, text="Calcular Troco", font=("Helvetica", 12, "bold"), bg="#007bff", fg="white", command=calcular_troco, relief="solid", bd=1)
troco_button.pack(pady=15)

# Resultado do troco
troco_label = tk.Label(scrollable_frame, text="Troco:", font=("Helvetica", 14, "bold"), bg="#eaf4fc", fg="#000")
troco_label.pack()
troco_display = tk.Label(scrollable_frame, textvariable=troco_var, font=("Helvetica", 14), bg="#eaf4fc", fg="#28a745")
troco_display.pack()

# Executando a aplicação
root.mainloop()
