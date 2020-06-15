from flask import Flask, render_template, request,redirect,url_for
from werkzeug.routing import BaseConverter

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
    url = url_for('request_views')
    return redirect(url)

@server.route('/h1')
@server.route('/h2')
def hello():
    return 'hello 1'

@server.route('/user/<int:user_id>')
def user(user_id):

    return 'user detail page %s' %user_id

#定义自己的转换器
class MobileConverter(BaseConverter):

    def __init__(self,url_map):
        super().__init__(url_map)
        self.regex = '1[34578]\d{9}'


#定义自己的转换器
class RegexConverter(BaseConverter):

    def __init__(self,url_map,regex):
        #调用父类的初始化方法
        super().__init__(url_map)
        #将正则表达式的参数保存到对象的属性中，flask会去使用这个属性来进行路由的正则匹配
        self.regex = regex

#将自定义的转换器添加到flask的应用中
server.url_map.converters['re'] = RegexConverter

@server.route("/send/<re('1[34578]\d{9}'):mobile>")
def send_smg(mobile):
    return 'send smg to %s' %mobile


if __name__ == '__main__':
    server.run(debug=True)