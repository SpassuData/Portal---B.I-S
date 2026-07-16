# Portal B.I-S

Aplicação web que consolida, em um único lugar, os links dos principais dashboards de BI usados no dia a dia da equipe.

## 📋 Sobre o projeto

O **Portal B.I-S** nasce da necessidade de centralizar o acesso aos diversos dashboards de Business Intelligence espalhados pela organização, evitando a dispersão de links e facilitando a navegação da equipe entre os relatórios utilizados com mais frequência.

## 🚀 Tecnologias

- **Python** / **Django** — back-end e regras de negócio
- **HTML** (templates Django) — camada de apresentação
- **SQLite** — banco de dados (`db.sqlite3`)

## 📁 Estrutura do projeto

```
Portal---B.I-S/
├── core/            # Configurações principais do projeto Django (settings, urls, wsgi/asgi)
├── portal_bi/        # Aplicação principal (models, views, lógica do portal)
├── templates/         # Templates HTML das páginas
├── db.sqlite3         # Banco de dados local
├── manage.py           # Script de gerenciamento do Django
└── requeriments.txt    # Dependências do projeto
```

## ⚙️ Como rodar o projeto localmente

### Pré-requisitos

- Python 3.10+ instalado
- pip

### Passo a passo

1. Clone o repositório
   ```bash
   git clone https://github.com/SpassuData/Portal---B.I-S.git
   cd Portal---B.I-S
   ```

2. Crie e ative um ambiente virtual
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. Instale as dependências
   ```bash
   pip install -r requeriments.txt
   ```
   > ⚠️ O arquivo `requeriments.txt` está vazio no momento. Adicione aqui as dependências do projeto (ex.: `Django`) assim que definidas.

4. Aplique as migrações
   ```bash
   python manage.py migrate
   ```

5. Rode o servidor de desenvolvimento
   ```bash
   python manage.py runserver
   ```

6. Acesse [http://127.0.0.1:8000/](http://127.0.0.1:8000/) no navegador.

## 🗺️ Roadmap

- [ ] Cadastro e organização dos dashboards por categoria
- [ ] Autenticação de usuários
- [ ] Área administrativa para gerenciar links
- [ ] Documentar dependências em `requeriments.txt`

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/minha-feature`)
3. Commit suas alterações (`git commit -m 'Adiciona minha feature'`)
4. Faça push para a branch (`git push origin feature/minha-feature`)
5. Abra um Pull Request

## 📄 Licença

Ainda não definida. Adicione o arquivo `LICENSE` para especificar os termos de uso do projeto.
