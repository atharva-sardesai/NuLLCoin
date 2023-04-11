from flask import Flask, render_template, flash , redirect, url_for, session, request, logging
from passlib.hash import sha256_crypt
from flask_mysqldb import MySQL
from sqlhelpers import *
from sqlConfig import *



@app.route("/")
def index():
    users = Table("users","name","email","username","password")
    users.insert("abc","abc","abc","abc")
    return render_template('index.html')

if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug = True)