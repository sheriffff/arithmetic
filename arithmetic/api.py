from flask import Flask
from arithmetic import routes

app = Flask(__name__)

if __name__ == '__main__':
    app.run()