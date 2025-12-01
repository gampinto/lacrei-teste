# ✅ **README.md — Projeto Lacrei (Backend)**

## 📌 **Descrição do Projeto**

Este repositório implementa o backend de um sistema de gestão de profissionais e consultas, desenvolvido como parte do desafio técnico.
O objetivo do sistema é permitir que usuários autorizados realizem:

* CRUD de **Profissionais**
* CRUD de **Consultas**
* Autenticação via **JWT**
* Proteção de rotas
* Organização limpa da estrutura do projeto

Toda a API foi construída utilizando **Django** e **Django REST Framework**, seguindo boas práticas de arquitetura e segurança.

---

# 🏗 **Tecnologias Utilizadas**

* **Python 3.12**
* **Django**
* **Django REST Framework**
* **Django SimpleJWT**
* **SQLite ou PostgreSQL (dependendo da configuração)**
* **Docker + Docker Compose (opcional)**

---

# 📁 **Estrutura do Projeto**

```
project/
│
├── api/
│   ├── settings.py
│   ├── urls.py
│   ├── permissions.py
│   └── ...
│
├── core/
│   ├── settings.py
│   ├── views.py
│   └── ...
│
├── manage.py
└── requirements.txt
```

Tudo separado em módulos limpos, cada um com responsabilidade única, seguindo boas práticas de organização.

---

# ⚙️ **Instalação e Execução**

## 🔹 1. Clonar o repositório

```
git clone https://github.com/gampinto/lacrei-teste.git
cd lacrei-teste
```

## 🔹 2. Criar e ativar um ambiente virtual

```
python -m venv venv
source venv/bin/activate   # Linux
venv\Scripts\activate      # Windows
```

## 🔹 3. Instalar dependências

```
pip install -r requirements.txt
```

## 🔹 4. Rodar migrações

```
python manage.py migrate
```

## 🔹 5. Criar superusuário

```
python manage.py createsuperuser
```

## 🔹 6. Rodar o servidor

```
python manage.py runserver
```

API disponível em:

```
http://127.0.0.1:8000/api/

```
## 🔹 7. Criar o logs.
O Arquivo logs.txt deve ser colocado na raiz do projeto. O Software é programado para registrar nele os erros.

```

---

# 🔐 **Autenticação (JWT)**

Antes de acessar qualquer rota protegida, gere um token de acesso. Este foi o mecanismo de segurança utilizado para evitar SQL Injections e garantindo a integridade, confiabilidade e disponibilidade: os três pilares da segurança da informação!

## 📥 **Gerar token**

POST →

```
http://127.0.0.1:8000/api/token/
utilize o superusuario Django.

  "access": "TOKEN_AQUI",
  "refresh": "TOKEN_REFRESH"

## ✔ Como usar o token

Enviar no header:

```
Authorization: Bearer SEU_TOKEN
```
Para todos os códigos de consulta, o token será necessário.
---

# 📚 **Documentação das Rotas da API**

## ▶ **Profissionais**

### 🔹 Listar profissionais

GET

```
/api/profissionais/
```

### 🔹 Criar profissional

POST

```
/api/profissionais/
```

