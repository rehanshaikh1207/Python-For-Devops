# api using classes
import requests

class Api_testing:
    def testing1(self):
        url = "https://jsonplaceholder.typicode.com/posts"
        response = requests.get(url)
        if response.status_code == 200:
            print("api is working")
        else:
            print("api is not working")


api1 = Api_testing()
api1.testing1()

