import csv
import hashlib
from flask import Flask, render_template, request
app = Flask(__name__)

def searchUser(l, target):
    x=0
    while x<len(l):
        if l[x][0]==target:
            return x
        x+=1
    return -1

@app.route('/')
def login():
    return render_template('hello.html')

@app.route('/auth', methods=['POST'])
def auth():
    action=request.form.get('action')
    if action=="login":
        f=open('passwords.csv','r')
        accounts=f.read()
        rows=accounts.split('\n')
        counter=0
        while counter < len(rows):
            rows[counter]=rows[counter].split(',')
            counter+=1
            #creats list of user-pass pairs in the format of a list of lists
        if (searchUser(rows, request.form["user"])==-1):
            return render_template('login.html', result="User DNE")
            #user does not exist if not in rows
        else:
            m=hashlib.sha1()
            m.update(request.form['password'])
            hashedP=m.hexdigest()
            if (hashedP==rows[searchUser(rows, request.form['user'])][1]):
                return render_template('login.html', result="Logged in")
            else:
                return render_template('login.html', result="Wrong Password")
        f.close()
                #changing variable dependent on login status
                
    if action=="register":
        f=open('passwords.csv','r+')
        accounts=f.read()
        rows=accounts.split('\n')
        counter=0
        while counter < len(rows):
            rows[counter]=rows[counter].split(',')
            counter+=1
        if searchUser(rows, request.form['user'])==-1:
            m=hashlib.sha1()
            m.update(request.form['password'])
            hashedP=m.hexdigest()
            accounts+="\n"+request.form['user']+','+hashedP
            f.write(accounts)
            f.close()
            return render_template('hello.html', result="Successfully Created New Account")
        else:
            return render_template('hello.html', result="Username is Taken")

        
if __name__ == '__main__':
    app.debug = True
    app.run()

