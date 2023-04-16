
from flask import Flask, render_template, request

# Create Flask app instance
app = Flask(__name__)

# Set up route for the login page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        
        return 'Logged in successfully!'
    return render_template('login.html')

if __name__=='__main__':
    

    app.run(debug=True)
