import requests
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
#Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'} 
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")
# Store API response in a variable.
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")
# Process results.
print(response_dict.keys())
#print(response_dict['items'][0]['name'])
print(f"Total repositories: {response_dict['total_count']}")
# Explore information about the repositories.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")
# Examine the first repository.
#repo_dict=repo_dicts[0]
#print(repo_dict['name'])
#print(f"\nKeys: {len(repo_dict)}")
'''for t, key in enumerate(sorted (repo_dict.keys())):
    print(t,key)'''
print("\nSelected information about first repository:")

'''for repo_dict in repo_dicts:
    print("\nRepository Information:")
    print(f"Name: {repo_dict.get('name')}")
    print(f"Owner: {repo_dict.get('owner', {}).get('login')}")
    print(f"Stars: {repo_dict.get('stargazers_count')}")
    print(f"Repository: {repo_dict.get('html_url')}")
    print(f"Created: {repo_dict.get('created_at')}")
    print(f"Updated: {repo_dict.get('updated_at')}")
    print(f"Description: {repo_dict.get('description')}")'''
for repo_dict in repo_dicts:
   print(f"Name: {repo_dict['name']}")
   print(f"Owner: {repo_dict['owner']['login']}")
   print(f"Stars: {repo_dict['stargazers_count']}")
   print(f"Repository: {repo_dict['html_url']}")
   print(f"Created: {repo_dict['created_at']}")
   print(f"Updated: {repo_dict['updated_at']}")
   desc = repo_dict.get('description')
   print(f"Description: {desc[:100] if desc else 'No description'}")
   
