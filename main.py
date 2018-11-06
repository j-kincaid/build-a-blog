from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy


# TODO: When a user submits a new post, redirect them to the main blog page.

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



# TODO: Make a Blog class with the necessary properties (i.e., an id, title, and body), then initialize your database with these:

# (flask-env) $ python
# from main import db, Blog
# db.create_all()
# db.session.commit()

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # The name is the column within word name
    title = db.Column(db.String(120))
    body = db.Column(db.Text)

# Create a constructor: 
    def __init__(self, title, body):
        self.title = title
        self.body = body

# @app.route('/', methods=['POST', 'GET'])
# def index():

#     words = Blog.query.filter_by(completed=False).all()
#     completed_words = Blog.query.filter_by(completed=True).all()
#     return render_template('entries.html',title="Build a Blog!", 
#         words=words, completed_words=completed_words)

@app.route('/blog')
def index():
    return render_template('blog.html')

@app.route('/blog', methods=['POST'])
def add_entry():

    if request.method == 'POST':
        blog_name = request.form['word']
        new_blog = Blog(blog_name)
        db.session.add(new_blog)
        db.session.commit()

    return render_template('entries.html')



@app.route('/newpost', methods=['POST'])
def process_add_entry():

    word_id = int(request.form['word-id'])
    word = word.query.get(word_id)
    word.completed = True
    db.session.add(word)
    db.session.commit()

    return redirect('/')
if __name__ == '__main__':
    app.run()