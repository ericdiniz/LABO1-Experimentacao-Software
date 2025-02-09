QUERY_POPULAR_REPOS = """
query ($afterCursor: String) {
  search(query: "stars:>0", type: REPOSITORY, first: 5, after: $afterCursor) {
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
    pageInfo {
      endCursor
      hasNextPage
    }
  }
}
"""
