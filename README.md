# 🎮 API REST - Biblioteca de Jogos

🔗 Repositório:
https://github.com/0f4el/Atividades-em-sala-CRUD.git

---

## 📌 Sobre o Projeto

Esta aplicação é uma **API RESTful** desenvolvida com **Python e Flask** para gerenciamento de uma biblioteca de jogos.

O sistema permite realizar operações completas de **CRUD (Create, Read, Update e Delete)** utilizando um banco de dados **SQLite**.

---

## 🚀 Tecnologias Utilizadas

* Python 3
* Flask
* SQLite3
* Curl (para testes via terminal)

---

## 📁 Estrutura do Projeto

```
Atividades-em-sala-CRUD/
│
├── app.py              # API principal (rotas e lógica CRUD)
├── init_db.py          # Script de criação do banco de dados
├── jogos.db            # Banco SQLite
├── requirements.txt    # Dependências do projeto
└── README.md           # Documentação
```

---

## ⚙️ Configuração do Ambiente

### 1. Clonar o repositório

```bash
git clone https://github.com/0f4el/Atividades-em-sala-CRUD.git
cd Atividades-em-sala-CRUD
```

---

### 2. Criar o ambiente virtual

```bash
python -m venv venv
```

---

### 3. Ativar o ambiente virtual

#### 🟦 Windows (CMD)

```bash
venv\Scripts\activate
```

#### 🟦 PowerShell

```bash
venv\Scripts\Activate.ps1
```

#### 🟩 Linux / Mac

```bash
source venv/bin/activate
```

---

### 4. Instalar as dependências

```bash
pip install -r requirements.txt
```


---

## 🗄️ Inicialização do Banco de Dados

Execute o script abaixo para criar o banco e popular com dados iniciais:

```bash
python init_db.py
```

---

## ▶️ Executando a API

```bash
python app.py
```

A aplicação estará disponível em:

```
http://localhost:5000
```

---

## 📡 Endpoints da API

| Método | Rota          | Descrição                  |
| ------ | ------------- | -------------------------- |
| GET    | `/jogos`      | Lista todos os jogos       |
| GET    | `/jogos/<id>` | Retorna um jogo específico |
| POST   | `/jogos`      | Cria um novo jogo          |
| PUT    | `/jogos/<id>` | Atualiza um jogo existente |
| DELETE | `/jogos/<id>` | Remove um jogo             |

---

## 🧪 Testes com CURL (Windows - CMD)

⚠️ No **CMD**, os comandos devem ser executados em **uma única linha**.

---

### 🔹 Listar todos os jogos

```bash
curl http://localhost:5000/jogos
```

---

### 🔹 Buscar jogo por ID

```bash
curl http://localhost:5000/jogos/1
```

---

### 🔹 Inserir novo jogo

```bash
curl -X POST http://localhost:5000/jogos -H "Content-Type: application/json" -d "{\"titulo\":\"Hollow Knight\",\"genero\":\"Metroidvania\",\"plataforma\":\"PC\",\"ano_lancamento\":2017,\"desenvolvedora\":\"Team Cherry\",\"preco\":46.99}"
```

---

### 🔹 Atualizar jogo

```bash
curl -X PUT http://localhost:5000/jogos/1 -H "Content-Type: application/json" -d "{\"titulo\":\"Zelda Atualizado\",\"genero\":\"Aventura\",\"plataforma\":\"Switch\",\"ano_lancamento\":2017,\"desenvolvedora\":\"Nintendo\",\"preco\":199.90}"
```

---

### 🔹 Remover jogo

```bash
curl -X DELETE http://localhost:5000/jogos/1
```

---

### 🔹 Teste de erro (ID inexistente)

```bash
curl http://localhost:5000/jogos/999
```

---

## 📊 Estrutura do Banco de Dados

Tabela: **jogos**

| Campo          | Tipo                         |
| -------------- | ---------------------------- |
| id             | INTEGER (PK, AUTO INCREMENT) |
| titulo         | TEXT                         |
| genero         | TEXT                         |
| plataforma     | TEXT                         |
| ano_lancamento | INTEGER                      |
| desenvolvedora | TEXT                         |
| preco          | REAL                         |

---

## ✅ Funcionalidades Implementadas

* ✔ Cadastro de jogos (POST)
* ✔ Listagem de jogos (GET)
* ✔ Busca por ID (GET)
* ✔ Atualização de dados (PUT)
* ✔ Remoção de registros (DELETE)
* ✔ Tratamento de erro (404)
* ✔ Respostas em JSON

---

## 🧠 Boas Práticas Aplicadas

* Uso de **queries parametrizadas** (segurança contra SQL Injection)
* Separação de responsabilidades (script de banco + API)
* Uso de **ambiente virtual (venv)**
* Uso de **requirements.txt**
* Adoção de **padrões REST**
* Retorno de **status HTTP adequados**

---

## 👨‍💻 Autor
Rafael Eloisio
---

## 📌 Observações

* Caso utilize PowerShell, use `curl.exe` no lugar de `curl`
* O banco de dados é criado automaticamente pelo script `init_db.py`

---
