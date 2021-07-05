from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)



@app.route("/")
def home():
    return render_template('home.html')

@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/see", methods=['GET', 'POST'])
def see():
    file_path = ""
    tableName = ""
    column_names = []
    length = 0
    rows = []
    
    if request.method == 'POST':
        file_path = request.form['file-path']
        tableName = request.form['table-name']
        conn = sqlite3.connect(file_path)
        curs = conn.cursor()
        command = "SELECT * FROM " + tableName
        curs.execute(command)
        rows = curs.fetchall()
        column_names = [ description[0] for description in curs.description]
        length = len(column_names)
        
        curs.close()
        conn.commit()
        conn.close()
    print("file Path : " + file_path)
    return render_template('see.html',db_path=file_path,column_names=column_names,length=length,rows=rows)
        

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/delete")
def delete():
    return render_template("delete.html")


@app.route("/edit")
def edit():
    return render_template("edit.html")




if __name__ == "__main__":
    app.run(debug=True)

