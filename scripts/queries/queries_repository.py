
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
          updatedAt
          primaryLanguage {
            name
          }
          releases {
            totalCount
          }
          issues {
            totalCount
          }
          closedIssues: issues(states: CLOSED) {
            totalCount
          }
          pullRequests(states: MERGED) {  # <-- Adicionado para RQ 02
            totalCount
          }
          defaultBranchRef {
            target {
              ... on Commit {
                history(first: 1) {
                  totalCount
                }
              }
            }
          }
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
