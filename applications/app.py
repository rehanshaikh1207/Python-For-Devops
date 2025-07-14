from flask import Flask
from flask import Response

app = Flask(__name__)
@app.route("/")
def hello():
    return Response("The server is up and running")

if __name__ == '__main__':
    print("this will only run when i execute app.py")
    app.run()
