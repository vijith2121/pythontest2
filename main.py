import requests
l=[]
for page in range(1,13):
    url = 'https://reqres.in/api/users?page=%s'%page
    user_side = requests.get(url)
    user = user_side.json()
    l.append(user)


print("first Page")
print("total user : ",len(l[0]["data"]))

print("Second Page")
print("total user : ",len(l[1]["data"]))






  
    

 
    


    