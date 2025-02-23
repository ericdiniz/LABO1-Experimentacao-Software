import os
import requests
import time
import random
from dotenv import load_dotenv
from scripts.queries.queries_repository import QUERY_POPULAR_REPOS

load_dotenv()
TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_API_URL = "https://api.github.com/graphql"

def fetch_popular_repositories():
    headers = {"Authorization": f"Bearer {TOKEN}"}
    all_repositories = []
    after_cursor = None
    max_attempts = 5
    timeout_seconds = 180

    while len(all_repositories) < 1000:
        variables = {"afterCursor": after_cursor}
        attempt = 0

        while attempt < max_attempts:
            try:
                response = requests.post(
                    GITHUB_API_URL,
                    json={"query": QUERY_POPULAR_REPOS, "variables": variables},
                    headers=headers,
                    timeout=timeout_seconds
                )

                if response.status_code == 200:
                    response_data = response.json()
                    data = response_data.get("data", {}).get("search", {})
                    repositories = data.get("edges", [])
                    page_info = data.get("pageInfo", {})

                    if not repositories:
                        print("Nenhum repositório encontrado! Verifique sua query.")
                        return None

                    for repo in repositories:
                        node = repo["node"]
                        all_repositories.append({
                            "Nome": node["name"],
                            "Dono": node.get("owner", {}).get("login", "Desconhecido"),
                            "Descrição": node.get("description", "Sem descrição"),
                            "Estrelas": node.get("stargazers", {}).get("totalCount", 0),
                            "Forks": node.get("forks", {}).get("totalCount", 0),
                            "Criado em": node.get("createdAt", "Data não disponível"),
                            "Última Atualização": node.get("updatedAt", "Data não disponível"),
                            "Linguagem": (node.get("primaryLanguage") or {}).get("name", "Não especificada"),
                            "Commits": node.get("defaultBranchRef", {}).get("target", {}).get("history", {}).get("totalCount", 0),
                            "Issues Abertas": node.get("issues", {}).get("totalCount", 0),
                            "Issues Fechadas": node.get("closedIssues", {}).get("totalCount", 0),
                            "Releases": node.get("releases", {}).get("totalCount", 0),
                            "PRs Aceitos": node.get("pullRequests", {}).get("totalCount", 0),
                        })

                    print(f"{len(all_repositories)}/1000 repositórios coletados...")

                    if page_info.get("hasNextPage") and len(all_repositories) < 1000:
                        after_cursor = page_info.get("endCursor")
                    else:
                        print("Coleta de repositórios concluída!")
                        return all_repositories

                    break

                elif response.status_code == 502:
                    wait_time = min(60, 2 ** attempt) + random.uniform(0, 3)
                    print(f"Erro 502. Tentando novamente ({attempt+1}/{max_attempts}) em {wait_time:.2f}s...")
                    time.sleep(wait_time)
                    attempt += 1

                elif response.status_code == 403:
                    reset_time = int(response.headers.get("X-RateLimit-Reset", time.time() + 60))
                    wait_time = max(0, reset_time - time.time())
                    print(f"Rate limit atingido! Aguardando {int(wait_time)} segundos...")
                    time.sleep(wait_time)
                    attempt += 1

                else:
                    print(f"Erro inesperado: {response.status_code} - {response.text}")
                    return None

            except requests.exceptions.ReadTimeout:
                print(f"Timeout! Tentando novamente ({attempt+1}/{max_attempts}) em 5s...")
                time.sleep(5)
                attempt += 1

            except requests.exceptions.ChunkedEncodingError:
                print(f"Erro 'Response ended prematurely'. Tentando novamente ({attempt+1}/{max_attempts}) em 5s...")
                time.sleep(5)
                attempt += 1

            except requests.exceptions.RequestException as e:
                print(f"Erro na requisição: {e}")
                return None

    print("Coleta de repositórios concluída!")
    return all_repositories
