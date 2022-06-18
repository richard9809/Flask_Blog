from flask import render_template, request, Blueprint
from flask_blog.models import Post, Comment

main = Blueprint('main', __name__) 

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    comments = Comment.query.order_by(Comment.date_posted.desc()).limit(3)
    return render_template('home.html', posts=posts, comments=comments)

@main.route("/about")
def about():
    return render_template('about.html')
