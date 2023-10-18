from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from server.forms import RegistrationForm, LoginForm
from server.models import User, Product, db

main = Blueprint('main', __name__)


@main.route('/')
def index():
    # Replace with your code to fetch products for different carousels
    top_sellers = Product.query.order_by(Product.sold.desc()).limit(10).all()
    random_products = Product.query.order_by(db.func.random()).limit(10).all()
    # Replace 'category_name' with the desired category
    category_products = Product.query.filter_by(
        category='category_name').limit(10).all()

    return render_template('index.html', top_sellers=top_sellers, random_products=random_products, category_products=category_products)


# Store Dashboard
@main.route('/dashboard')
@login_required
def dashboard():
    if not current_user.is_seller:
        flash('You do not have permission to access the dashboard.', 'danger')
        # Redirect to the home page or an error page
        return redirect(url_for('main.index'))

    products = Product.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', products=products)


# Display a list of products created by the store
@main.route('/products')
@login_required
def store_products():
    if not current_user.is_seller:
        flash('You do not have permission to access store products.', 'danger')
        # Redirect to the home page or an error page
        return redirect(url_for('main.index'))

    products = Product.query.filter_by(user_id=current_user.id).all()
    return render_template('store_products.html', products=products)

# Update an existing product


@main.route('/product/edit/<int:product_id>', methods=['GET', 'POST'])
@login_required
def edit_product(product_id):
    if not current_user.is_seller:
        flash('You do not have permission to edit products.', 'danger')
        # Redirect to the home page or an error page
        return redirect(url_for('main.index'))

    product = Product.query.get(product_id)
    if not product:
        flash('Product not found.', 'danger')
        # Redirect to the home page or an error page
        return redirect(url_for('main.index'))

    if request.method == 'POST':
        product.name = request.form.get('name')
        product.description = request.form.get('description')
        product.price = request.form.get('price')
        product.image = request.form.get('image')
        product.inventory = request.form.get('inventory')
        product.category = request.form.get('category')

        db.session.commit()
        flash('Product updated successfully!', 'success')
        return redirect(url_for('main.index'))

    # Create an HTML template for the product editing form
    return render_template('edit_product.html', product=product)

# Delete an existing product


@main.route('/product/delete/<int:product_id>', methods=['POST'])
@login_required
def delete_product(product_id):
    if not current_user.is_seller:
        flash('You do not have permission to delete products.', 'danger')
        # Redirect to the home page or an error page
        return redirect(url_for('main.index'))

    product = Product.query.get(product_id)
    if not product:
        flash('Product not found.', 'danger')
        # Redirect to the home page or an error page
        return redirect(url_for('main.index'))

    db.session.delete(product)
    db.session.commit()
    flash('Product deleted successfully!', 'success')
    return redirect(url_for('main.store_products'))


@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        # Hash the password before storing it
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(email=form.email.data,
                    password=hashed_password, name=form.name.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in.', 'success')
        login_user(user)
        return redirect(url_for('main.index'))
    return render_template('register.html', form=form)


@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            return redirect(url_for('main.index'))
        else:
            flash('Login unsuccessful. Please check email and password.', 'danger')
    return render_template('login.html', form=form)


@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


# Implement product detail page
@main.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get(product_id)
    if not product:
        flash('Product not found.', 'danger')
        # Redirect to the home page or an error page
        return redirect(url_for('main.index'))

    return render_template('product_detail.html', product=product)

# Implement the "Add to Cart" functionality


@main.route('/add_to_cart/<int:product_id>', methods=['POST'])
@login_required
def add_to_cart(product_id):
    product = Product.query.get(product_id)
    if not product:
        flash('Product not found.', 'danger')
        # Redirect to the home page or an error page
        return redirect(url_for('main.index'))

    # You can implement cart functionality here, e.g., adding the product to the user's cart
    # Consider using a session or database to manage the cart

    flash('Product added to your cart!', 'success')
    return redirect(url_for('main.index'))


# Create a new product
@main.route('/product/create', methods=['GET', 'POST'])
@login_required
def create_product():
    if not current_user.is_seller:
        flash('You do not have permission to create products.', 'danger')
        # Redirect to the home page or an error page
        return redirect(url_for('main.index'))

    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        price = request.form.get('price')
        image = request.form.get('image')
        inventory = request.form.get('inventory')
        category = request.form.get('category')

        product = Product(name=name, description=description, price=price,
                          image=image, inventory=inventory, category=category)
        db.session.add(product)
        db.session.commit()
        flash('Product created successfully!', 'success')
        return redirect(url_for('main.index'))

    # Create an HTML template for the product creation form
    return render_template('create_product.html')
