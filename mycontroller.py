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

class Post(Controller):
   def POST(self, **kwargs):
        conn = sqlite3.connect('blog.db')
        c = conn.cursor()
        c.execute('SELECT Count(*) FROM posts') 
        (post_id,) = c.fetchone()
        row = ( post_id,kwargs['title'], kwargs['body'])
        try:
           c.execute('INSERT INTO posts (post_id,title,body) VALUES(?,?,?)', row ) 
        except sqlite3.Error as e:
            print "An error occurred:", e.args[0]
        conn.commit()
        conn.close()
        return 'Posted blog id {}'.format(kwargs['title'])
