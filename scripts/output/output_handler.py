import csv
import os

OUTPUT_DIR = "outputs"

def save_to_csv(repositories, filename="repos.csv"):
    """Salva a lista de repositórios em um arquivo CSV dentro da pasta outputs/."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    filepath = os.path.join(OUTPUT_DIR, filename)

    with open(filepath, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Nome", "Dono", "Descrição", "Estrelas", "Forks", "Criado em",
            "Última Atualização", "Linguagem", "Commits",
            "Issues Abertas", "Issues Fechadas", "Releases", "PRs Aceitos"
        ])

        for repo in repositories:
            writer.writerow([
                repo["Nome"],
                repo["Dono"],
                repo["Descrição"],
                repo["Estrelas"],
                repo["Forks"],
                repo["Criado em"],
                repo["Última Atualização"],
                repo["Linguagem"],
                repo["Commits"],
                repo["Issues Abertas"],
                repo["Issues Fechadas"],
                repo["Releases"],
                repo["PRs Aceitos"]
            ])

    print(f"📁 Dados salvos em: {filepath}")
