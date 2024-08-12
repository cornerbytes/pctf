from flask import Flask, render_template, session, request, flash, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'random.random(12)'
FLAG = 'PCTF{FAKEFLAG}'


@app.get('/dashboard')
def dashboard():
    # onyl admin user can access the flag
    try:
        if 'admin' in session['username']:
            return render_template('index.html', flag=FLAG)
        else:
            return render_template('index.html')
    except:
        return redirect(url_for('login'))


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if (username == 'guest') and (password == 'guest'):
            flash('login success')
            session['username'] = 'guest'
            return redirect(url_for('dashboard'))
        else:
            flash('invalid username or password')
            return redirect(url_for('login'))
    return render_template('login.html')


@app.get('/logout')
def logout():
    session.pop('username', default=None)
    flash("Logout success")
    return redirect(url_for('login'))


@app.route('/')
def root():
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=False, port=8888)
