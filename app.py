from flask import Flask, render_template, request, session, redirect, url_for
app = Flask(__name__)
app.secret_key = "super-secret-key"
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['logged_in'] = True
        return redirect(url_for('dashboard'))
    return render_template('login.html')
@app.route('/dashboard')
def dashboard():
    if 'logged_in' in session and session['logged_in'] == True:
        return render_template('loggedout.html')
    else:
        return redirect(url_for('login'))
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))
if __name__=='__main__':
    app.run(debug=True)
