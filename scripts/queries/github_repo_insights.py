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

df = pd.read_csv(file_path)

df["Criado em"] = pd.to_datetime(df["Criado em"], errors='coerce').dt.tz_localize(None)
df["Última Atualização"] = pd.to_datetime(df["Última Atualização"], errors='coerce').dt.tz_localize(None)

df["Idade (anos)"] = (datetime.datetime.now() - df["Criado em"]).dt.days / 365
df["Tempo desde última atualização (dias)"] = (datetime.datetime.now() - df["Última Atualização"]).dt.days
df["Percentual Issues Fechadas"] = (df["Issues Fechadas"] / df["Issues Abertas"]).fillna(0) * 100

def add_labels(ax):
    for container in ax.containers:
        ax.bar_label(container, fmt="%.0f", fontsize=10, color="black", fontweight="bold")

fig, axes = plt.subplots(3, 2, figsize=(14, 12))

# RQ 01 - Idade dos Repositórios
sns.histplot(df["Idade (anos)"].dropna(), bins=20, ax=axes[0, 0], kde=True, color="royalblue")
axes[0, 0].set_title("Idade dos Repositórios Populares", fontsize=12)
axes[0, 0].set_xlabel("Idade (anos)")
axes[0, 0].set_ylabel("Número de Repositórios")

# RQ 02 - Pull Requests Aceitos
sns.histplot(df["PRs Aceitos"].dropna(), bins=20, ax=axes[0, 1], kde=True, color="darkred", log_scale=True)
axes[0, 1].set_title("Distribuição de Pull Requests Aceitos", fontsize=12)
axes[0, 1].set_xlabel("PRs Aceitos")
axes[0, 1].set_ylabel("Número de Repositórios")

# RQ 03 - Releases
sns.histplot(df["Releases"].dropna(), bins=20, ax=axes[1, 0], kde=True, color="seagreen", log_scale=True)
axes[1, 0].set_title("Distribuição de Releases", fontsize=12)
axes[1, 0].set_xlabel("Total de Releases")
axes[1, 0].set_ylabel("Número de Repositórios")

# RQ 04 - Tempo desde Última Atualização
sns.histplot(df["Tempo desde última atualização (dias)"].dropna(), bins=20, ax=axes[1, 1], kde=True, color="orange")
axes[1, 1].set_title("Tempo desde Última Atualização", fontsize=12)
axes[1, 1].set_xlabel("Dias desde a última atualização")
axes[1, 1].set_ylabel("Número de Repositórios")

# RQ 05 - Linguagens Populares
ax5 = sns.barplot(x=df["Linguagem"].value_counts().head(10).index,
                  y=df["Linguagem"].value_counts().head(10).values,
                  hue=df["Linguagem"].value_counts().head(10).index,
                  ax=axes[2, 0], palette="Blues_r", legend=False)
axes[2, 0].set_title("Top 10 Linguagens em Repositórios Populares", fontsize=12)
axes[2, 0].set_xlabel("Linguagem")
axes[2, 0].set_ylabel("Número de Repositórios")
axes[2, 0].tick_params(axis='x', rotation=45)
add_labels(ax5)

# RQ 06 - Percentual de Issues Fechadas
sns.histplot(df["Percentual Issues Fechadas"].dropna(), bins=20, ax=axes[2, 1], kde=True, color="purple")
axes[2, 1].set_title("Distribuição do Percentual de Issues Fechadas", fontsize=12)
axes[2, 1].set_xlabel("Percentual de Issues Fechadas (%)")
axes[2, 1].set_ylabel("Número de Repositórios")

languages_popular = ["Python", "JavaScript", "Java", "C#", "C++", "Go", "Rust", "TypeScript"]

# RQ 07 - Bonus
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


plt.tight_layout()
plt.show()
