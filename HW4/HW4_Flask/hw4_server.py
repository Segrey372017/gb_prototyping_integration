from flask import Flask, jsonify, request
import numpy as np
import json
import cv2
from PIL import Image
import os, sys
import secrets

workdir = os.path.dirname(sys.argv[0])
os.chdir(os.path.abspath(workdir))

app = Flask('__name__')

cnf = {}
with open('server_config/server_config.json', "r") as f:
    cnf = json.load(f)
print(cnf)


@app.route('/', methods=['GET', 'POST'])
def index():
    content = """
    <html> 
    <body>
    <h1> Welcome to homework 2 Flask server</h1>
    <p> Use client.py for sending requests</p>
    </body
    </html>
    """
    if request.method == "GET":
        return content

    return '<200>'


@app.route('/get_config', methods=['GET'])
def get_config():
    """
    Задание 1.
    Отдает данные файла конфигурации сервера
    """
    if request.method == 'GET':
        with open('server_config/server_config.json', 'r') as f:
            body = json.load(f)
            return jsonify({"answer": body["server"]})  # возвращаем только секцию "server" из файла конфигурации
    return


@app.route('/post_json', methods=['POST'])
def post_json():
    """
    Задание 2
    Принимает данные в формате json
    """
    if request.method == 'POST':
        data = request.get_json()
        if data != {}:  # проверяем пришли ли данные в json
            print(data)
            if "adress" in data.keys():  # если есть нужное поле
                return jsonify({"answer": "Данные получены",
                                "adress": data["adress"],
                                "id": data["id"]
                                })
    return


@app.route('/post_image', methods=['POST'])
def post_image():
    if request.method == 'POST':
        data = request.get_data()
        print(data)
        nparr = np.frombuffer(data, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        h, w, _ = img.shape
        print("height: ", h, "width: ", w)
        return jsonify({"height": h, "width": w})

    return


@app.route('/post_image2', methods=['POST'])
def post_image2():
    if request.method == 'POST':
        data = request.files["image"]
        img = Image.open(data)
        h, w = img.size
        print("h ", h, "w ", w)
        return jsonify({"height": h, "width": w})

    return


@app.route('/show_image', methods=['GET'])
def get_image(img):
    if request.method == 'GET':
        if img != None:
            return f"<img> {img} </img>"

    return


@app.route('/login', methods=['GET', 'POST'])
def login():
    token = secrets.token_hex(12)
    if request.method == 'POST':
        data = request.get_json()
        if data != {}:
            print("Пришли данные")
            with open('server_config/server_config.json', 'r') as f:
                config = json.load(f)
                if config["user"]["login"] == data["login"]:
                    if config["user"]["pass"] == data["pass"]:
                        print("Возращаем токен")
                        return jsonify({"token": str(token)})

    return


if __name__ == '__main__':
    app.run(host=cnf["server"]["host"],
            port=cnf["server"]["port"])