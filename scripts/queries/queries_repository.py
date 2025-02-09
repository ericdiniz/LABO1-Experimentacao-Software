QUERY_POPULAR_REPOS = """
{
  search(query: "stars:>0", type: REPOSITORY, first: 3) {
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
