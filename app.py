import os.path
import sqlite3
from bottle import redirect, request, route, run, template, debug

DB = 'carpool.db'


def create_db():
    """Create database file if it doesn't exist already.

    """
    if os.path.exists(DB):
        return
    conn = sqlite3.connect(DB)
    conn.execute("CREATE TABLE carpool ("
                 "id INTEGER PRIMARY KEY, "
                 "name char(100) NOT NULL, "
                 "date text, "
                 "num int(5) NOT NULL)")
    conn.commit()


@route('/')
def index():
    """Show list of drivers and date last driven.

    """
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT name, date, num FROM carpool ORDER BY date desc")
    drivers = c.fetchall()
    c.close()
    return template('make_table.tpl', rows=drivers)


@route('/update_driver/<driver>', method="GET")
def update_driver(driver):
    """Update database for driver clicked with current date.

    """
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("UPDATE carpool SET date=datetime('now'), "
              "num=num+1 WHERE name=?", (driver,))
    conn.commit()
    c.close()
    redirect("/")


@route('/add_driver', method='GET')
def add_driver():
    """Add a new driver to the database

    """
    if request.GET.get('save', '').strip():
        name = request.GET.get('name', '').strip()
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute("INSERT INTO carpool (name, num) "
                  "VALUES (?, 0)", (name,))
        conn.commit()
        c.close()
        redirect('/')
    else:
        return template('add_driver.tpl')


@route('/del_driver')
def del_driver():
    """Delete a driver from the database

    """
    pass


if __name__ == "__main__":
    create_db()
    debug(True)
    run(reloader=True)
    #remember to remove reloader=True and debug(True) when you move your
    #application from development to a production environment
