import os
import requests
from dotenv import load_dotenv

# Carrega variáveis de ambiente do .env
load_dotenv()
TOKEN = os.getenv("GITHUB_TOKEN")

GITHUB_API_URL = "https://api.github.com/graphql"

# Função para fazer requisições GraphQL
def fetch_github_data(query):
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.post(GITHUB_API_URL, json={"query": query}, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erro: {response.status_code} - {response.text}")
