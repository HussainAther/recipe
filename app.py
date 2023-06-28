import helpers

from flask import Flask, request, jsonify
from flask import session
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mxextjzb:QAYIJflQwwAKtSIDO6cdylZHy4HLOIYG@rajje.db.elephantsql.com/mxextjzb' 
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@hostname/database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
login_manager = LoginManager(app)
CORS(app)

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Recipe Model
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('recipes', lazy=True))

# Recipe Schema
class RecipeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'user_id')

recipe_schema = RecipeSchema()
recipes_schema = RecipeSchema(many=True)

# Routes
@app.route('/register', methods=['POST'])
def register():
    username = request.json['username']
    password = request.json['password']
    
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User registered successfully'})

@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']
    
    user = User.query.filter_by(username=username).first()
    if user and user.password == password:
        login_user(user)
        return jsonify({'message': 'Login successful'})
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logout successful'})

@app.route('/recipes', methods=['GET'])
@login_required
def get_recipes():
    recipes = Recipe.query.filter_by(user_id=current_user.id).all()
    return jsonify(recipes_schema.dump(recipes))

@app.route('/recipes/<int:recipe_id>', methods=['GET'])
@login_required
def get_recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    if recipe:
        return jsonify(recipe_schema.dump(recipe))
    else:
        return jsonify({'message': 'Recipe not found'}), 404

@app.route('/recipes', methods=['POST'])
@login_required
def create_recipe():
    title = request.json['title']
    description = request.json['description']
    
    new_recipe = Recipe(title=title, description=description, user_id=current_user.id)
    db.session.add(new_recipe)
    db.session.commit()
    
    return jsonify({'message': 'Recipe created successfully'})

@app.route('/recipes/<int:recipe_id>', methods=['PUT', 'POST'])
@login_required
def update_recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    if recipe:
        recipe.title = request.json['title']
        recipe.description = request.json['description']
        db.session.commit()
        return jsonify({'message': 'Recipe updated successfully'})
    else:
        return jsonify({'message': 'Recipe not found'}), 404

@app.route('/recipes/<int:recipe_id>', methods=['DELETE'])
@login_required
def delete_recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    if recipe:
        db.session.delete(recipe)
        db.session.commit()
        return jsonify({'message': 'Recipe deleted successfully'})
    else:
        return jsonify({'message': 'Recipe not found'}), 404

@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        user_id = session['user_id']
        username = session['username']
        # Access other user-specific session variables as needed
        return render_template('dashboard.html', username=username)
    else:
        return redirect(url_for('login'))

@app.route('/create', methods=['POST'])
def create():
    # Validate input data using the helper function
    if not helpers.validate_input(request.form.get('data')):
        return helpers.handle_error('Invalid input')

    # Format data using the helper function
    formatted_data = helpers.format_data(request.form.get('data'))

    # Perform other operations

    return redirect(url_for('success'))

if __name__ == '__main__':
    app.run(debug=True)

