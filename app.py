from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "Welcome to the Dockerized Flask App!"
@app.route('/about')
def about():
    return "This is a scalable app powered by Flask, Docker, and Nginx!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