{
  "nome_social": "Maria Souza",
  "profissao": "Psicóloga",
  "endereco": "Rua A, 123",
  "contato": "11 99999-0000"
}
```

### 🔹 Obter profissional pelo ID 

GET

```
/api/profissionais/<id>/
```

### 🔹 Atualizar profissional

PUT/PATCH

```
/api/profissionais/<id>/
```

### 🔹 Deletar profissional

DELETE

```
/api/profissionais/<id>/
```

---

## ▶ **Consultas**

### 🔹 Listar consultas

GET

```
/api/consultas/
```

### 🔹 Criar consulta

POST

```
/api/consultas/
```

Body:

{
  "profissional": 1,
  "data": "2025-12-01",
  "hora": "14:00",
  "paciente": "João Silva",
  "descricao": "Primeiro atendimento"
}

### 🔹 Atualizar consulta

PUT/PATCH

```
/api/consultas/<id>/
```

### 🔹 Deletar consulta

DELETE

```
/api/consultas/<id>/
```
Todas as funções de CRUD ficarão desativadas, isso é a evidência de funcionamento do sistema de segurança implementado com JWT. Para desativar o mecanismo de segurança e testar o CRUD facilmente pelo navegador, troque a linha:
" "rest_framework.permissions.IsAuthenticated","
por:
" 'rest_framework.permissions.AllowAny', "
As áspas são necessárias.

--------------------------------------

Caso queira testar como os CRUDs funcionam mesmo com a segunraça JWT, utilize os seguintes códigos no seu gitbash:

1) LISTAR PROFISSIONAIS:
curl -X GET http://127.0.0.1:8000/api/profissionais/ \
-H "Authorization: Bearer SEU_TOKEN_AQUI"

2) CRIAR PROFISSIONAL:
curl -X POST http://127.0.0.1:8000/api/profissionais/ \
-H "Content-Type: application/json" \
-H "Authorization: Bearer SEU_TOKEN_AQUI" \
-d "{
    \"nome_social\": \"Ana Pereira\",
    \"profissao\": \"Psicologa\",
    \"endereco\": \"Rua B, 456\",
    \"contato\": \"(21) 98888-7777\"
}"

3) LER UM PROFISSIONAL ATRAVÉS DO ID (substitua o ID):
curl -X GET http://127.0.0.1:8000/api/profissionais/1/ \
-H "Authorization: Bearer SEU_TOKEN_AQUI"

4) ATUALIZAR UM PROFISSIONAL:
curl -X PUT http://127.0.0.1:8000/api/profissionais/1/ \
-H "Content-Type: application/json" \
-H "Authorization: Bearer SEU_TOKEN_AQUI" \
-d "{
    \"nome_social\": \"Ana P. Almeida\",
    \"profissao\": \"Psicóloga Clínica\",
    \"endereco\": \"Rua Nova, 789\",
    \"contato\": \"(21) 97777-2222\"
}"

5) DELETAR UM PROFISSIONAL (substitua o ID /1/ pelo correspondente)
curl -X DELETE http://127.0.0.1:8000/api/profissionais/1/ \
-H "Authorization: Bearer SEU_TOKEN_AQUI"

6) LISTAR CONSULTAS:
curl -X GET http://127.0.0.1:8000/api/consultas/ \
-H "Authorization: Bearer SEU_TOKEN_AQUI"

7) CRIAR CONSULTA:
curl -X POST http://127.0.0.1:8000/api/consultas/ \
-H "Content-Type: application/json" \
-H "Authorization: Bearer SEU_TOKEN_AQUI" \
-d "{
    \"profissional\": 1,
    \"data\": \"2024-05-20\",
    \"hora\": \"14:30\",
    \"paciente\": \"João da Silva\",
    \"descricao\": \"Avaliação inicial\"
}"

8) LER CONSULTA ESPECÍFICA: (Troque o ID)
curl -X GET http://127.0.0.1:8000/api/consultas/1/ \
-H "Authorization: Bearer SEU_TOKEN_AQUI"

9) ATUALIZAR CONSULTA (Troque o ID):
curl -X PUT http://127.0.0.1:8000/api/consultas/1/ \
-H "Content-Type: application/json" \
-H "Authorization: Bearer SEU_TOKEN_AQUI" \
-d "{
    \"profissional\": 1,
    \"data\": \"2024-05-22\",
    \"hora\": \"15:00\",
    \"paciente\": \"João da Silva\",
    \"descricao\": \"Retorno\"
}"

10) DELETAR CONSULTA (Troque o ID)
curl -X DELETE http://127.0.0.1:8000/api/consultas/1/ \
-H "Authorization: Bearer SEU_TOKEN_AQUI"

IMPORTANTE: Algumas versões podem provocar erros no uso de qualquer caracter especial.
---

# 📌 **Boas Práticas Utilizadas**

### ✅ **1. Arquitetura organizada**

Cada módulo isolado por responsabilidade, facilitando manutenção e escalabilidade.

### ✅ **2. Código limpo**

* Nomeração clara
* Separação de camadas
* Uso correto de serializers e views
* DRF com ViewSets e URLs organizadas

### ✅ **3. Segurança**

* Autenticação JWT
* Todas rotas de CRUD protegidas
* Sem exposição de dados sensíveis
* Uso de permissões customizadas quando necessário

### ✅ **4. CORS configurado para desenvolvimento**

Permite que o futuro front-end consuma a API.

### ✅ **5. Uso de ambiente virtual**

Evita conflitos de versões e padroniza o ambiente de desenvolvimento.

---

# 🧪 **Testes de API**

O projeto pode ser testado via:

* Insomnia
* Postman
* curl no terminal

---

# 🚀 **Próximos Passos (Front-end)**

O front-end será implementado posteriormente, com:

* Página inicial
* CRUD completo em 4 telas para cada módulo
* Requisições utilizando `fetch()`
* Token salvo diretamente no navegador
* Interface simples e direta, adaptada para ser utilizada por um simples secretário.

---

# 📄 **Licença**

Projeto entregue exclusivamente para fins avaliativos do desafio técnico. Considere domínio público.

---