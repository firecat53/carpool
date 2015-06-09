#!/usr/bin/env python
import datetime
import sqlite3
from bottle import redirect, request, route, run, template, debug, static_file

DB = 'data/carpool.db'
CYCLE1_START = datetime.date(2015, 1, 4)
CYCLE2_START = datetime.date(2015, 1, 7)


def create_db():
    """Create database file if it doesn't exist already.

    """
    conn = sqlite3.connect(DB)
    conn.execute("CREATE TABLE IF NOT EXISTS carpool ("
                 "name char(25) PRIMARY KEY, "
                 "date text, "
                 "num int(4) NOT NULL, "
                 "position int(2) NOT NULL, "
                 "riding_next int(1), "
                 "next_shift text)")
    conn.commit()


@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='static')


@route('/')
def index():
    """Show list of drivers and date last driven.

    """
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    # Compare stored next shift with current next shift. Update next_shift for
    # all riders and clear the checkboxes.
    ns = c.execute("SELECT next_shift FROM carpool LIMIT 1").fetchone()[0]
    s = get_next_shift().strftime("%a, %b %d")
    if ns != s:
        c.execute("UPDATE carpool set riding_next=0, next_shift=?", (s,))
        conn.commit()
    c.execute("SELECT name, strftime('%Y-%m-%d', date), "
              "num, position, riding_next, next_shift "
              "FROM carpool ORDER BY position desc")
    drivers = c.fetchall()
    conn.close()
    return template('view/make_table.tpl', rows=drivers, shift=s)


@route('/update_driver/<driver>')
def update_driver(driver):
    """Update database for driver clicked with current date. Clear checkboxes
    for who will be carpooling the next shift.

    """
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("UPDATE carpool SET position=position+1")
    c.execute("UPDATE carpool SET date=datetime('now', 'localtime'), "
              "position=0, num=num+1 WHERE name=?", (driver,))
    conn.commit()
    conn.close()
    redirect("/")


@route('/update_rider/<rider>')
def update_rider(rider):
    """Toggle the values for who is riding next shift

    """
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("UPDATE carpool SET riding_next=NOT riding_next "
              "WHERE name=?", (rider,))
    conn.commit()
    conn.close()
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
        s = get_next_shift().strftime("%a, %b %d")
        c.execute("INSERT INTO carpool "
                  "VALUES (?, '', 0, ?+1, 0, ?)", (name, pos, s))
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


def date_generator(start, end):
    """Generate a range of dates from start to end

    """
    res = []
    while True:
        res.append(start)
        start += datetime.timedelta(days=8)
        if start < end:
            continue
        else:
            break
    return res


def get_next_shift():
    """Return the date of our next shift after today

    """
    today = datetime.date.today()
    end = today + datetime.timedelta(days=8)
    res = sorted(date_generator(CYCLE1_START, end) +
                 date_generator(CYCLE2_START, end))[-3:]
    if today not in res:
        res.append(today)
        res = sorted(res)
        return res[res.index(today) + 1]
    else:
        return res[res.index(today)]


if __name__ == "__main__":
    create_db()
    debug(False)
    run(reloader=False, host='0.0.0.0', port=8080)
