# Remuneration Project

Este é um projeto Django para controle de remunerações com API RESTful, Swagger, testes Pytest e Docker.

---

## 📦 Tecnologias Utilizadas

* Python 3.10
* Django 4.2
* Django REST Framework
* drf-spectacular (Swagger)
* Pytest
* Docker / Docker Compose
* SQLite3 (banco de dados padrão)

---

## ⚙️ Instalação Local (sem Docker)

```bash
# 1. Clone o repositório
$ git clone https://github.com/alispnor/remuneration_project.git
$ cd remuneration_project

# 2. Crie e ative um ambiente virtual
$ python3 -m venv venv
$ source venv/bin/activate

# 3. Instale as dependências
$ pip install -r requirements.txt

# 4. Rode as migrações e o servidor
$ python manage.py migrate
$ python manage.py runserver
```

Acesse a API: [http://localhost:8000/docs/](http://localhost:8000/docs/)

---

## 🐳 Instalação com Docker

```bash
# Suba os containers
$ docker compose up --build
```

> O serviço estará disponível em [http://localhost:8000](http://localhost:8000)

---

## 🔍 Documentação Swagger

* Swagger: [http://localhost:8000/docs/](http://localhost:8000/docs/)
* OpenAPI JSON: [http://localhost:8000/schema/](http://localhost:8000/schema/)

---

## ✅ Rodar os Testes

```bash
pytest
or 
DJANGO_SETTINGS_MODULE=remuneration_project.settings pytest

```

---

## 📌 Lógicas de Negócio Importantes

1. **ISS (2%) é descontado automaticamente sobre `value` no model.**

2. **`nf_value` é calculado como:**

   `value - (iss + pis + cofins + csll)`

3. **Validação da porcentagem esperada:**

   ```python
   calc_percent = (value / net_value) * 100
   if calc_percent != percent_value:
       logger.warning("Percentual divergente: calculado=%.2f%%, esperado=%.2f%%", calc_percent, percent_value)
   ```

---

## 🧪 Estrutura de Testes

* `api/tests/test_models.py`: Testa a lógica de cálculo e validações.
* `api/tests/test_api.py`: Testa criação via API.

---

## 📁 Estrutura do Projeto

```bash
remuneration_project/
├── api/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests/
├── remuneration_project/
│   ├── settings.py
│   ├── urls.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```



---

Feito com 💙 por \[Ali Mohammed]
