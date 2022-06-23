from flask import Flask
from flask import request, jsonify
import random
from PIL import Image


server_app = Flask(__name__)

@server_app.route('/', methods = ['POST', 'GET'])
def index():
    content = """
    <h1> Welcome!!! </h1>
    <h3> You inter in "Rock, paper, scissors" game server </h3>
    <p> Use client.py for sending game requests </p>
    
    """
    

    if request.method == 'GET':
        return content
        

    if request.method == 'POST':
        user_data = request.get_json()
        print(user_data)
        return make_game(user_data)
        
        
    return
          
def make_game(data):
    """
    Случайным образом выбирает один из трех ходов компьютера 
    'rock', 'paper', 'scissors' далее определяется победитель или 
    ничья
    """
    turns= ['rock', 'paper', 'scissors']
    cturn = random.choice(turns)
    print("Ход компьютера: ", cturn)
    resp = 'Что-то пошло не так'

    # определяем исходы
    c_wins = ['rockscissors', 'paperrock', 'scissorspaper']

    if cturn + data['turn'] in c_wins:
        resp = '<h2> Компьтер выиграл </h2>'
    else:
        resp = f"<h2> {data['username']}  выиграл </h2>"
        
    if cturn == data['turn']:
        resp = f"<h2> {data['username']} и компьютер сыграли в ничью </h2>"
    
    print(resp)
    return jsonify({'answer': resp})
    



if __name__ == '__main__':
    server_app.run('0.0.0.0', port = 8889)