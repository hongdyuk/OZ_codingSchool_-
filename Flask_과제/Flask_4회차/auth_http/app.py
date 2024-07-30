from flask import Flask, render_template
from flask_httpauth import HTTPBasticAuth #pip install flask_httpauth

app = Flask(__name__)
auth = HTTPBasticAuth()

users = {
    'admin':'secret',
    'guest':'pw123'
}

@auth.verify_password
def verify_password(username, password):
    if username in users and password==users[username] == password:
        return username

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/protected')
@auth.login_required
def protected():
    return render_template('secret.html')

if __name__ == '__main__':
    app.run(debug=True)