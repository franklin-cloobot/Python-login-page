from flask import Flask, request, session, redirect, url_for, render_template, flash
import psycopg2 #pip install psycopg2 
import psycopg2.extras
import re 
from werkzeug.security import generate_password_hash, check_password_hash
 
app = Flask(__name__)
conn = psycopg2.connect(database = "Task-1-Cloobot", user = "postgres", password = "Sairam", host = "localhost", port = "5432")
cur = conn.cursor()
@app.route('/login', methods=["GET","POST"])
def login():
		if request.method=='post' and 'username' in request.form and 'password' in request.form:
			username = request.form['username']
			password = request.form['password']
			print(password)
         	# Check if account exists using MySQL
        	cursor.execute('SELECT * FROM cloobot_employee WHERE username = %s', (username,))
        	# Fetch one record and return result
        	account = cursor.fetchone()

        	if account:
        		password_rs = account['password']
            	print(password_rs)
            	if check_password_hash(password_rs, password):
                	return redirect("./fronted/src/app/dashboard/dashboard.component.ts")
            	else:
                	# Account doesnt exist or username/password incorrect
                	flash('Incorrect username/password')
        	else:
            	# Account doesnt exist or username/password incorrect
            	flash('Incorrect username/password')

if __name__ == "__main__":
    app.run(debug=True)