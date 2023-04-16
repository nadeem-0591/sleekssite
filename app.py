
# Set up route for the login page
# Import required libraries
from flask import Flask, render_template, request

# Create Flask app instance
app = Flask(__name__)

# Set up route for the login page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Allow any username and password combination
        return 'Logged in successfully!'
    return render_template('login.html')

if __name__=='__main__':
    

    app.run(debug=True)
