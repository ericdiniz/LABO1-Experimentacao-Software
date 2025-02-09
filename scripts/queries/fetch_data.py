import os
import requests
from dotenv import load_dotenv
from scripts.queries.queries_repository import QUERY_POPULAR_REPOS

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()
TOKEN = os.getenv("GITHUB_TOKEN")

GITHUB_API_URL = "https://api.github.com/graphql"

def fetch_popular_repositories():
    """Realiza a requisição GraphQL para buscar os 100 repositórios mais populares."""
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.post(GITHUB_API_URL, json={"query": QUERY_POPULAR_REPOS}, headers=headers)

    print("\n🛠 Debug - Status Code:", response.status_code)
    try:
        response_data = response.json()
        print("\n📜 Debug - Resposta JSON:", response_data)
    except Exception as e:
        print("\n⚠️ Erro ao converter resposta para JSON:", e)
        return None

    if response.status_code == 200:
        data = response_data.get("data", {}).get("search", {}).get("edges", [])

        # Formatar os dados para uma saída mais legível
        repo_list = []
        for repo in data:
            node = repo["node"]
            repo_list.append({
                "Nome": node["name"],
                "Dono": node.get("owner", {}).get("login", "Desconhecido"),  # Evita erro se o campo não existir
                "Descrição": node.get("description", "Sem descrição"),
                "Estrelas": node.get("stargazers", {}).get("totalCount", 0),
                "Forks": node.get("forks", {}).get("totalCount", 0),
                "Criado em": node.get("createdAt", "Data não disponível")
            })

        return repo_list
    else:
        print(f"❌ Erro na requisição: {response.status_code} - {response.text}")
        return None
