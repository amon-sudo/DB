

from flask import Flask, request, session
from Agustus import get_db

def login():
    d = get_db()
    customer = d.execute(
        "SELECT * FROM Users WHERE username = ?",
        (request.form.get("username"))
        ).fetchone()
    d.close()
    if customer["password"] == request.form.get("password") :
        session["user_id"] = customer["id"]
        session["who"] = customer["who"]
        return customer
    return None

def isLogged():
    return "customer_id" in session


def admin():
    return session.get("who") == "admin"