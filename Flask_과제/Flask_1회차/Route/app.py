from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello This is Main Page!'

@app.route('/about')
def about():
    return 'This is About Page!'

@app.route('/user/<username>')
def user_profile(username):
    return f'UserName : {username}!'

@app.route("/submit/methods=['GET','POST','PUT','DELETE']")
def submit(username):
    print(request.method)
    return ''

if __name__ == '__main__':
    app.run()