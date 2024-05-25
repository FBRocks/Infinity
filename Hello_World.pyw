import tkinter as tk
from tkinter import ttk

class HelloWorld:
    def __init__(self, root):
        self.root = root
        self.root.title("Hello World")

        largura_janela = 350
        altura_janela = 100
        largura_tela = root.winfo_screenwidth()
        altura_tela = root.winfo_screenheight()
        x = (largura_tela - largura_janela) // 2
        y = (altura_tela - altura_janela) // 2
        self.root.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")

        self.label_mensagem = ttk.Label(root, text="", font=("Helvetica", 14))
        self.label_mensagem.pack(pady=10)

        self.botao_hello = ttk.Button(root, text="Hello World", command=self.exibir_mensagem)
        self.botao_hello.pack(pady=10)

    def exibir_mensagem(self):
        self.label_mensagem.config(text="Hello World")

if __name__ == "__main__":
    root = tk.Tk()
    app = HelloWorld(root)
    root.mainloop()