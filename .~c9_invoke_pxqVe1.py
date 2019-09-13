import os
from flask import Flask, render_template, redirect, request, url_for ,request, redirect, session, g, flash
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from flask import request
from flask_bcrypt import bcrypt

app = Flask(__name__)
app.secret_key=os.urandom(24)


app.config["MONGO_DBNAME"] = 'online_cookbook'
app.config["MONGO_URI"] = "mongodb+srv://root:root123456@myfirstcluster-jkztf.mongodb.net/online_cookbook?retryWrites=true&w=majority"


mongo = PyMongo(app)

# MongoDB collections

users_collection = mongo.db.users
recipes_collection = mongo.db.recipes
categories_collection = mongo.db.categories

@app.route('/<category_name>', methods=['GET'])
def filter_list(category_name):
    categories = list(categories_collection.find())
    category_name = categories_collection.find_one(
        {'category_name': category_name})
    recipes = recipes_collection.find()
    return render_template(
        'filter.html',
        categories=categories,
        category_name=category_name,
        recipes=recipes)



@app.route('/', methods=["GET", "POST"])
def index():
    """
    Main welcome page with option to search, add or browse recipes.
    """
    if request.method == "POST":
        if request.form['action'] == 'search':
            search_term = request.form['search']
            if search_term == "":
                flash("Please enter a value to search")
                return redirect(url_for('recipe'))
            for i in search_term:
                if not i.isalnum():
                    search_term= search_term.replace(i, "-")
            return redirect(url_for('search', search_term= search_term))
                                    
                                    
    return render_template("index.html")
"""
Login/User sessions
"""
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        existing_user = users_collection.find_one(
            {'name': request.form.get('username')})
        if existing_user:
            session['username'] = request.form.get('username')
            return redirect('/loggedin/' + session['username'])
        return redirect(url_for('signup'))
    return render_template('login.html')
    
    
@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        existing_user = \
            users_collection.find_one(
                {'name': request.form.get('username')})
        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form.get('password')
                                     .encode('utf-8'), bcrypt.gensalt())
            users_collection.insert(
                {'name': request.form.get('username'), 'password': hashpass})
            session['username'] = request.form.get('username')
            return redirect('/loggedin/' + session['username'])
    return render_template('signup.html')
    
@app.route('/loggedin/<username>', methods=['GET', 'POST'])
def loggedin(username):
    recipes = \
        recipes_collection.find({'added_by': session['username']})\
        .sort('name', pymongo.ASCENDING)
    return render_template(
        'profile.html',
        username=session['username'],
        recipes=recipes
        )
        
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

"""
Recipe Create/Update/Delete Methods

"""    
@app.route('/recipe/<recipe_id>', methods=['GET', 'POST'])
def recipe_page(recipe_id):
    """Route to show single recipe view page"""
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('single_recipe.html', recipe=recipe)
    
    

@app.route('/get_recipes')
def get_recipes():
     return render_template("recipes.html",
     recipes= mongo.db.recipes.find())
       



@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html", 
    recipes= mongo.db.recipes.find())
    
    
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
   recipes =  mongo.db.recipes
   recipes.insert_one(request.form.to_dict())
   return redirect(url_for('get_recipes'))



"""
Category adding
"""

@app.route('/categories')
def categories():
    categories = \
        categories_collection.find().sort('category_name', pymongo.ASCENDING)
    return render_template('categories.html', categories=categories)

@app.route('/add_category ')
def add_category():
    return render_template("add_category.html")

@app.route('/insert_category', methods=['POST'])
def insert_category():
    category_doc = {'category_name': request.form['category_name']}
    categories_collection.insert_one(category_doc)
    return redirect(url_for('categories'))

@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    categories_collection.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('categories'))

@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    return render_template('editcategory.html',
                           category=categories_collection.find_one(
                               {'_id': ObjectId(category_id)}
                               ))


@app.route('/update_category/<category_id>', methods=['POST'])
def update_category(category_id):
    categories_collection.update(
        {'_id': ObjectId(category_id)},
        {'category_name': request.form['category_name']})
    return redirect(url_for('categories'))
     
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)