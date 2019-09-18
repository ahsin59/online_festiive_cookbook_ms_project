# online_festiive_cookbook_ms_project
## UX

I created an application called ONLINE COOKBOOK that allows user to store and easily access recipes.
The app is a recipe Festival that will store all your Festive and occasional recipes in one place! It allow the user
to read recipe, create new recipe, edit and delete them (CRUD).
As a user you can:

* view the app on your preferred device (mobile, tablet, desktop)
* create your own recipe and add to the website
* edit the recipes
* delete the recipes
* see card of all recipes
* see a list of all recipes
* search for recipes by choosen category
* register to the application with username and password
* login to the application with username and password
* Msnsge cstegoris by
* create new categories
* edit categories
* delete categories
* update categories

### Design

I created this website using  Materialize CSS. This app contain register page where new user is able to register, login page where user is able to login, home page
with navbar, buttons, and lists of recipes when clicked it will lead to individual recipe page.
when you want to add new recipes and also new categories you need to Register first when you register then you will have to Login in app
your username your email and password then you will enter the Result of data page in this page you can edit or delete the recipes 
also add recipes and manage, add , update and delete categories

## WIREFRAMES
step by step i Demonstrate the user stories  how this application work


### wireframes for desktop
* Ist step of all is Home page in Desktop  Preview  show my App
![Home-Desktop](https://user-images.githubusercontent.com/38302279/65088841-c8560f00-d9b2-11e9-9091-a6c18e5c4f8e.png)
### wireframes for mobile
* 2nd  is Home page in Mobile Preview show my App
![Home-Mobile](https://user-images.githubusercontent.com/38302279/65088945-1834d600-d9b3-11e9-9daf-edc02e29af55.png)
### Singnup
* 3rd  step user need to signup my app if user want to add his on Recipe,categories and cuisines
 ![Singnup](https://user-images.githubusercontent.com/38302279/65088976-40bcd000-d9b3-11e9-855e-d8d6c1f06069.png)
### signin
* 4th step a fter signup user need to Signin to enter the Add_Recipe,Categories and Cuisines and also Result page
![SignIn](https://user-images.githubusercontent.com/38302279/65089462-f851e200-d9b3-11e9-8628-1a3aa62e2f7f.png)
### Recipe
*5th step user want to see the Recipe in apps user can see the Recipes without Login the app 
![Recipe](https://user-images.githubusercontent.com/38302279/65095638-f4c15980-d9b9-11e9-9487-279142ff0e6c.png)
### Add_Recipe
* 6th step if user want to addrecipe click the page will  show previw 
![Add-Recipe](https://user-images.githubusercontent.com/38302279/65090221-26cfbd00-d9b4-11e9-88c6-0bde8aed7c32.png)
### Result
* 7th step after user fill the addrecipe form and press the Publish button the Result page automatically appear on the 
app where can user can edit or delete the recipe Button appear on bottom of  Recipe card
![Result-of-Data](https://user-images.githubusercontent.com/38302279/65095897-e9226280-d9ba-11e9-8b0e-effaf0f96c42.png)
### Manage Category
* 8th step if user want to manage categories then click Manage-Categories 
![Manage-Categories](https://user-images.githubusercontent.com/38302279/65093222-dad14800-d9b4-11e9-8964-dc8fdf399305.png)
* 9th step if user want to add his own category then press Add_category Button when user add the category his own then press add the page get user to Manage categories where user can see his 
own category add in Manage Category Page.
### Add_category
![Add-Category](https://user-images.githubusercontent.com/38302279/65094589-7b276c80-d9b5-11e9-8974-754abba05330.png)
* 10th step if user want to Edit his own category then press Edit_category Button hange the category and then pressthe save Change Button
the page get user to Manage categories where user can see his edit_category
### Edit_category
![Edit-Categoery](https://user-images.githubusercontent.com/38302279/65094770-3bad5000-d9b6-11e9-862c-f1c9e4cc74d5.png)
* 11th step if user want to delete category his own or on the app user need to press delete button category will be delete on
 the Manage Categoery page.
### Delete_category
![Category-Delete1](https://user-images.githubusercontent.com/38302279/65094953-15d47b00-d9b7-11e9-80fc-fb76f2f565e5.png)
* in this example i show user want to delete category name birthday Party you will see this picture Birthday Party category
will show top of the Manage categories and second picture will show category delete in Manage Category page
![Category-Delete2](https://user-images.githubusercontent.com/38302279/65095041-7499f480-d9b7-11e9-8516-ea310e327d24.png)
* 12th step if user want to add his own cuisine then press Add_cuisine Button
* ### Manage Cuisine
![Manage-cuisine](https://user-images.githubusercontent.com/38302279/65095209-2a654300-d9b8-11e9-9c9a-45062cc32e33.png)
* step 14th when user add the cuisine his own then press add the page get user to Manage cuisine where user can see his 
own cuisine add in Manage-Cuisine Page.
### Add_cuisine
![Add-Cuisine](https://user-images.githubusercontent.com/38302279/65095213-305b2400-d9b8-11e9-8c64-e6f622ee4969.png)
### Edit_cuisine
* 13th step if user want to Edit his own cuisine then press Edit_cuisine Button
![Edit-Cuisine](https://user-images.githubusercontent.com/38302279/65095214-33561480-d9b8-11e9-80f3-5d59f65f8285.png)
* 16th step when user want to Edit his  own  Cuisine then press Edit button change the cuisine and then pressthe save Change Button
the page get user to Manage Cuisines where user can see his edit_cuisine
* 14th step if user want to delete cuisine his own or on the app user need to press delete button cuisine will be delete on
 the Manage cuisine page.
### delete_cuisine
![cuisine-delete1](https://user-images.githubusercontent.com/38302279/65095217-394bf580-d9b8-11e9-8c25-8a207c31cb90.png)
* in this example i show you if user want to delete cuisine name poland you will see this picture poland cuisine
will show bottom  of the Manage cuisines and second picture will show cuisine delete in Manage cuisine  page
![cuisine-delete2](https://user-images.githubusercontent.com/38302279/65095221-3b15b900-d9b8-11e9-9f1a-c20b9300a3e7.png)

## Database Schema
![Database_Schema_mongo](https://user-images.githubusercontent.com/38302279/65098588-153fe280-d9bf-11e9-91da-46a01f657902.png)


### Example schema from the 'recipes' collection:
```
{
    "_id": {
        "$oid": "5cbdf6f4e7179a264cf45ea0"
    },
    "cooking_time": "15 mins",
    "cuisine": "British",
    "method": "Bring a deep saucepan of water to the boil (at least 2 litres) and add the vinegar. Break the eggs into 4 separate coffee cups or ramekins. Split the muffins, toast them and warm some plates. Swirl the vinegared water briskly to form a vortex and slide in an egg. It will curl round and set to a neat round shape. Cook for 2-3 mins, then remove with a slotted spoon. Repeat with the other eggs, one at a time, re-swirling the water as you slide in the eggs. Spread some sauce on each muffin, scrunch a slice of ham on top, then top with an egg. Spoon over the remaining hollandaise and serve at once.",
    "ingredients": [
        "3 tbsp White Wine Vinegar",
        "2 Toasting Muffins",
        "4 Eggs",
        "4 slices Parma Ham",
        "1 batch Hollandaise sauce"
    ],
    "name": "Eggs Benedict",
    "image": "https://upload.wikimedia.org/wikipedia/commons/6/6f/Eggs_Benedict-01-cropped.jpg",
    "added_by": "cskinner",
    "prep_time": "5 mins",
    "category": "Breakfast",
    "serves": "2"
}
```


## FEATURES

##### Existing features

* **Register page** - will allow new user to register to get access to the application

* **Login page** - will allow user to login before using the application

* **'COOK-BOOK' - logo** - when clicked it will always bring the user to the home page

* **Navbar** - created to navigate particular list: (*recipes*, *categories* or *cusines*). Across the navbar the are links
with names of the lists. When hoover over the link color will change. For smaller devices the navbar collapse 
into *burger icon*.

* **'Add New Recipe' - button** - when clicked, it will allows the user to add new recipe

* **'Search By Category' - button** - when clicked, it will allows user to search recipes by particular category

* **'View' - button** - when clicked, will bring to individual recipe page

* **'Edit Recipe' - button** - allows user to edit particular recipe and make changes

* **'Delete' - button** - allows user to Delete particualar recipe

##### Features left to implement

* Feature that will allow user remove or edit(make changes) only its own recipes - but not others users recipes.


## TECHNOLOGIES USED

* **Git** - used command line to for regular commits and to push my project to github
* **Github** - used to remotely store project code and allow public to see my website
* **JQuery 3.3.1** - to assist the form.js file
* **Materialize 1.0.0** - https://materializecss.com/text-inputs.html used for imput fields
* **Material Design Icons** - https://material.io/resources/icons/?style=baseline used to add icons to the input fields
* **Heroku** - this application is hosted via heroku


##### Front-End Technologies

* **HTML** - to create basic structure
* **CSS** - to add styles to the websites
* **Java Script** to add quary in form.js file

##### Back-End Technologies

* **Flask** - to construct and render templates
* **Python 3.6.8** - used as the backend programming language
* **MongoDB Atlas** - database used to storewebsite backend data
* **PyMongo 3.8.0** - used for interacting with MongoDB database from Python
* **Jinja** - to display back-end data to the front-end
* **BSON ObjectId** - allows you to create and parse ObjectIDs without a reference to the MongoDB or bson modules

## TESTING

This website had been tested on different devices such as: Desktop, Tablet, Mobile. I used Chrome DevTools to make sure it works on: Samsung Galaxy S5, iPhone 5/6/7/8, iPad, PC Desktop;



## TROUBLESHOOTING

**Registration and Login system** - that was the biggest challenge but with lots of searching in google  websites I eventually  was able to create it

##### To be fixed

Add alert messages to registration and login system: 

* when user register to the app successfully - confirmation message should pop up
* when user login and try to use the same username which already exist - warning message should pop up

## DEPLOYMENT

##### GITHUB

I deploy my project by going to GitHub, navigate to my github pages site's repository. Under my repository name I clicked Settings. Then I used the Select
drop-down menu to select master branch and then save it. Now my project is deployed to github pages and accessible to anyone via URL.

Link to my github repository: https://github.com/ahsin59/online_festiive_cookbook_ms_project

##### HEROKU

In the terminal, I created a requirements.txt file using this command: pip freeze > requirements.txt.
In the terminal, I created a Procfile by running: echo web: python app.py > Procfile command.
I push these files to my GitHub repository.
I created a new app on Heroku dashboard, I named it 'COOK-BOOK and then I set the region.
I linked Github repository to Heroku.
I set the config vars as follows: IP 0.0.0.0 and PORT 5000.

My app can be found at: http://online-festive-cookbook.herokuapp.com/

To run this project you need to do the following:

* Go to Github repository and click on the 'clone or download' and copy the link https://github.com/ahsin59/online_festiive_cookbook_ms_project.git.
* Create virtual environment that helps to keep dependencies required by this project separate from other projects by creating isolated python virtual environments.
* Install all required modules by creating requirements.txt file.
* Create a .env file with the connection to MongoDB database, and a secret key.
* You can run this application by following command: python3 app.py

## CREDIT

##### Content

The Recipes I added to this page are from this website: https://www.bbc.co.uk/food/occasions

##### Aknowlegment

my mentor:  Anthnoy Negne and Tutor support and slack Team - my help throughout the project

