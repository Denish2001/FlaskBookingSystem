from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = '8c3b25fff694cf6cfb5f053ac8a57712'  # Necessary for flashing messages

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345678',
    database='booking'
)

@app.route('/')
@app.route('/flights')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/search_flights', methods=['POST'])
def search_flights():
    start = request.form['from']
    destination = request.form['destination']
    cursor = connection.cursor(dictionary=True)
    
    query = "SELECT * FROM flights WHERE `From` = %s AND `Destination` = %s"
    cursor.execute(query, (start, destination))
    results = cursor.fetchall()
    cursor.close()
    
    return render_template('index.html', results=results)

@app.route('/book_flight', methods=['POST'])
def book_flight():
    fullname = request.form['fullname']
    email = request.form['email']
    seatnumber = request.form['seatnumber']
    airline = request.form['airline']
    from_location = request.form['from']
    destination = request.form['destination']
    date = request.form['date']
    price = request.form['price']
    level = request.form['level']
    
    cursor = connection.cursor()
    query = """
        INSERT INTO bookedplanes (fullname, email, seatnumber, airline, from_location, destination, date, price, level)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (fullname, email, seatnumber, airline, from_location, destination, date, price, level))
    connection.commit()
    cursor.close()
    flash('Your booking was successful!', 'success')
    return redirect(url_for('index'))

@app.route('/hotels')
def hotel():
    return render_template('hotel.html')

@app.route('/search_hotel', methods=['POST'])
def search_hotel():
    city = request.form['city']
    cursor = connection.cursor(dictionary=True)
    
    query = "SELECT * FROM hotels WHERE city = %s"
    cursor.execute(query, (city,))
    results = cursor.fetchall()
    cursor.close()
    
    return render_template('hotel.html', results=results)

@app.route('/book_hotel', methods=['POST'])
def book_hotel():
    hotelname = request.form['name']
    roomnumber = request.form['roomnumber']
    phonenumber = request.form['phonenumber']
    email = request.form['email']
    date = request.form['date']
    city = request.form['city']
    price = request.form['price']
    size = request.form['size']
    fullname = request.form['fullname']
   
     
    cursor = connection.cursor()
    query = """
        INSERT INTO bookedrooms ( hotelname, roomnumber, phonenumber, email, date,  city, price, size, fullname )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (hotelname, roomnumber, phonenumber, email, date, city, price, size, fullname))
    connection.commit()
    cursor.close()
    flash('Your booking was successful!', 'success')
    return redirect(url_for('hotel'))

@app.route('/taxi')
def taxi():
    return render_template('taxi.html')

@app.route('/search', methods=['POST'])
def search():
    pickup_point = request.form['pickup_point']
    cursor = connection.cursor(dictionary=True)
    
    query = "SELECT * FROM taxi WHERE pickup = %s"
    cursor.execute(query, (pickup_point,))
    results = cursor.fetchall()
    cursor.close()
    
    return render_template('taxi.html', results=results)

@app.route('/book_taxi', methods=['POST'])
def book_taxi():
    pickup = request.form['pickup']
    destination = request.form['destination']
    size = request.form['size']
    price = request.form['Price']
    fullname = request.form['fullname']
    email = request.form['email']
    contact = request.form['contact']
    paymentmethod = request.form['paymentmethod']
    
    cursor = connection.cursor()
    query = """
        INSERT INTO bookedtaxis ( pickup, destination, size, price, fullname, email, contact, paymentmethod )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (pickup, destination, size, price, fullname, email, contact, paymentmethod ))
    connection.commit()
    cursor.close()
    flash('Your booking was successful!', 'success')
    return redirect(url_for('taxi'))


if __name__ == '__main__':
    app.run(debug=True)
