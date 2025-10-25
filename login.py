from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')  # make sure your HTML file is in /templates/

# Chatbot route
@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')  # or return same index if chatbot is part of it

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # Do your authentication logic here
        if username == 'admin' and password == 'admin':  # just a sample
            return redirect(url_for('chatbot'))
        else:
            return "Invalid credentials"
    return render_template('login.html')  # this should be your login page

if __name__ == '__main__':
    app.run(debug=True)
