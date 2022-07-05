import requests
import numpy as np
from PIL import Image
import cv2
import json

SERVER ="http://localhost:8000"     # "0.0.0.0"
PORT = "8889"


def main(m):
    """
    Функционал меню для запуска запросов
    """
    req = { 1: get_config,
            2: post_json,
            3: post_image1,
            4: post_image2,
            5: get_token,
            0: exit
       }

    if m in [0, 1, 2, 3, 4, 5]:
        req[m]()
    
    return

def get_config():
    """
    Отправляет GET запрос на получение данных конфигурации сервера
    """
    
    ans = requests.get(SERVER+"/get_config")
    return print ("Ответ сервера", ans.json())
    
    pass

def post_json():
    """
    Отправляет POST запрос на сервер. Передает метаданные фотографии
    в json
    """
    body = {"id": "000001",
            "adress": "ул. Менделеева",
            "long": "42.119412",
            "alt": "57.46057"}

    ans = requests.post(SERVER+"/post_json",
                       json = body,
                       headers = {"Content-Type": "application/json"})
    
    return print(ans.json())
        
    

def post_image1():
    """
    Отправляет POST запрос. Передает изображение на сервер.
    Изображение перед передачей кодируется в массив numpy
    с помощью библиотеки OpenCV
    """
    img_data = cv2.imread('road.jpg')
    print("image shape", img_data.shape)
    _, img_encoded = cv2.imencode('.jpg',img_data)
    ans = requests.post(SERVER+"/post_image",
                        data = img_encoded.tobytes())
                    
    print(ans)
    print(ans.json())
    return 

def post_image2():
    """
    Отправляем POST запрос с картинкой. Картинка направляется 
    как файл
    """
    with open('road.jpg', 'rb') as f:
        ans = requests.post(SERVER+"/post_image2",
                           data= f)
      
        print(ans.json())
    return  

def get_token():
    body = {"login": "log",
           "pass": "pass"}
    ans = requests.post(SERVER+"/login", 
                      json = body)    
    return print(ans.json()) # вернется словарь со значением токена

if __name__ == "__main__":
    while True:
        content = """
        Выберите желаемое действие:
        1. Вернуть часть конфига
        2. Отправить данные в json
        3. Отправить картинку (способ1)
        4. Отправить картинку (способ2)
        5. Получить токен
        0. Выйти
        """
        print(content)
        choice = int(input("Выберите действие: "))
        main(choice)