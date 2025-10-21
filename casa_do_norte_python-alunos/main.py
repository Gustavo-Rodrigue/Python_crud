import tkinter as tk
from tkinter import ttk

# Importa funções auxiliares
from db import ensuredb
from utils import centralizarjanela
from login import showlogin
from comidas import showcomidas
from estoque import showgestaoestoque


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🍲 Controle de Estoque: Comidas Nordestinas")
        self.configure(bg="#1E1E1E")

        # Inicializa banco
        ensuredb()
        self.currentuser = None

        # Centraliza janela inicial
        centralizarjanela(self, 400, 250)

        # Aplica tema moderno
        self._configurar_estilo()

        # Exibe tela de login
        showlogin(self)

    # ----------------------#
    # Estilos e cores       #
    # ----------------------#
    def _configurar_estilo(self):
        style = ttk.Style(self)
        style.theme_use("clam")

        # 🎨 Paleta de cores
        CORES = {
            "fundo": "#1E1E1E",
            "painel": "#252526",
            "texto": "#F3F3F3",
            "texto_sec": "#BBBBBB",
            "botao": "#E07B39",
            "botao_hover": "#FF8C42",
            "botao_menu": "#A64208",
            "botao_menu_hover": "#C95B0C"
        }

        self.configure(bg=CORES["fundo"])

        # Frames
        style.configure("TFrame", background=CORES["painel"])

        # Labels
        style.configure(
            "TLabel",
            background=CORES["painel"],
            foreground=CORES["texto"],
            font=("Segoe UI", 11)
        )

        # Botões principais
        style.configure(
            "TButton",
            font=("Segoe UI", 10, "bold"),
            padding=(10, 6),
            background=CORES["botao"],
            foreground="white",
            borderwidth=0,
            relief="flat"
        )
        style.map(
            "TButton",
            background=[("active", CORES["botao_hover"])],
            foreground=[("disabled", "#999999")]
        )

        # Botões do menu superior
        style.configure(
            "Menu.TButton",
            background=CORES["botao_menu"],
            foreground="white",
            font=("Segoe UI", 10, "bold"),
            padding=(10, 6),
            borderwidth=0,
            relief="flat"
        )
        style.map(
            "Menu.TButton",
            background=[("active", CORES["botao_menu_hover"])]
        )

        # Label do topo (usuário)
        style.configure(
            "User.TLabel",
            background=CORES["painel"],
            foreground="#FFD580",
            font=("Segoe UI Semibold", 11)
        )

        # Guarda paleta no objeto para reutilizar
        self.CORES = CORES

    # ----------------------#
    # Tela principal (pós-login)
    # ----------------------#
    def showmain(self):
        # Limpa widgets anteriores
        for w in self.winfo_children():
            w.destroy()

        # Expande janela
        centralizarjanela(self, 1000, 550)
        self.configure(bg=self.CORES["fundo"])

        # Painel superior
        top = ttk.Frame(self, padding=10)
        top.pack(fill="x")

        ttk.Label(
            top,
            text=f"👤 Usuário logado: {self.currentuser.get('nome_completo', '')}",
            style="User.TLabel"
        ).pack(side="left")

        ttk.Button(top, text="Sair", style="Menu.TButton",
                   command=lambda: showlogin(self)).pack(side="right", padx=5)

        ttk.Button(top, text="Cadastro de Comidas", style="Menu.TButton",
                   command=lambda: showcomidas(self)).pack(side="right", padx=5)

        ttk.Button(top, text="Gestão de Estoque", style="Menu.TButton",
                   command=lambda: showgestaoestoque(self)).pack(side="right", padx=5)

        # Frame central (conteúdo)
        center = ttk.Frame(self, padding=50)
        center.pack(expand=True)

        msg = (
            f"Olá, {self.currentuser.get('nome_completo', '')} 👋\n\n"
            "Bem-vindo ao sistema de **Controle de Estoque de Comidas Nordestinas**.\n\n"
            "Aqui você pode:\n"
            " 🍛 Cadastrar novos pratos e comidas típicas\n"
            " 📦 Consultar e editar o estoque\n"
            " ➕ Registrar entradas e saídas\n\n"
            "Selecione uma opção no menu superior para começar!"
        )

        tk.Label(
            center,
            text=msg,
            font=("Segoe UI", 14),
            justify="left",
            bg=self.CORES["fundo"],
            fg=self.CORES["texto_sec"],
            wraplength=800
        ).pack()

        # Rodapé simples
        footer = ttk.Frame(self, padding=10)
        footer.pack(side="bottom", fill="x")
        ttk.Label(
            footer,
            text="🍴 Sistema desenvolvido para gestão de Comidas Nordestinas — v1.0",
            foreground="#777777",
            background=self.CORES["painel"],
            font=("Segoe UI", 9)
        ).pack(side="right")


# -------------------------------------------#
# Ponto de entrada do programa (main script) #
# -------------------------------------------#
if __name__ == "__main__":
    app = App()
    app.mainloop()
