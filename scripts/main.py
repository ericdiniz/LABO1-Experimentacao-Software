from scripts.queries.fetch_data import fetch_popular_repositories

def main():
    """Executa a consulta GraphQL e exibe os 1.000 repositórios mais populares."""
    print("\n🔍 Buscando os 1.000 repositórios mais populares no GitHub...\n")
    repos = fetch_popular_repositories()

    if repos:
        for i, repo in enumerate(repos, 1):
            print(f"{i}. {repo['Nome']} - {repo['Dono']}")
            print(f"   ⭐ Estrelas: {repo['Estrelas']} | 🍴 Forks: {repo['Forks']}")
            print(f"   📅 Criado em: {repo['Criado em']}")
            print(f"   📝 Descrição: {repo['Descrição']}\n")
    else:
        print("❌ Falha ao buscar repositórios.")

if __name__ == "__main__":
    main()
