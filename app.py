from flask import Flask, render_template, request, redirect, url_for, jsonify
from models import db, Game

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///steam.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()


# 🔵 Браузерний інтерфейс

@app.route('/')
def index():
    games = Game.query.all()
    return render_template('index.html', games=games)

@app.route('/add', methods=['GET', 'POST'])
def add_game():
    if request.method == 'POST':
        game = Game(
            name=request.form['name'],
            genre=request.form['genre'],
            developer=request.form['developer'],
            year=int(request.form['year']),
            rating=float(request.form['rating']),
            price=float(request.form['price'])
        )
        db.session.add(game)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_game.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_game(id):
    game = Game.query.get(id)
    if request.method == 'POST':
        game.name = request.form['name']
        game.genre = request.form['genre']
        game.developer = request.form['developer']
        game.year = int(request.form['year'])
        game.rating = float(request.form['rating'])
        game.price = float(request.form['price'])
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit_game.html', game=game)

@app.route('/delete/<int:id>')
def delete_game(id):
    game = Game.query.get(id)
    db.session.delete(game)
    db.session.commit()
    return redirect(url_for('index'))



@app.route('/api/games', methods=['POST'])
def api_add_game():
    data = request.get_json()
    try:
        new_game = Game(
            name=data['name'],
            genre=data.get('genre'),
            developer=data.get('developer'),
            year=data.get('year'),
            rating=data.get('rating'),
            price=data.get('price')
        )
        db.session.add(new_game)
        db.session.commit()
        return jsonify({'message': 'Гру додано успішно!', 'id': new_game.id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
