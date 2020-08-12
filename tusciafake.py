import facebook
import random
f=open("tusciav.txt",encoding="utf8")
f=f.read()
lista=f.splitlines()
random.seed()
articolo=lista[random.randint(1,200)]
graph = facebook.GraphAPI(access_token="token", version="2.12")
graph.put_object(parent_object='me', connection_name='feed',
                  message=articolo)
