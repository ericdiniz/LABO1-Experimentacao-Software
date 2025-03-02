import pandas as pd
import matplotlib.pyplot as plt
import datetime
import seaborn as sns
import os

plt.style.use("seaborn-v0_8-darkgrid")
sns.set_palette("coolwarm")

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.abspath(os.path.join(BASE_DIR, "../../"))

file_path = os.path.join(ROOT_DIR, "outputs", "repos.csv")
output_dir = os.path.join(ROOT_DIR, "outputs", "graphs")

# Criar diretório para salvar gráficos, se não existir
os.makedirs(output_dir, exist_ok=True)

df = pd.read_csv(file_path)

df["Criado em"] = pd.to_datetime(df["Criado em"], errors='coerce').dt.tz_localize(None)
df["Última Atualização"] = pd.to_datetime(df["Última Atualização"], errors='coerce').dt.tz_localize(None)

df["Idade (anos)"] = (datetime.datetime.now() - df["Criado em"]).dt.days / 365
df["Tempo desde última atualização (dias)"] = (datetime.datetime.now() - df["Última Atualização"]).dt.days
df["Percentual Issues Fechadas"] = (df["Issues Fechadas"] / df["Issues Abertas"]).fillna(0) * 100

def save_graph(fig, filename):
    file_path = os.path.join(output_dir, filename)
    fig.savefig(file_path)
    plt.close(fig)

# RQ 01 - Idade dos Repositórios
fig, ax = plt.subplots(figsize=(8, 6))
sns.histplot(df["Idade (anos)"].dropna(), bins=20, ax=ax, kde=True, color="royalblue")
ax.set_title("Idade dos Repositórios Populares", fontsize=12)
ax.set_xlabel("Idade (anos)")
ax.set_ylabel("Número de Repositórios")
save_graph(fig, "RQ01_idade_repositorios.png")

# RQ 02 - Pull Requests Aceitos
fig, ax = plt.subplots(figsize=(8, 6))
sns.histplot(df["PRs Aceitos"].dropna(), bins=20, ax=ax, kde=True, color="darkred", log_scale=True)
ax.set_title("Distribuição de Pull Requests Aceitos", fontsize=12)
ax.set_xlabel("PRs Aceitos")
ax.set_ylabel("Número de Repositórios")
save_graph(fig, "RQ02_pull_requests.png")

# RQ 03 - Releases
fig, ax = plt.subplots(figsize=(8, 6))
sns.histplot(df["Releases"].dropna(), bins=20, ax=ax, kde=True, color="seagreen", log_scale=True)
ax.set_title("Distribuição de Releases", fontsize=12)
ax.set_xlabel("Total de Releases")
ax.set_ylabel("Número de Repositórios")
save_graph(fig, "RQ03_releases.png")

# RQ 04 - Tempo desde Última Atualização
fig, ax = plt.subplots(figsize=(8, 6))
sns.histplot(df["Tempo desde última atualização (dias)"].dropna(), bins=20, ax=ax, kde=True, color="orange")
ax.set_title("Tempo desde Última Atualização", fontsize=12)
ax.set_xlabel("Dias desde a última atualização")
ax.set_ylabel("Número de Repositórios")
save_graph(fig, "RQ04_ultima_atualizacao.png")

# RQ 05 - Linguagens Populares
fig, ax = plt.subplots(figsize=(8, 6))
ax = sns.barplot(x=df["Linguagem"].value_counts().head(10).index,
                 y=df["Linguagem"].value_counts().head(10).values,
                 hue=df["Linguagem"].value_counts().head(10).index,
                 palette="Blues_r", legend=False)
ax.set_title("Top 10 Linguagens em Repositórios Populares", fontsize=12)
ax.set_xlabel("Linguagem")
ax.set_ylabel("Número de Repositórios")
ax.tick_params(axis='x', rotation=45)
save_graph(fig, "RQ05_linguagens.png")

# RQ 06 - Percentual de Issues Fechadas
fig, ax = plt.subplots(figsize=(8, 6))
sns.histplot(df["Percentual Issues Fechadas"].dropna(), bins=20, ax=ax, kde=True, color="purple")
ax.set_title("Distribuição do Percentual de Issues Fechadas", fontsize=12)
ax.set_xlabel("Percentual de Issues Fechadas (%)")
ax.set_ylabel("Número de Repositórios")
save_graph(fig, "RQ06_issues_fechadas.png")

# RQ 07 - Análise por Linguagem
languages_popular = ["Python", "JavaScript", "Java", "C#", "C++", "Go", "Rust", "TypeScript"]

df_filtered = df.dropna(subset=["PRs Aceitos", "Releases", "Tempo desde última atualização (dias)", "Linguagem"])
df_filtered["Linguagem Popular"] = df_filtered["Linguagem"].apply(lambda x: x if x in languages_popular else "Outras")

grouped_data = df_filtered.groupby("Linguagem Popular").agg({
    "PRs Aceitos": "mean",
    "Releases": "mean",
    "Tempo desde última atualização (dias)": "mean"
}).reset_index()

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

sns.barplot(data=grouped_data, x="Linguagem Popular", y="PRs Aceitos", ax=axes[0], palette="coolwarm")
axes[0].set_title("Média de Pull Requests Aceitos por Linguagem")
axes[0].set_xlabel("Linguagem")
axes[0].set_ylabel("Média de PRs Aceitos")
axes[0].tick_params(axis='x', rotation=45)

sns.barplot(data=grouped_data, x="Linguagem Popular", y="Releases", ax=axes[1], palette="coolwarm")
axes[1].set_title("Média de Releases por Linguagem")
axes[1].set_xlabel("Linguagem")
axes[1].set_ylabel("Média de Releases")
axes[1].tick_params(axis='x', rotation=45)

sns.barplot(data=grouped_data, x="Linguagem Popular", y="Tempo desde última atualização (dias)", ax=axes[2], palette="coolwarm")
axes[2].set_title("Média de Tempo desde Última Atualização por Linguagem")
axes[2].set_xlabel("Linguagem")
axes[2].set_ylabel("Média de Dias desde Última Atualização")
axes[2].tick_params(axis='x', rotation=45)

save_graph(fig, "RQ07_analise_por_linguagem.png")
