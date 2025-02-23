import os
from dotenv import load_dotenv
from scripts.queries.fetch_data import fetch_popular_repositories
from scripts.output.output_handler import save_to_csv

load_dotenv()
TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_API_URL = "https://api.github.com/graphql"

def main():
    print("\nBuscando os 1000 repositórios com mais estrelas no GITHUB...\n")
    repos = fetch_popular_repositories()

    if repos:
        save_to_csv(repos)
    else:
        print("Falha ao buscar repositórios.")

if __name__ == "__main__":
    main()
