import endpoints
from endpoints import Controller
import sqlite3
import json

class Default(Controller):
    def GET(self):
       return 

    def POST(self, **kwargs):
        return

class Posts(Controller):
    def GET(self):
        conn = sqlite3.connect('blog.db')
        c = conn.cursor()
        c.execute('SELECT  * FROM posts') 
        json_string = json.dumps(c.fetchall())
        return json_string
        conn.close()