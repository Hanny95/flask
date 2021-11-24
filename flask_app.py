import matplotlib.pyplot as plt
import matplotlib
from flask import Flask, request, render_template, send_file
from io import BytesIO
from gangnam_ap import main, getData

matplotlib.use('Agg') # 쿠키와 상관없이 이미지 요청시 엑박 안뜸

app = Flask(__name__)

# 클라이언트의 요청이 들어오면 어떤 함수를 실행하라는 명령! -- > request
@app.route('/') # http://127.0.0.1:5000/
@app.route('/home')
def home():
    return 'hello flask!'

@app.route('/page1')
def page1():
    return 'This is page1.'

@app.route('/page1/page1_1')
def page1_1():
    return 'This is page1_1.'

@app.route('/user/<user_id>/<int:user_pw>/<float:user_height>')
def userInfo(user_id, user_pw, user_height):
    return f'user_id: {user_id}, user_pw : {user_pw}, user_height: {user_height}'

@app.route('/news/viewHTML/<date>')
def viewHtml(date):
    return f'''
        <h1>Today News</h1>
        <p>오늘 날짜 : {date}</p>
        <p>오늘은 영하 10도 입니다.</p>
    '''

@app.route('/naver/<date>')
def goNaver(date):
    return f'''
        <h1>Go to Naver Page</h1>
        <a href="/news/viewHTML/{date}" target="_blank">go naver</a>
    '''

@app.route('/google')
def goGoogle():
    return render_template('index.html')

@app.route('/myPage/<myID>/<myPW>')
def myPage(myID, myPW):
    return render_template('myPage.html', myID = myID, myPW = myPW)

@app.route('/form/userInfo')
def userInfo_():
    return render_template('form/userInfo.html')

# get, post, put, modify, delete <-- methods 방식
@app.route('/form/userInfoConfirm', methods=['post'])
def userInfoConfirm():

    u_id = ''
    u_pw = ''
    u_dongName = ''

    if (request.method == 'POST'): # 항시 대문자로 !
        # post 방식
        u_id = request.form.get('u_id')
        u_pw = request.form.get('u_pw')
        u_dongName = request.form.get('u_dongName')
    elif (request.method == 'GET'):
        # get 방식
        u_id = request.args.get('u_id')
        u_pw = request.args.get('u_pw')
        u_dongName = request.args.get('u_dongName')

    print(f'u_id {u_id}')
    print(f'u_pw {u_pw}')
    print(f'u_dongName {u_dongName}')

    return render_template('form/userInfoConfirm.html',
                           u_id = u_id,
                           u_pw = u_pw,
                           u_dongName = u_dongName)

@app.route('/matImg')
def matImg():
    xValues = [1, 2, 3, 4, 5]
    yValues = [1, 2, 3, 4, 5]

    plt.scatter(xValues, yValues)

    img = BytesIO()
    plt.savefig(img,
                format='png',
                dpi=300)
    img.seek(0)

    return send_file(img,
                     mimetype='image/png')

@app.route('/matImg2')
def matImg2():
    return render_template('matHtml.html')


@app.route('/getAptData')
def getAptData():


    img = BytesIO()
    getData(img)

    img.seek(0)

    return send_file(img,
                     mimetype='image/png')


@app.route('/getAptData2')
def getAptData2():
    return render_template('aptData.html')


if __name__ == '__main__':
    app.run(debug=True)

