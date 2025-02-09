queries_repository = """
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
