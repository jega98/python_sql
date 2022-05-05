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
    field_names = [i[0] for i in c.description]
    return {"data": final_result, "coloum": field_names}

@app.route('/customers/insert')
def insert_customers():
    host = 'localhost'
    user = 'root'
    password = 'sivakavi'
    port = 3306
    db = 'my schema details'
    db = sql.connect(host = host, user = user, password = password, port = port, db = db)
    c=db.cursor()
    c.executemany(
          """INSERT INTO customers (customerNumber, customerName, contactFirstName, contactLastName, phone, addressLine1, addressLine2, city, state, postalCode, country, salesRepEmployeeNumber, creditLimit)
      VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
      [
      (573, "jevanathan", "ram", "jey", "9345470683", "sugunaStore", "annaNagar", "madurai", "tamilNadu", "cscsc x", "india", 1165, 1000000),
      ] )
      
    c.execute("""select * from customers""") 
    final_result = c.fetchall()
    field_names = [i[0] for i in c.description]
    return {"data": final_result, "coloum": field_names}

@app.route('/customers/update')
def update_customers():
    host = 'localhost'
    user = 'root'
    password = 'sivakavi'
    port = 3306
    db = 'my schema details'
    db = sql.connect(host = host, user = user, password = password, port = port, db = db)
    c=db.cursor()
    query = "UPDATE customers SET phone = '9788671743' WHERE customerNumber = '496'"
    c.execute(query)
    db.commit()  
    c.execute("""select * from customers""") 
    final_result = c.fetchall()
    field_names = [i[0] for i in c.description]
    return {"data": final_result, "coloum": field_names}

@app.route('/orders/delete/<int:orderID>')
def delete_orders(orderID):
    host = 'localhost'
    user = 'root'
    password = 'sivakavi'
    port = 3306
    db = 'my schema details'
    db = sql.connect(host = host, user = user, password = password, port = port, db = db)
    c=db.cursor()
    query = "DELETE FROM orders WHERE orderNumber ="+str(orderID)
    c.execute(query)
    db.commit()

    c.execute("""select * from orders""") 
    final_result = c.fetchall()
    field_names = [i[0] for i in c.description]
    return {"data": final_result, "coloum": field_names}

@app.route('/customers/<int:customerID>')
def get_customer(customerID):
    host = 'localhost'
    user = 'root'
    password = 'sivakavi'
    port = 3306
    db = 'my schema details'
    db = sql.connect(host = host, user = user, password = password, port = port, db = db)
    c=db.cursor()
      
    c.execute("""select * from customers where customerNumber ="""+str(customerID)) 
    final_result = c.fetchall()
    field_names = [i[0] for i in c.description]
    return {"data": final_result, "coloum": field_names}

@app.route('/employees/<int:employeeID>')
def get_employee(employeeID):
    host = 'localhost'
    user = 'root'
    password = 'sivakavi'
    port = 3306
    db = 'my schema details'
    db = sql.connect(host = host, user = user, password = password, port = port, db = db)
    c=db.cursor()
      
    c.execute("""select * from employees where employeeNumber ="""+str(employeeID)) 
    final_result = c.fetchall()
    field_names = [i[0] for i in c.description]
    return {"data": final_result, "coloum": field_names}


if __name__ == '__main__':
   app.run()