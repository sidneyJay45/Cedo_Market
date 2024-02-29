from flask import Flask, render_template, flash ,request
from flask_sqlalchemy import SQLAlchemy
from forms import RegisterForm, LoginForm , PurchaseItemForm, SellItemForm
from flask_login import login_required, current_user





app = Flask(__name__)
# SQLite3 database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'  # SQLite database file name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '51c88966a7b44053f2d07222'
items = [
    {"id": 1, "name": "Laptop", "barcode": "123456789", "price": 1200},
    {"id": 2, "name": "Keyboard", "barcode": "987654321", "price": 80},
    {"id": 3, "name": "Mouse", "barcode": "567890123", "price": 40},
    {"id": 4, "name": "Phone", "barcode": "334444444", "price": 450}  # New item
]



# Initialize the database
db = SQLAlchemy(app)

# Define a model for your database table
class Item(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(30), nullable=False, unique=True)
    Price = db.Column(db.Integer(), nullable=False)
    Barcode = db.Column(db.String(12), nullable=False, unique=True)
    Description = db.Column(db.String(1024), nullable=True)

# Route to view items in the database
@app.route('/view_items')
def view_items():
    # Fetch all items from the database
    items = Item.query.all()
    return render_template("view_items.html", items=items)

# Route for the home page
@app.route('/')
def home_page():
    return render_template("home.html")

@app.route('/market', methods=['GET', 'POST'])
def market_page():
    purchase_form = PurchaseItemForm()
    sell_form = SellItemForm()

    if request.method == 'POST' and purchase_form.validate_on_submit():
        purchased_item = purchase_form.item.data
        p_item_object = Item.query.filter_by(name=purchased_item).first()

    if request.method == 'POST' and sell_form.validate_on_submit():
        sell_item = sell_form.item.data
        s_item_object = Item.query.filter_by(name=sell_item).first()

        # Perform further processing or database operations here
        # For example, you might add code to process the purchase

    # Pass the items to the market.html template
    items = [
        {"id": 1, "name": "Laptop", "barcode": "123456789", "price": 1200},
        {"id": 2, "name": "Keyboard", "barcode": "987654321", "price": 80},
        {"id": 3, "name": "Mouse", "barcode": "567890123", "price": 40},
        {"id": 4, "name": "Phone", "barcode": "334444444", "price": 450}  # New item
    ]

    return render_template("market.html", items=items, purchase_form=purchase_form, sell_form=sell_form)


# Route for the register page
@app.route('/register', methods=['GET', 'POST'])
def register_page():
    # Create an instance of RegisterForm
    form = RegisterForm()

    # Validate the form when it's submitted
    if form.validate_on_submit():
        # Create a new user based on the form data
        user_to_create = User(
            username=form.username.data,
            email_address=form.email_address.data,
            password_hash=form.password1.data
        )

    # If there are errors in the form, display them using flash messages
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}')

    # Render the register.html template and pass the form to it
    return render_template('register.html', form=form)

@app.route('/login')
def login_page():
    return render_template("login.html")


@app.route('/logout')
def logout_page():
    return render_template("logout.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
