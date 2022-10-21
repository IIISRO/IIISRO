import requests
import json

url="https://api.github.com/user/repos"
token='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'

headers={"Authorization":"token {}".format(token)}

RepositoryName=input("Enter repo name:")

data={'name':"{}".format(RepositoryName)}

requests.post(url,data=json.dumps(data),headers=headers)