import requests
import secrets

#step 1 - create a jira issue using the snyk endpoint
#orgId = 'a42d5fd5-56a7-4ae7-a106-4c90dbc1e825'
#projectId = 'f8ec6a50-4212-4dfc-a794-a85defd9ae9d'
#issueId = 'SNYK-JS-ANSIHTML-1296849'
url = 'https://snyk.io/api/v1/org/a42d5fd5-56a7-4ae7-a106-4c90dbc1e825/project/f8ec6a50-4212-4dfc-a794-a85defd9ae9d/issue/SNYK-JS-ANSIHTML-1296849/jira-issue'

snyk_post = requests.post(url, headers = {
    'Content Type': 'application/json',
    'Authorization': secrets.API_KEY
})