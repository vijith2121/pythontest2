import requests
l=[]
for page in range(1,13):
    url = 'https://reqres.in/api/users?page=%s'%page
    user_side = requests.get(url)
    user = user_side.json()
    l.append(user)


print("first Page")
print(len(l[0]["data"]))

print("Second Page")
print(len(l[1]["data"]))

print("Third Page")
print(len(l[2]["data"]))

print("Fourth Page")
print(len(l[3]["data"]))

print("Fifth Page")
print(len(l[4]["data"]))





  
    

 
    


    