from flask import Flask, render_template, request, redirect, url_for, make_response
import uuid
app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    cookie = request.cookies.get('token')
    if (request.method == 'POST') or (cookie):
        token = uuid.uuid4().hex
        
        resp = make_response(redirect(url_for('out')))
        if not cookie:
            resp.set_cookie('token', token)
        return resp

    return render_template('login.html')

@app.route('/out')
def out():
    cookie = request.cookies.get('token')
    if cookie:
        return render_template('loggedout.html')
    else:
        return render_template('login.html')
    
@app.route('/logout')
def logout():
    resp = make_response(redirect(url_for('login')))
    resp.set_cookie('token',expires=0)
    return resp

if __name__=='__main__':
    app.run(debug=True)

