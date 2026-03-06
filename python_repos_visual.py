import requests
from plotly.graph_objects import Bar,Layout
from plotly import offline
#Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'} 
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")
# Process results.
response_dict = r.json()
repo_dicts = response_dict['items']
repo_links,stars, labels= [],[],[]
for repo_dict in repo_dicts:
    repo_name=repo_dict['name']
    stars.append(repo_dict['stargazers_count'])
    owner=repo_dict['owner']['login']
    desc=repo_dict.get('description')
    description=desc[:100] if desc else "No description"
    label=f"{owner}<br />{description}"
    labels.append(label)
    repo_url=repo_dict['html_url']
    repo_link=f"<a href='{repo_url}'> {repo_name}</a>"
    repo_links.append(repo_link)
    
# MAKE visualization clearly

data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext':labels,
    'marker':{
        'color':"rgb(60,100,150)",
        'line':{'width':1.5, 'color':'rgb(255,0,0)'}
    },
    'opacity':0.6,

}]

my_layout={
    'title': 'Most_Starred Python Projects on GitHub',
   
    'xaxis':{
        'title':'Repository',
        
    },
    'yaxis':{
        'title':'Stars',
      
    },

}
fig={'data':data,'layout':my_layout}
offline.plot(fig,filename='python_repos.html')
