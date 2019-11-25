import urllib.request

response = urllib.request.urlopen("http://placekitten.com/g/200/300")
cat_img = response.read()
with open("D:\\github\\python-room\\output\\cat_200_300.jpg", "wb") as f:
    f.write(cat_img)
