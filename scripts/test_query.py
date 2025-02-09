import requests

GITHUB_API_URL = "https://api.github.com/graphql"
TOKEN = "token"

#
query = """
{
  repository(owner: "torvalds", name: "linux") {
    name
    description
    stargazers {
      totalCount
    }
    forks {
      totalCount
    }
    createdAt
  }
}
"""

headers = {"Authorization": f"Bearer {TOKEN}"}
response = requests.post(GITHUB_API_URL, json={"query": query}, headers=headers)

print(response.json())
