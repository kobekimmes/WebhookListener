from flask import Flask, request

whl_app = Flask(__name__)


@whl_app.route('/api/v1/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        payload = request.json
        print(payload)
        return 0


whl_app.run(host='0.0.0.0', port=8000)


