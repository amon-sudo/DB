from flask import Flask, request
from Caeser.Agustus import get_db
def user(username, password, who="user"):
   d= get_db()
   
   d.execute(
       "INSERT INTO users (username, password, who) VALUES (?, ?, ?)",
       (username, password, who)
   )
   d.commit()
   d.close()