from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'result': 'hello via https'})

@app.route('/webhook', methods=['POST'])
def webhook():
    subprocess.run(['git', 'pull'], cwd='/path/to/repo')
    return '', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, ssl_context=('cert.pem', 'key.pem'), debug=True)
