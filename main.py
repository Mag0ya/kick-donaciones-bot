from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(data)  # Aquí puedes hacer lo que quieras con los datos recibidos
    return '', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)