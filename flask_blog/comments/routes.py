from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flask_blog import db
from flask_blog.models import Comment, User, Post
from flask_blog.comments.forms import CommentForm

comments = Blueprint('comments', __name__)

@comments.route("/comment/new", methods=['GET', 'POST'])
@login_required
def new_comment():
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(comment=form.comment.data, author=current_user, post_id = post_id)
        db.session.add(comment)
        db.session.commit()
    return render_template('comments.html', form=form, image_file=image_file)

@comments.route("/comment", methods=['GET', 'POST'])
def comment():
    comments = Comment.query.order_by(Comment.date_posted.asc())
    return render_template('comments.html', comments=comments)