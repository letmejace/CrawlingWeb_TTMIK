import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():

    # 가져올 페이지 주소
    req = requests.get('https://datalab.naver.com/')

    # HTML에 있는 코드 추출
    soup = BeautifulSoup(req.text, 'html.parser')

    myList = []

    for i in soup.select('span.title') :
        myList.append(i.get_text())

    return render_template("index.html", list = myList)

if __name__ == '__main__':
    app.run()