from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__, template_folder= "templates")

# conn = sql.connect("database.db")
# print(" Opened Database Successfully");

# conn.execute('CREATE TABLE Employee3(fname TEXT, addr TEXT, city TEXT, pin TEXT)')
# print("Table Created Sucessfully");
# conn.close()


@app.route('/')
def Home():
    return render_template('Home.html')


@app.route('/enter_new')
def New_Employee():
    return render_template('Employee.html')


@app.route('/addrec', methods = ['POST','GET'])
def addrec():
    if request.method == 'POST':
        try:
            fname = request.form['fname']
            addr = request.form['add']
            city = request.form['city']
            pin = request.form['pin']

            with sql.connect("database.db") as con:
                cur = con.cursor()

                cur.execute("INSERT INTO Employee2(fname, addr, city, pin) VALUES (?,?,?,?)", (fname, addr, city, pin))

                con.commit()
                msg = "Record added Successfully"
        except:
            con.rollback()
            msg = "Error in Insert Operation"

        finally:
            return render_template('result.html', msg = msg)
            con.close()


@app.route('/list')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("Select * from Employee2")

    rows = cur.fetchall();
    return render_template('list.html',rows = rows)


if __name__ == "__main__":
    app.run(debug=True)
