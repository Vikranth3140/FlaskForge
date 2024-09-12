from flask import render_template
from flask_login import login_required
from app.main import bp
from app.models import Post

@bp.route('/')
@bp.route('/index')
def index():
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('main/index.html', title='Home', posts=posts)

@bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('main/dashboard.html', title='Dashboard')
