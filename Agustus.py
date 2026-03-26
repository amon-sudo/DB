from flask import Flask, sqlite3, requets
DATABASE_DATA = "base.db"

def get_db():
    conn = sqlite3.connect("base.db")
    conn.row_factory = sqlite3.Row
    return conn 


def anzaDb():
    kk = get_db
    
    
    kk.commit()
    kk.close()