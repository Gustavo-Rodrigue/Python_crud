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
<<<<<<< HEAD



🧩 Tela de Login

<img width="400" height="200" alt="Captura de tela 2025-10-21 110832" src="https://github.com/user-attachments/assets/e1259e0f-6c30-406f-ae1b-9f0d665326f8" />

<img width="400" height="200" alt="Captura de tela 2025-10-21 110852" src="https://github.com/user-attachments/assets/f48bd875-31da-46b6-8b35-6dc2d577456c" />

🏠 Tela Principal

<img width="400" height="200" alt="Captura de tela 2025-10-21 110907" src="https://github.com/user-attachments/assets/f68570a4-6a9c-4bf0-940a-040932665304" />

📦 Tela de Estoque

<img width="400" height="200" alt="Captura de tela 2025-10-21 110935" src="https://github.com/user-attachments/assets/d5358240-abe3-492c-81ce-d9534b932472" />

<img width="400" height="200" alt="Captura de tela 2025-10-21 110946" src="https://github.com/user-attachments/assets/e8345191-743c-4678-9f7b-b726220f34e6" />

<img width="400" height="200" alt="Captura de tela 2025-10-21 111005" src="https://github.com/user-attachments/assets/d50311d1-d956-45ac-9ae3-97c057fd14f2" />

<img width="400" height="200" alt="Captura de tela 2025-10-21 111014" src="https://github.com/user-attachments/assets/5fc9640c-9903-46bb-8cf1-50cbbc792cf6" />

<img width="400" height="200" alt="Captura de tela 2025-10-21 111025" src="https://github.com/user-attachments/assets/f206c0fe-c0bc-4700-804b-f916c2de2196" />

🍛 Tela de Cadastro de Comidas

<img width="400" height="200" alt="Captura de tela 2025-10-21 111048" src="https://github.com/user-attachments/assets/3321f9d7-e72f-4d52-8d76-5b55b37ba39e" />

<img width="400" height="200" alt="Captura de tela 2025-10-21 111041" src="https://github.com/user-attachments/assets/ed2fda0e-00bd-49c3-aa83-8d409ebbffe4" />

<img width="400" height="200" alt="Captura de tela 2025-10-21 111130" src="https://github.com/user-attachments/assets/8da7a496-5e0b-4534-905b-b7bb569ef851" />

<img width="400" height="200" alt="Captura de tela 2025-10-21 111137" src="https://github.com/user-attachments/assets/fc1761a9-77a0-4180-9b0b-1fefdafb70a1" />

<img width="400" height="200" alt="Captura de tela 2025-10-21 111147" src="https://github.com/user-attachments/assets/39583541-8501-4508-87e3-19e9f77ee215" />

<img width="400" height="200" alt="Captura de tela 2025-10-21 111200" src="https://github.com/user-attachments/assets/bcc40009-571b-4720-9ea6-1219590c1fc7" />

<img width="400" height="200" alt="Captura de tela 2025-10-21 111217" src="https://github.com/user-attachments/assets/563f4fb3-afc0-4419-a545-2ebcca737a01" />

