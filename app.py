from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def login():
    return render_template('hello.html')

@app.route('/authenticate', methods=['POST'])
def authenticate():
    if request.form['user']=='gary' and request.form['password']=='johnson':
        return render_template('login.html', result="Broccoli")
    else:
	return render_template('login.html', result="Wall")
if __name__ == '__main__':
    app.debug = True
    app.run()

