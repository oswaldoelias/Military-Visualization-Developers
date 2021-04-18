import requests; 

# response = requests.get("https://randomfox.ca/floof"); 
# # print(response.json());
# fox = response.json();
# print(fox['image']); 

city = input('Enter your city : ');

url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=935e2063c4da3de8f7008a245776dfe5".format(city);

res = requests.get(url);

data = res.json();

print(res);

print(data);