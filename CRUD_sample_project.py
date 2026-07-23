# API: Application Programming Interface
# JSON: Java Script Object Notation
# Third Party Module: Request
# HTTP: Hyper Text Transfer Protocol - Rules 
# HTTP Methods: 
# C -> POST
# R -> GET
# U -> PUT/PATCH
# D -> DELETE

# GET
import requests

api=requests.get("http://localhost:3000/headphones")

a=api.json()
for post in a:
    print(post)


# Ex:1 DUMPS POST
import requests
import json #Json in-built module
api="http://localhost:3000/Mobiles"

sending_data ={"Id":1,"Name":"RealmeGT7","Ram":"12GB","Processor":"Dimencity 94","Price":41000}

json_data=json.dumps(sending_data) # Dumps method converts the python objects into json code 

res=requests.post(api,data=json_data)
print(res)
print(res.json())


# EX:2 POST
import requests
import json
api = "http://localhost:3000/Mobiles"

new_mobile = {"id":"5","Name":"s26","Ram":"12GB","Processor":"SPGen8s elite"}

# #json_data=json.dumps(new.mobile)
res=requests.post(api,json=new_mobile) # Json keyword converts data automatically

print(res.json())



# PUT: PUT Can Create new one, and it removes old one
# Patch: It just update a value 

# Ex: 5 PUT it can update new, and removes previous 
import requests

api="http://localhost:3000/smartwatches/1"

data = {"Processor":"S8 GEN9"}

res=requests.put(api,json=data)

print(res.json())


# Ex: 6 Patch for update existing data
import requests

api="http://localhost:3000/tablets/3"

data = {"Ram":"16GB"}

res=requests.patch(api,json=data)

print(res.json())


# Ex: 7 Delete
import requests

api = "http://localhost:3000/Mobiles/1"

res = requests.delete(api)

print(res.status_code)