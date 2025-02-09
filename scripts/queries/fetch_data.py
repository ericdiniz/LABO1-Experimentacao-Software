import os
import requests
import time
from dotenv import load_dotenv
from scripts.queries.queries_repository import QUERY_POPULAR_REPOS

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()
TOKEN = os.getenv("GITHUB_TOKEN")

GITHUB_API_URL = "https://api.github.com/graphql"

def fetch_popular_repositories():
    """Busca os 1.000 repositórios mais populares em blocos de 5, evitando erro 502."""
    headers = {"Authorization": f"Bearer {TOKEN}"}
    all_repositories = []
    after_cursor = None  # Para paginação
    max_attempts = 5  # Número máximo de tentativas por requisição

    while len(all_repositories) < 1000:
        variables = {"afterCursor": after_cursor}
        attempt = 0

        while attempt < max_attempts:
            response = requests.post(GITHUB_API_URL, json={"query": QUERY_POPULAR_REPOS, "variables": variables}, headers=headers)
            print("\n🛠 Debug - Status Code:", response.status_code)

            if response.status_code == 200:
                response_data = response.json()
                print("\n📜 Debug - Resposta JSON:", response_data)

                data = response_data.get("data", {}).get("search", {})
                repositories = data.get("edges", [])
                page_info = data.get("pageInfo", {})

                for repo in repositories:
                    node = repo["node"]
                    all_repositories.append({
                        "Nome": node["name"],
                        "Dono": node.get("owner", {}).get("login", "Desconhecido"),
                        "Descrição": node.get("description", "Sem descrição"),
                        "Estrelas": node.get("stargazers", {}).get("totalCount", 0),
                        "Forks": node.get("forks", {}).get("totalCount", 0),
                        "Criado em": node.get("createdAt", "Data não disponível")
                    })

                # Se ainda há mais páginas, atualizamos o cursor
                if page_info.get("hasNextPage") and len(all_repositories) < 1000:
                    after_cursor = page_info["endCursor"]
                else:
                    return all_repositories  # Se não há mais páginas, terminamos

                break  # Sai do loop de tentativas se tiver sucesso

            elif response.status_code == 502:
                print(f"⚠️ Erro 502! Tentando novamente... ({attempt+1}/{max_attempts})")
                time.sleep(2**attempt)  # Espera exponencial antes de tentar de novo
                attempt += 1

            else:
                print(f"❌ Erro inesperado: {response.status_code} - {response.text}")
                return None

    return all_repositories
