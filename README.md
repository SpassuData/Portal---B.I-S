# Portal B.I-S

Aplicação web que consolida, em um único lugar, os links dos principais dashboards de BI usados no dia a dia da equipe.

## 📋 Sobre o projeto

O **Portal B.I-S** nasce da necessidade de centralizar o acesso aos diversos dashboards de Business Intelligence espalhados pela organização, evitando a dispersão de links e facilitando a navegação da equipe entre os relatórios utilizados com mais frequência.

Os dashboards são organizados por área (People Analytics, DP Analytics, Performance & Resultados, Ramp Up, Workforce Analytics) e o acesso exige login com conta corporativa Microsoft.

## 🚀 Tecnologias

- **Python** / **Django** — back-end e regras de negócio
- **MSAL** — autenticação via Azure AD / Microsoft Entra ID
- **HTML** (templates Django) — camada de apresentação
- **WhiteNoise** — arquivos estáticos em produção
- **Gunicorn** — servidor WSGI de produção

> O projeto não usa banco de dados (login e sessão não dependem de tabelas; a sessão é assinada via cookie). Se cadastro/administração de dashboards for implementado no futuro, um banco (Postgres em produção) pode ser adicionado.

## 📁 Estrutura do projeto

```
Portal---B.I-S/
├── core/            # App principal (views, urls, decorators)
├── portal_bi/        # Configurações do projeto Django (settings, urls, wsgi/asgi)
├── templates/         # Templates HTML das páginas
├── static/             # Arquivos estáticos (CSS, JS, imagens)
├── manage.py           # Script de gerenciamento do Django
├── requirements.txt    # Dependências do projeto
└── .env.example         # Modelo das variáveis de ambiente necessárias
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
   pip install -r requirements.txt
   ```

4. Copie o arquivo de variáveis de ambiente e preencha os valores
   ```bash
   cp .env.example .env
   ```
   > O `.env` nunca deve ser commitado (já está no `.gitignore`). Preencha `SECRET_KEY`, `ALLOWED_HOSTS`, as credenciais `AZURE_CLIENT_ID`/`AZURE_CLIENT_SECRET`/`AZURE_TENANT_ID`/`REDIRECT_URI` e os links `DASHBOARD_*` de cada área. Veja `.env.example` para a lista completa.

5. Rode o servidor de desenvolvimento
   ```bash
   python manage.py runserver
   ```

6. Acesse [http://127.0.0.1:8000/](http://127.0.0.1:8000/) no navegador.

## 🗺️ Roadmap

- [x] Organização dos dashboards por categoria
- [x] Autenticação de usuários (Azure AD / Microsoft Entra ID)
- [ ] Área administrativa para gerenciar links

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/minha-feature`)
3. Commit suas alterações (`git commit -m 'Adiciona minha feature'`)
4. Faça push para a branch (`git push origin feature/minha-feature`)
5. Abra um Pull Request

## 📄 Licença

Ainda não definida. Adicione o arquivo `LICENSE` para especificar os termos de uso do projeto.
