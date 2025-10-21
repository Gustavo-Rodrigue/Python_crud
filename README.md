# 🍲 Controle de Estoque de Comidas Nordestinas

Um sistema completo de **CRUD em Python** com interface gráfica feita em **Tkinter + ttk**, projetado para gerenciar o estoque de comidas típicas nordestinas.  
O projeto combina simplicidade e estética moderna para facilitar o controle de produtos, com login, banco de dados local e interface amigável.

---

## ✨ Funcionalidades

- 🔐 **Autenticação de Usuário** — login seguro com persistência local.  
- 🍛 **Cadastro de Comidas** — adicione, edite e remova pratos típicos.  
- 📦 **Gestão de Estoque** — controle entradas e saídas de produtos.  
- 🧾 **Banco de Dados SQLite** — criação automática via `ensuredb()`.  
- 🎨 **Interface Moderna (Dark Mode)** — layout limpo, responsivo e temático.  

---

## 🧱 Estrutura do Projeto

```
📦 Python_crud/
├── main.py          # Interface principal e tela inicial
├── db.py            # Inicialização e manipulação do banco SQLite
├── login.py         # Tela de login e autenticação
├── comidas.py       # Cadastro de comidas típicas
├── estoque.py       # Gestão de estoque (entradas e saídas)
├── utils.py         # Funções auxiliares (centralizar janela, etc)
└── assets/          # Ícones e recursos visuais (opcional)
```

---

## 🚀 Como Executar

### 🔧 1. Pré-requisitos

Tenha o **Python 3.8+** instalado:

```bash
python --version
```

Instale as dependências (Tkinter geralmente já vem junto com o Python):

```bash
pip install pillow
```

> 💡 *No Linux, se necessário:*
> ```bash
> sudo apt install python3-tk
> ```

---

### ▶️ 2. Executando o Sistema

Após extrair o projeto:

```bash
cd Python_crud
python main.py
```

---

## 💻 Telas do Sistema

### 🏠 Tela de Login
Permite o acesso seguro ao sistema, validando credenciais.

### 📦 Tela Principal
Exibe as opções de navegação (Comidas, Estoque, Sair) com visual moderno.

### 🍛 Cadastro de Comidas
Interface amigável para registrar e editar pratos.

### 📊 Gestão de Estoque
Controle completo de quantidades, entradas e saídas de produtos.

---

## 🧑‍💻 Tecnologias Utilizadas

| Categoria | Ferramenta |
|------------|-------------|
| Linguagem | 🐍 Python 3 |
| Interface | Tkinter + ttk.Style |
| Banco de Dados | SQLite3 |
| Design | Dark Mode temático |
| Organização | Estrutura modular (MVC simplificado) |

---

## 🎨 Estilo Visual

- **Tema:** “Dark Mode Nordestino”  
- **Cores principais:**  
  - Fundo: `#1E1E1E`  
  - Destaque: `#E07B39`  
  - Ação (hover): `#FF8C42`  
- **Fonte:** `Segoe UI`  
- **Layout:** Centralizado, com ícones e tipografia moderna  

---



## 🖼️ Demonstração do Sistema

A seguir estão as capturas de tela que ilustram o funcionamento completo do sistema:

![Captura de tela 2025-10-21 110832.png](Fotos/Captura de tela 2025-10-21 110832.png)

![Captura de tela 2025-10-21 110852.png](Fotos/Captura de tela 2025-10-21 110852.png)

![Captura de tela 2025-10-21 110907.png](Fotos/Captura de tela 2025-10-21 110907.png)

![Captura de tela 2025-10-21 110935.png](Fotos/Captura de tela 2025-10-21 110935.png)

![Captura de tela 2025-10-21 110946.png](Fotos/Captura de tela 2025-10-21 110946.png)

![Captura de tela 2025-10-21 111005.png](Fotos/Captura de tela 2025-10-21 111005.png)

![Captura de tela 2025-10-21 111014.png](Fotos/Captura de tela 2025-10-21 111014.png)

![Captura de tela 2025-10-21 111025.png](Fotos/Captura de tela 2025-10-21 111025.png)

![Captura de tela 2025-10-21 111041.png](Fotos/Captura de tela 2025-10-21 111041.png)

![Captura de tela 2025-10-21 111048.png](Fotos/Captura de tela 2025-10-21 111048.png)

![Captura de tela 2025-10-21 111130.png](Fotos/Captura de tela 2025-10-21 111130.png)

![Captura de tela 2025-10-21 111137.png](Fotos/Captura de tela 2025-10-21 111137.png)

![Captura de tela 2025-10-21 111147.png](Fotos/Captura de tela 2025-10-21 111147.png)

![Captura de tela 2025-10-21 111200.png](Fotos/Captura de tela 2025-10-21 111200.png)

![Captura de tela 2025-10-21 111217.png](Fotos/Captura de tela 2025-10-21 111217.png)

## 🧩 Roadmap

- [ ] Adicionar relatórios em PDF (estoque e movimentações)  
- [ ] Implementar cadastro de usuários com níveis de acesso  
- [ ] Criar interface de pesquisa e filtros  
- [ ] Exportar dados para Excel/CSV  

---

## 👨‍🍳 Autor

**Desenvolvido com carinho por [Seu Nome]**  
💬 *Inspirado na cultura e sabor das comidas nordestinas do Brasil.*  

📧 Contato: [seu.email@exemplo.com]  
🌐 GitHub: [https://github.com/seuusuario](https://github.com/seuusuario)

---

## 🪪 Licença

Este projeto está licenciado sob a **MIT License** — sinta-se à vontade para usar, modificar e distribuir.

---

### 🖤 “Tecnologia com sabor de cultura nordestina.” 🌵
