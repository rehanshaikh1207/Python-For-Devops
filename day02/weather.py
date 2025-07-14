# this is a project to get weather report of any city
import requests

class API:
    def api_check(self):
        url = "https://jsonplaceholder.typicode.com/posts"
        response = requests.get(url)
        if response.status_code == 200:
            print("Api is working")
        else:
            print("Api is not working")
    
    def api_weather(self, city):
        url = f'https://wttr.in/{city}'
        response = requests.get(url)
        print(response.text)

print('weather details of the city of your choice')
city = input("Enter the city:")
if not city:
    print("City name cannot be empty!")

api_a = API()
api_a.api_check()
api_a.api_weather(f'{city}')