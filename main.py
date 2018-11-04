from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy


# TODO: When a user submits a new post, redirect them to the main blog page.
# TODO: Make a Blog class with the necessary properties (i.e., an id, title, and body), then initialize your database:

# (flask-env) $ python
# from main import db, Blog
# db.create_all()
# db.session.commit()

# TODO: /blog route displays all the blog posts.

# TODO: submit a new post at the /newpost route

# TODO: two templates, one each for the /blog (main blog listings) and /newpost (post new blog entry) views. Your templates should extend a base.html template which includes some boilerplate HTML that will be used on each page.

# TODO:
# TODO:
# TODO:
# TODO:
# TODO:



app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:introducingKat@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)



class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    # The name is the column within task name
    name = db.Column(db.String(120))
    completed = db.Column(db.Boolean)

# Create a constructor: 
    def __init__(self, name):
        self.name = name
        self.completed = False


@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        blog_name = request.form['task']
        new_blog = Blog(blog_name)
        db.session.add(new_blog)
        db.session.commit()

# Change template name

    tasks = Blog.query.filter_by(completed=False).all()
    completed_tasks = Blog.query.filter_by(completed=True).all()
    return render_template('entries.html',title="Build a Blog!", 
        tasks=tasks, completed_tasks=completed_tasks)


@app.route('/blog', methods=['POST'])
def delete_task():

    task_id = int(request.form['task-id'])
    task = Blog.query.get(task_id)
    task.completed = True
    db.session.add(task)
    db.session.commit()

    return redirect('/')


@app.route('/newpost', methods=['POST'])
def delete_task():

    task_id = int(request.form['task-id'])
    task = Task.query.get(task_id)
    task.completed = True
    db.session.add(task)
    db.session.commit()

    return redirect('/')
if __name__ == '__main__':
    app.run()