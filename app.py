from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'inventory_db'
}

# Database connection function
def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        name = request.form['name']
        quantity = request.form['quantity']
        price = request.form['price']
        category = request.form['category']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute(
                "INSERT INTO items (name, quantity, price, category) VALUES (%s, %s, %s, %s)",
                (name, quantity, price, category)
            )
            conn.commit()
            flash('Item added successfully!', 'success')
        except Exception as e:
            flash(f'Error adding item: {str(e)}', 'error')
        finally:
            cursor.close()
            conn.close()
            
        return redirect(url_for('view_inventory'))
    
    return render_template('add_item.html')

@app.route('/inventory')
def view_inventory():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM items ORDER BY date_added DESC")
    items = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('view_inventory.html', items=items)

if __name__ == '__main__':
    app.run(debug=True) 