import requests
from flask import Flask, request

app= Flask(__name__)

@app.route('/hello',methods=['GET'])
def hello():
    if request.method=='GET':
        return('hello')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)