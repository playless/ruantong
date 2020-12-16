from flask import Flask, request, render_template

app=Flask(__name__)
@app.route('/')
def hello():
    return "hello"
@app.route('/s/')
def so():
    wd=request.args.get('wd')
    return '通过查询搜索的关键字为：{0}'.format(wd)

@app.route('/login/',methods=['GET','POST'])
def login():
    content={'msg':None}
    if request.method=='GET':
        return render_template('login.html')
    if request.method=='POST':
        username=request.form.get('username',None)
        password=request.form.get('password',None)
        if username=='wuya' and password=='admin':
            return '登录成功'
if __name__ == '__main__':
    app.run(debug=True)