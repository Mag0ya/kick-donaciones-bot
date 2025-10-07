from flask import Flask, request
import pyautogui

app = Flask(__name__)

@app.route('/', methods=['POST'])
def recibir_donacion():
    data = request.json
    monto = data.get('amount', 0)

    # Si la donación es igual o superior a 1 (por ejemplo)
    if monto >= 1:
        pyautogui.press('a')
        pyautogui.press('a')
        print("¡Donación recibida! Presionando 'A' dos veces.")

    return {'status': 'ok'}, 200

@app.route('/', methods=['GET'])
def home():
    return "Bot activo", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
