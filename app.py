#!/usr/bin/env python
import sqlite3
from bottle import redirect, request, route, run, template, debug

DB = 'carpool.db'


def create_db():
    """Create database file if it doesn't exist already.

    """
    conn = sqlite3.connect(DB)
    conn.execute("CREATE TABLE IF NOT EXISTS carpool ("
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
    c.execute("SELECT name, strftime('%Y-%m-%d', date), num, position "
              "FROM carpool ORDER BY position desc")
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
    c.execute("UPDATE carpool SET date=datetime('now', 'localtime'), "
              "position=0, num=num+1 WHERE name=?", (driver,))
    conn.commit()
    c.close()
    redirect("/")


@route('/admin')
def admin():
    """Admin page to add/remove driver and clear database

    """
    return template('view/admin.tpl')


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


@route('/del_driver', method='GET')
def del_driver():
    """TODO: Delete a driver from the database

    """
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    name = request.GET.get('name', '').strip()
    if name:
        c.execute("DELETE FROM carpool WHERE name=?", (name,))
        conn.commit()
        redirect('/admin')
    else:
        c.execute("SELECT name FROM carpool")
        drivers = [i[0] for i in c.fetchall()]
        c.close()
        return template('view/del_driver.tpl', rows=drivers)


@route('/reset_db')
def reset_db():
    """Delete _all_ database information.

    """
    conn = sqlite3.connect(DB)
    conn.execute("DROP TABLE carpool")
    conn.commit()
    create_db()
    redirect('/admin')


if __name__ == "__main__":
    create_db()
    debug(False)
    run(reloader=False, host='0.0.0.0')
