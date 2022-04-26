from flask import Flask
import MySQLdb as sql
app = Flask(__name__)

@app.route('/customers')
def get_customers():
    host = 'localhost'
    user = 'root'
    password = 'sivakavi'
    port = 3306
    db = 'my schema details'
    db = sql.connect(host = host, user = user, password = password, port = port, db = db)
    c=db.cursor()
    c.execute("""select * from customers""") 
    final_result = c.fetchall()
    num_fields = len(c.description)
    field_names = [i[0] for i in c.description]
    return {"data": final_result, "coloum": field_names}

if __name__ == '__main__':
   app.run()