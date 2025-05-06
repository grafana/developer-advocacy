# prompt: create a python function that does a request to GET /api/search/ from https://play.grafana.org with type=dash-db and limit 5000 and returns the result as json
from google.colab import userdata

import requests
import json

tok = userdata.get('token')

def grafana_search():
  url = "https://play.grafana.org/api/search/"
  params = {
      "type": "dash-db",
      "limit": 5000
  }
  try:
    response = requests.get(url, params=params, headers={"Authorization": "Bearer %s" % tok})
    response.raise_for_status() # Raise an exception for bad status codes
    return response.json()
  except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
    return None

# Example usage
results = grafana_search()
uids = [r['uid'] for r in results]
if results:
  print(json.dumps(uids))
  print("%d dashboards" % len(uids))

from google.colab import userdata
tok = userdata.get('token')

uid = "000000012"
headers = {
    "Authorization": "Bearer " + tok
}
response = requests.get(f"https://play.grafana.org/api/dashboards/uid/{uid}/versions", headers=headers)
versions = response.json()['versions']
x=0

for version in versions:
  uid = version['uid']
  createdBy = version['createdBy']
  created = version['created']
  vNumber = version['version']

  print("%s,%s,%s,%s" % (uid, createdBy, created, vNumber))

from google.colab import drive
drive.mount('/content/drive')
path = "/content/drive/My Drive/Play Enumeration"

import pandas as pd

data = {
    "author": ["a","b"],
    "dashboard": ["c", "d"]
}

df = pd.DataFrame(data)
df.to_csv(path + "/test.csv", index=False)
print(df)

"""## Enumerate all Accounts which have ever modified anything"""

from google.colab import userdata
tok = userdata.get('token')

data = {
    "author": [],
    "dashboard": [],
}
authors = {
    "author": [],
    "n": [],

}

frame = {
    "uid": [],
    "createdBy": [],
    "created": [],
    "version": []
}

headers = {
    "Authorization": "Bearer " + tok
}

cache = {}

limit = 2000
x=0

for uid in uids:
  x = x + 1
  if x >= limit: break

  if x % 10 == 0:
    print("Request %d" % x)

  response = requests.get(f"https://play.grafana.org/api/dashboards/uid/{uid}/versions", headers=headers)
  try:
    j = response.json()
    versions = j['versions']
  except KeyError:
    print("Failed versions on %s" % json.dumps(j))
    versions = []


  for version in versions:
    uid = version['uid']
    createdBy = version['createdBy']
    created = version['created']
    vNumber = version['version']

    frame["uid"].append(uid)
    frame["createdBy"].append(createdBy)
    frame["created"].append(created)
    frame["version"].append(vNumber)

    if not createdBy in cache:
      cache[createdBy] = { "latest": created, "versions": 1 }
    else:
      cache[createdBy]['versions'] = cache[createdBy]['versions'] + 1
      if cache[createdBy]['latest'] < created:
        cache[createdBy]['latest'] = created

df = pd.DataFrame(frame)
df.to_csv(path + "/dashboard-authors-all-versions.csv", index=False)

frame2 = {
    "author": [],
    "versions": [],
    "latest": []
}

for author in cache:
  frame2["author"].append(author)
  frame2["versions"].append(cache[author]['versions'])
  frame2["latest"].append(cache[author]['latest'])

df = pd.DataFrame(frame2)
df.to_csv(path + "/dashboard-authors-summarized-stats.csv", index=False)

print(json.dumps(cache, indent=2))
print("Done")

"""## Enumerate ALL users whether or not they've ever made a change"""

# prompt: create a python function that does a request to GET /api/search/ from https://play.grafana.org with type=dash-db and limit 5000 and returns the result as json
from google.colab import userdata

import requests
import json

tok = userdata.get('token')

def user_search(page=1):
  url = "https://play.grafana.org/api/org/users/search?perpage=5000&page=%s&query=&sort=login-asc,email-asc" % page
  try:
    response = requests.get(url, headers={"Authorization": "Bearer %s" % tok})
    response.raise_for_status() # Raise an exception for bad status codes
    data = response.json()
    return data
  except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
    return None

page = 0

users = {
    "orgId": [],
    "userId": [],
    "uid": [],
    "email": [],
    "login": [],
    "name": [],
    "role": [],
    "lastSeenAt": [],
    "lastSeenAtAge": [],
    "isExternallySynced": [],
    "isDisabled": [],
    'avatarUrl': [],
}

while True:
  page = page + 1
  print("Page %d" % page)
  results = user_search(page)

  for user in results['orgUsers']:
    users["orgId"].append(user['orgId'])
    users["userId"].append(user['userId'])
    users["uid"].append(user['uid'])
    users["email"].append(user['email'])
    users["login"].append(user['login'])
    users["name"].append(user['name'])
    users["role"].append(user['role'])
    users["lastSeenAt"].append(user['lastSeenAt'])
    users["lastSeenAtAge"].append(user['lastSeenAtAge'])
    users["isExternallySynced"].append(user['isExternallySynced'])
    users["isDisabled"].append(user['isDisabled'])
    users['avatarUrl'].append(user['avatarUrl'])

  # print(json.dumps(user, indent=2))

  if len(results['orgUsers']) == 0:
    break

print("Writing CSV")
df = pd.DataFrame(users)
df.to_csv(path + "/all-users.csv", index=False)
print("Done")
