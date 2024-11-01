from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'  


tours = []


@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        tour = request.form['tour']
    
        flash(f'Дякуємо за бронювання, {name}! Ви забронювали тур "{tour}".')
        return redirect(url_for('booking'))
    return render_template('booking.html', tours=tours)


@app.route('/add_tour', methods=['GET', 'POST'])
def add_tour():
    if request.method == 'POST':
        tour_name = request.form['tour_name']
        description = request.form['description']
        price = request.form['price']
      
        tours.append({'name': tour_name, 'description': description, 'price': price})
        flash(f'Тур "{tour_name}" успішно доданий!')
        return redirect(url_for('add_tour'))
    return render_template('add_tour.html')

if __name__ == '__main__':
    app.run(debug=True)