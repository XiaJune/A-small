import http.cookies


cook = http.cookies.BaseCookie('name=Louis')
cook['age'] = 20
cook['favor'] = 0
for k, v in cook.items():
    print(k,v)

print(cook.output())