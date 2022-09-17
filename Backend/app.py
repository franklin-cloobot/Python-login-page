from flask import Flask, render_template, request
import psycopg2
app = Flask(__name__)
@app.route("/", methods=['GET','POST'])
def login()
	conn = psycopg2.connect(database = "Task-1-Cloobot", user = "postgres", password = "Sairam", host = "localhost", port = "5432")
	cur = conn.cursor()
	cur.execute('select * from cloobot_employee;')
	conn.commit()
	cur.close()
	conn.close()

if __name__ == "__main__":
    app.run(debug=True)