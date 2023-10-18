from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from server.forms import RegistrationForm, LoginForm
from server.models import User, Product, db

main = Blueprint('main', __name__)


@main.route('/')
def index():
    # Replace with your welcome screen template
    return render_template('index.html')


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
