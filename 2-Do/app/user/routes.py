import uuid
from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    request,
    jsonify,
    flash,
)
from flask_login import login_required, current_user
from app.models.todo import Todo
from app.user.form import CreateTodoForm, EditTodoForm
from app import db
from sqlalchemy import or_
from app.auth.forms import LoginForm

user = Blueprint("user", __name__)


# Valid if ID is in uuid format
def is_valid_uuid(user_id):
    try:
        uuid.UUID(user_id, version=4)
        return True
    except ValueError:
        return False


@user.route("/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template("login.html", form=form)


@user.route("/home", methods=["GET", "POST"])
@login_required
def home():
    """
    Render the home page and handle form submissions to create a new todo.

    Method: POST
    Form Fields:
        - todo_content: Content of the todo (required)
        - todo_category: Category of the todo (required)
    """
    if request.method == "POST":
        todo_content = request.form.get("todo_content")
        todo_category = request.form.get("todo_category")

        if not todo_content or not todo_category:
            return jsonify({"status": "error", "message": "Incomplete data"})

        new_todo = Todo(
            content=todo_content, category=todo_category, user_id=current_user.id
        )
        db.session.add(new_todo)
        db.session.commit()

    todos = Todo.query.filter_by(user_id=current_user.id).all()

    return render_template("index.html", user=current_user, todos=todos)


@user.route("/create_todo", methods=["GET", "POST"])
@login_required
def create_todo():
    """
    Create a new todo via AJAX request.

    Method: POST
    JSON Payload:
        - todo_content: Content of the todo (required)
        - todo_category: Category of the todo (required)
    """
    form = CreateTodoForm()

    if form.validate_on_submit():
        new_todo = Todo(
            title=form.title.data,
            content=form.content.data,
            category=form.category.data,
            start_time=form.start_time.data,
            end_time=form.end_time.data,
            user=current_user,
        )
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for("user.home"))

    if request.method == "POST":
        return jsonify({"status": "error", "message": "Incomplete data"})

    return render_template("create_todo.html", form=form)


@user.route("/edit_todo/<string:todo_id>", methods=["GET", "POST"])
@login_required
def edit_todo(todo_id):
    """
    Edit an existing todo.

    Method: PUT
    Form Fields:
        - title: New title of the todo (required)
        - content: New content of the todo (required)
        - category: New category of the todo (required)
        - start_time: New start time of the todo (required)
        - end_time: New end time of the todo (required)
    """
    if not is_valid_uuid(todo_id):
        return jsonify({"status": "error", "message": "Invalid todo ID"})

    todo = Todo.query.get(todo_id)

    if not todo or todo.user_id != current_user.id:
        return jsonify({"status": "error", "message": "Invalid todo"})

    form = EditTodoForm(obj=todo)  # Pass the todo object to pre-fill the form

    if request.method == "POST":
        if form.validate_on_submit():
            # Update the existing todo
            todo.title = form.title.data
            todo.content = form.content.data
            todo.category = form.category.data

            db.session.commit()
            flash("Todo updated successfully", "success")
            return redirect(url_for("user.home"))

    return render_template("edit_todo.html", todo=todo, form=form)


@user.route("/delete_todo/<string:todo_id>", methods=["GET", "DELETE"])
@login_required
def delete_todo(todo_id):
    """
    Delete an existing todo.

    Method: POST
    """
    if not is_valid_uuid(todo_id):
        return jsonify({"status": "error", "message": "Invalid todo ID"})

    todo = Todo.query.get(todo_id)

    if not todo or todo.user_id != current_user.id:
        return jsonify({"status": "error", "message": "Todo not found"})

    db.session.delete(todo)
    db.session.commit()

    flash("Todo deleted successfully", "success")
    return redirect(url_for("user.home"))


@user.route("/search", methods=["GET"])
@login_required
def search():
    """
    Search for todos based on the title or category parameters.
    """
    query = request.args.get("query", "")

     # Perform the search based on the title or category, and associated with the logged-in user
    todos = Todo.query.filter(
        (Todo.title.ilike(f"%{query}%") | Todo.category.ilike(f"%{query}%")) &
        (Todo.user_id == current_user.id)
    ).all()

    # Render the search results
    return render_template("search_results.html", query=query, todos=todos)
