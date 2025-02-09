import json
from queries.queries_repository import queries_repository
from fetch_data import fetch_github_data

# Executa a query e exibe os resultados formatados
if __name__ == "__main__":
    try:
        result = fetch_github_data(query_repo)
        repo_data = result.get("data", {}).get("repository", {})

        if repo_data:
            print("\n📌 Repositório: ", repo_data["name"])
            print("📝 Descrição: ", repo_data["description"])
            print("⭐ Estrelas: ", repo_data["stargazers"]["totalCount"])
            print("🔄 Forks: ", repo_data["forks"]["totalCount"])
            print("📅 Criado em: ", repo_data["createdAt"])
        else:
            print("❌ Nenhum dado encontrado.")

    except Exception as e:
        print(f"\n❌ Erro ao buscar dados: {e}")
