from flask import Flask, request, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Here you would typically check the credentials against a database
        if username == 'admin' and password == 'password':
            return "Login successful!"
        else:
            return "Invalid credentials, please try again."
    return render_template('Login_page.html')
if __name__ == '__main__':
    app.run(debug=True)