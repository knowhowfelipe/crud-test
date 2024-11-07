from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from .models import User, Item, db
from flask_login import login_user, logout_user, login_required, current_user

main = Blueprint('main', __name__)

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            flash('Login bem-sucedido!', 'success')
            return redirect(url_for('main.dashboard'))
        flash('Credenciais inválidas!', 'danger')
    return render_template('login.html')

@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você foi desconectado!', 'info')
    return redirect(url_for('main.login'))

@main.route('/dashboard')
@login_required
def dashboard():
    items = Item.query.all()
    return render_template('dashboard.html', items=items)

@main.route('/create', methods=['GET', 'POST'])
@login_required
def create_item():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        new_item = Item(name=name, description=description)
        db.session.add(new_item)
        db.session.commit()
        flash('Item criado com sucesso!', 'success')
        return redirect(url_for('main.dashboard'))
    return render_template('create_item.html')

@main.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_item(id):
    item = Item.query.get_or_404(id)
    if request.method == 'POST':
        item.name = request.form['name']
        item.description = request.form['description']
        db.session.commit()
        flash('Item atualizado com sucesso!', 'success')
        return redirect(url_for('main.dashboard'))
    return render_template('edit_item.html', item=item)

@main.route('/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_item(id):
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash('Item deletado com sucesso!', 'danger')
    return redirect(url_for('main.dashboard'))
