from flask import Flask, render_template, request

server = Flask(__name__)

class Person():

    name = None

    def say(self):
        return "hello i'm a person"

@server.route('/temp')
def temp():
    # dict = {'title':'我的第一个模板','bookName':'钢铁是怎样练成的',
    #         'author':'奥斯特洛夫斯基','price':32.5,'publisher':'北京大学出版社'}
    title = '我的第一个模板'
    bookName = '钢铁是怎样练成的'
    author = '奥斯特洛夫斯基'
    price = 32.5
    publisher = '北京大学出版社'
    list = ['金毛狮王','青衣福王','紫衫龙王','白眉鹰王']
    tup = ('刘德华','张学友','黎明','郭富城')
    dict = {'LW': '老魏', 'WWC': '隔壁老王',
             'LZ':'绿泽','PY':'皮爷'}

    per = Person()
    per.name = '漩涡名人'
    uname = 'uzuinko klsownc'
    return render_template('01_temp.html',params=locals())

@server.route('/request')
def request_views():
    scheme = request.scheme
    method = request.method
    args = request.args
    form = request.form
    values = request.values
    cookies = request.cookies
    path = request.path
    headers = request.headers

    ua = headers['User-Agent']

    #referer = request.headers['referer']
    referer = request.headers.get('referer','')

    return render_template('02_request.html',params=locals())

@server.route('/login')
def login():
    return '这里是登录页面'

if __name__ == '__main__':
    server.run(debug=True)