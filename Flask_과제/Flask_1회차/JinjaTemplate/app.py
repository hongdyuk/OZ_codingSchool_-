from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    users = [
        {"username": "traveler", "name": "Donghyuk"},
        {"username": "photographer", "name": "Lee"},
        {"username": "gourmet", "name": "Kim"}
    ]
    # (1) redering할 html 파일명 입력
    # (2) html로 넘겨줄 데이터 입력
    return render_template("index.html", users=users)

if __name__ == '__main__':
    app.run(debug=True)