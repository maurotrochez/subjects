from flask import Flask
from werkzeug.contrib.fixers import ProxyFix
from app import create_app

app = Flask(__name__)
app = create_app(app)
app.wsgi_app = ProxyFix(app.wsgi_app)

# @app.route('/')
# def hello_world():
#     return 'Hello World!'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
