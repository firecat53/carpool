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
                 "name char(25) PRIMARY KEY, "
                 "date text, "
                 "num int(4) NOT NULL, "
                 "position int(2) NOT NULL)")
    conn.commit()


@route('/')
def index():
    """Show list of drivers and date last driven.

    """
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT * FROM carpool ORDER BY position desc")
    drivers = c.fetchall()
    c.close()
    return template('view/make_table.tpl', rows=drivers)


@route('/update_driver/<driver>', method="GET")
def update_driver(driver):
    """Update database for driver clicked with current date.

    """
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("UPDATE carpool SET position=position+1")
    c.execute("UPDATE carpool SET date=datetime('now'), "
              "position=0, num=num+1 WHERE name=?", (driver,))
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
        c.execute("SELECT MAX(position) FROM carpool")
        try:
            pos = int(c.fetchall()[0][0])
        except TypeError:
            pos = 0
        c.execute("INSERT INTO carpool (name, num, position) "
                  "VALUES (?, 0, ?+1)", (name, pos))
        conn.commit()
        c.close()
        redirect('/')
    else:
        return template('view/add_driver.tpl')


@route('/del_driver')
def del_driver():
    """TODO: Delete a driver from the database

    """
    pass


if __name__ == "__main__":
    create_db()
    debug(True)
    run(reloader=True)
    #remember to remove reloader=True and debug(True) when you move your
    #application from development to a production environment
