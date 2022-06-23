import requests
import json
from PIL import Image


def send_request():
    headers =  {'content-type': 'application/json; charset=utf-8'} # заголовки для правильной интерпритации запроса сервером
    turns= ['rock', 'paper', 'scissors']
    #avatar = Image.open('panda.jpg')
    body = {} # тело запроса
    body['username'] = input('Введите ваше имя: ')
    print('Введите цифру чтобы сделать ход')
    t = int(input('(0 - камень; 1 - бумага; 2 - ножницы : '))
    print('Ваш выбор: ', t)
    if t in [0, 1, 2]:
        body['turn'] = turns[t]
    else:
        print("Указано неверное значение")
        exit()

    resp = requests.post(url = 'https://prototypinghw1.sergey372017.repl.co/', 
                 json = body,
                 headers = headers)

    print (resp)
    
    
    return resp.json()

if __name__ == '__main__' :
    print(send_request())