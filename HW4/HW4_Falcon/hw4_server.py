import os, sys
import json
import falcon
import numpy as np
import cv2
from PIL import Image
import secrets

class Index:
    """
    Приветствие сервиса
    """
    def on_get(self, req, resp):
        resp.text = "<h1> Welcome hw3 falcon web server</h1>"
        resp.render_body()
        resp.status = falcon.HTTP_200

        return

class Config:
    def on_get(self, req, resp):
        """
        Задание 1
        Метод для отправк данных в json
        """
                
        with open('server_config/config.json', 'r') as f:
            body = json.load(f)
            resp.text = json.dumps(body["service"])
            resp.status = falcon.HTTP_200
            
        return

class PostJson:
    def on_post(self, req, resp):
        """
        Задание 2 получить и обработать данные в json
        """
        data = req.media
        if data != {}: # проверяем пришли ли данные в json
            print(data)
            if "adress" in data.keys(): # если есть нужное поле
                resp.text = json.dumps({"answer": "Данные получены",
                            "adress": data["adress"],
                            "id": data["id"]
                           })
                resp.status = falcon.HTTP_200
        
        return
        

class PostImage:
    def on_post(self, req, resp):

        data = req.stream.read()
        nparr = np.frombuffer(data, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        h, w, _ = img.shape
        print("height: ", h, "width: ", w)
        resp.text = json.dumps({"height": h, "width":w})
        resp.status = falcon.HTTP_200
        return

class PostImage2:
    def on_post(self, req, resp):

        data = req.stream
        img = Image.open(data)
        w, h = img.size
        print("height: ", h, "width: ", w)
        resp.text = json.dumps({"height": h, "width":w})
        resp.status = falcon.HTTP_200
        return

class GetToken:
    def on_post(self, req, resp):
        token = secrets.token_hex(12)
        data = req.media
        if data != {}:
            print("Пришли данные")
            with open('server_config/config.json', 'r') as f:
                config = json.load(f)
                if config["user"]["login"] == data["login"]:
                    if config["user"]["pass"] == data["pass"]:
                       print("Возращаем токен")
                       resp.text= json.dumps({"token": str(token)})
                       resp.status = falcon.HTTP_200
        return

        


service = Index()
getcnf = Config()
post_json = PostJson()
image1 = PostImage()
image2 = PostImage2()
g_token = GetToken()

app = application = falcon.App()
app.add_route("/", service)
app.add_route("/get_config", getcnf)
app.add_route("/post_json", post_json)
app.add_route("/post_image", image1)
app.add_route("/post_image2", image2)
app.add_route("/login", g_token)

# gunicorn --reload hw3.hw3_server
# waitress-serve --host=127.0.0.1  --port=8000 hw4_server:app