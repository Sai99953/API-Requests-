import requests
api = "https://fakestoreapi.com/products/2"

data = requests.get(api)
print(data.json())

print("_________Another__________")

# EX:2 GET
api=requests.get("http://localhost:3000/tablets")
a=api.json()

for post in a:
    print(post)




# Ex:3 DUMPS POST
import json #Json inbuilt module
api=""
sending_data ={"Id":1,"Name":"RealmeGT7","Ram":"12GB","Processor":"Dimencity 94","Price":41000}
json_data=json.dumps(sending_data) # Dumps method converts the python objects into json code 
res=requests.post(api,data=json_data)
print(res)
print(res.json())



# EX:4 POST
# import json
# api = " "
# new_mobile = {"id":"5","Name":"s26","Ram":"12GB","Processor":"SPGen8s elite"}
# # #json_data=json.dumps(new.mobile)
# res=requests.post(api,json=new_mobile) # Json keyword converts data automatically
# print(res.json())



# PUT: PUT Can Create new one, and it removes old one
# Patch: It just update a value 

# Ex: 5 PUT
# import json
# api=" "
# data = {"Processor":"S8 GEN9"}
# res=requests.put(api,json=data)
# print(res.json())


# # Ex: 6 Patch
# import json
# api=" "
# data = {"Ram":"16GB"}
# res=requests.patch(api,json=data)
# print(res.json())


# Ex: 7 Delete
# api = " "
# res = requests.delete(api)
# print(res.json())