# **LAB01 - Análise de Repositórios Populares no GitHub**

📌 **Projeto do Laboratório de Experimentação de Software**

Este repositório contém a implementação do **Lab01**, onde analisamos as características de repositórios open-source populares no GitHub utilizando **GraphQL e Python**. O objetivo é coletar e estudar métricas que ajudam a responder perguntas sobre a popularidade, contribuições e evolução dos projetos.

---

## 📊 **Objetivo do Projeto**

O estudo tem como foco responder as seguintes **Questões de Pesquisa (RQs):**

1. **Os sistemas populares são maduros/antigos?**
2. **Recebem muitas contribuições externas?**
3. **Lançam releases com frequência?**
4. **São atualizados frequentemente?**
5. **Usam linguagens populares?**
6. **Possuem um alto percentual de issues fechadas?**
7. **(Bônus) Linguagens influenciam nas métricas?**

Para responder a essas perguntas, coletamos **dados de 1.000 repositórios mais populares** no GitHub.

---

## 🚀 **Tecnologias Utilizadas**

- **Python 3.x** → Processamento e análise dos dados
- **GraphQL API do GitHub** → Extração das métricas dos repositórios
- **Requests** → Requisições à API
- **Pandas** → Manipulação dos dados
- **Matplotlib & Seaborn** → Visualização dos resultados
- **Jupyter Notebook** → Análises exploratórias

---

## 📚 **Estrutura do Repositório**

```
📝 LAB01
 ┣ 📂 scripts/        # Scripts para coleta e processamento de dados
 ┣ 📂 data/           # Arquivos CSV e JSON com os dados coletados
 ┣ 📂 notebooks/      # Análises exploratórias e gráficos
 ┣ 📄 report.md       # Relatório final do laboratório
 ┣ 📄 requirements.txt # Dependências do projeto
 ┣ 📄 run.sh          # Script de execução (se necessário)
 ┗ 📄 README.md       # Documentação do repositório
```

**Nota:** O diretório do ambiente virtual (`venv/` ou `myenv/`) **não deve ser versionado**. Certifique-se de que ele está incluído no `.gitignore`.

---

## 🛠 **Como Rodar o Projeto**

1️⃣ **Clone o repositório:**
```sh
git clone https://github.com/seu-usuario/lab01.git
cd lab01
```

2️⃣ **Crie um ambiente virtual (recomendado):**
```sh
python3 -m venv venv
source venv/bin/activate  # (No Windows use: venv\Scripts\activate)
```

3️⃣ **Instale as dependências:**
```sh
pip install -r requirements.txt
```

4️⃣ **Execute a coleta de dados:**
```sh
python scripts/github_query.py
```

5️⃣ **Analise os dados:**
Abra o **Jupyter Notebook** e explore as métricas coletadas:
```sh
jupyter notebook
```

---

## 📢 **Resultados e Discussões**

Os resultados finais, gráficos e insights estarão disponíveis no arquivo **report.md**.

---

## 🐝 **Boas Práticas e Contribuição**

- Certifique-se de ativar o ambiente virtual antes de rodar qualquer código.
- Use `requirements.txt` para manter um controle das dependências.
- O diretório `venv/` **não deve ser versionado**.
- Se desejar contribuir, faça um fork e abra um Pull Request.

---

## 📝 **Licença**

Este projeto é apenas para fins acadêmicos e segue as diretrizes do curso.

---

Se precisar de mais ajustes, me avise! 🚀😊
