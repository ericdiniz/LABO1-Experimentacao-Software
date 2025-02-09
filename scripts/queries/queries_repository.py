QUERY_POPULAR_REPOS = """
{
  search(query: "stars:>1000", type: REPOSITORY, first: 5) {
    edges {
      node {
        ... on Repository {
          name
          owner {
            login
          }
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
    }
  }
}
"""
